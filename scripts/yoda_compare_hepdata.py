#! /usr/bin/env python

"""\
%prog [-h|--help] yodafile [-i|--inspire_id INSPIRE_ID] [-d|--yodafile_from_hepdata YODAFILE_FROM_HEPDATA] [-a|--annotations]

Check compatibility of a YODA reference data file, intended for inclusion in Rivet, with the YODA file downloaded from HEPData.

Specify either the INSPIRE_ID (to download the YODA file from HEPData) or the already-downloaded YODAFILE_FROM_HEPDATA.
There is an option to also compare annotations (not done by default) with "-a" or "--annotations".

Examples:
 %prog ATLAS_2017_I1614149.yoda -i 1614149 -a
 %prog ATLAS_2017_I1614149.yoda -d HEPData-ins1614149-v2-yoda.yoda -a

Note added: much of the functionality of this script, apart from the HEPData download and optional comparison of annotations,
is already available in the yodadiff script distributed with YODA (https://yoda.hepforge.org/trac/browser/bin/yodadiff).
"""

from __future__ import print_function
import yoda

import logging
logging.basicConfig(format='%(levelname)s: %(msg)s', level='INFO')
logger = logging.getLogger(__name__)

__author__ = 'Graeme Watt'

def main():
    """ Main function for command-line usage. """
    import argparse
    parser = argparse.ArgumentParser(description='Check compatibility of YODA reference data file with HEPData')
    parser.add_argument('yodafile', help='name of YODA reference data file (intended for inclusion in Rivet)')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-i', '--inspire_id', nargs=1, default=[0], type=int, help='INSPIRE ID (to download the YODA file from HEPData')
    group.add_argument('-d', '--yodafile_from_hepdata', nargs=1, default=[None], help='name of YODA file already downloaded from HEPData')
    parser.add_argument('-a', '--annotations', action='store_true', help='also compare annotations (not done by default)')
    args = parser.parse_args()
    compatible = compare_hepdata(args.yodafile, args.inspire_id[0], args.yodafile_from_hepdata[0], args.annotations)
    if compatible:
        print('YODA reference data files from Rivet and HEPData are compatible!')
    else:
        print('YODA reference data files from Rivet and HEPData are NOT compatible!')


def compare_hepdata(yodafile, inspire_id=0, yodafile_from_hepdata=None, annotations=False):
    """\
    Compare a YODA reference data file, intended for inclusion in Rivet, with the YODA file downloaded from HEPData.

    Loop over all analysis objects in Rivet YODA file and compare to corresponding analysis object in HEPData YODA file.
    This allows for the possibility that the HEPData YODA file may contain additional analysis objects not in Rivet.

    :param yodafile: name of YODA reference data file (intended for inclusion in Rivet)
    :param inspire_id: INSPIRE ID (to download the YODA file from HEPData)
    :param yodafile_from_hepdata: name of YODA file already downloaded from HEPData
    :param annotations: also compare annotations (not done by default)
    :return: True or False depending on whether YODA files are compatible
    """

    logger.info('Reading %s' % yodafile)
    aos = yoda.read(yodafile, asdict=False)

    if inspire_id:
        yodafile_from_hepdata = download_from_hepdata(inspire_id)

    if yodafile_from_hepdata:
        logger.info('Reading %s' % yodafile_from_hepdata)
        aos_from_hepdata = yoda.read(yodafile_from_hepdata)
    else:
        logger.error('No YODA file from HEPData specified')
        return False

    for ao in aos:
        if ao.path in aos_from_hepdata:
            logger.info('Found %s in %s' % (ao.path, yodafile_from_hepdata))
            ao_from_hepdata = aos_from_hepdata[ao.path]
            equal_scatters = check_scatters_equal(ao, ao_from_hepdata)
            if not equal_scatters:
                return False
            if annotations:
                logger.info('Comparing annotations for %s' % ao.path)
                equal_annotations = check_annotations_equal(ao, ao_from_hepdata)
                if not equal_annotations:
                    return False
            else:
                logger.info('Not comparing annotations for %s' % ao.path)
        else:
            logger.error('Not found %s in %s' % (ao.path, yodafile_from_hepdata))
            return False

    return True


def download_from_hepdata(inspire_id):
    """\
    Download the latest YODA reference data file from HEPData identified by the INSPIRE ID.
    Function contents modified from https://rivet.hepforge.org/trac/browser/bin/rivet-mkanalysis.
    It would be nicer to use the "requests" module if it can be assumed to be available.

    :param inspire_id: INSPIRE ID
    :return: name of YODA file downloaded from HEPData
    """

    import tarfile, io
    try:
        from urllib.request import urlopen
        from urllib.error import URLError
    except:
        from urllib2 import urlopen, URLError
    #
    hdurl = "https://hepdata.net/record/ins%s" % inspire_id
    logger.info("Downloading from %s" % hdurl)
    try:
        response = urlopen(hdurl + '?format=yoda')
    except URLError as e:
        logger.error("Download failed (%s), does %s exist?" % (e.reason, hdurl))
        return None
    download = response.read()
    tar = tarfile.open(mode="r:gz", fileobj=io.BytesIO(download))
    tar.extractall()
    yodafile_from_hepdata = tar.getnames()[0]
    response.close()
    logger.info("Downloaded %s" % yodafile_from_hepdata)
    return yodafile_from_hepdata


def check_scatters_equal(s, s1):
    """\
    Check that two Scatter objects (Scatter1D, Scatter2D, Scatter3D) are compatible.

    :param s: a Scatter object
    :param s1: another Scatter object
    :return: True or False depending on whether Scatter objects are compatible
    """

    if s.type != s1.type:
        logger.error("Different Scatter type (%s and %s)" % (s.type, s1.type))
        return False
    elif s.dim != s1.dim:
        logger.error("Different Scatter dim (%d and %d)" % (s.dim, s1.dim))
        return False
    elif s.numPoints != s1.numPoints:
        logger.error("Different Scatter numPoints (%d and %d)" % (s.numPoints, s1.numPoints))
        return False
    else:
        for i, p in enumerate(s.points):
            p1 = s1.points[i]
            equal_points = check_points_equal(p, p1)
            if not equal_points:
                logger.error("Point %d of %s not equal" % (i, s.path))
                return False
    return True


def check_points_equal(p, p1):
    """\
    Check that two Point objects (Point1D, Point2D, Point3D) are compatible (with allowance for rounding errors).

    :param p: a Point object
    :param p1: another Point object
    :return: True or False depending on whether Point objects are compatible
    """

    if p.dim != p1.dim:
        logger.error("Different Point dim (%d and %d)" % (p.dim, p1.dim))
        return False
    else:
        for i in range(1, p.dim + 1):
            same_val = fuzzyEquals(p.val(i), p1.val(i))
            same_eminus = fuzzyEquals(p.errMinus(i), p1.errMinus(i))
            same_eplus = fuzzyEquals(p.errPlus(i), p1.errPlus(i))
            same = same_val and same_eminus and same_eplus
            if not same:
                return False
    return True


def isZero(val, tolerance=1e-8):
    """\
    Compare a floating point number to zero with a degree of fuzziness expressed by the absolute tolerance parameter.
    Copied from C++ implementation in https://yoda.hepforge.org/trac/browser/include/YODA/Utils/MathUtils.h.

    :param val: floating point number
    :param tolerance: absolute tolerance parameter
    :return: True or False depending on whether val is compatible with zero
    """

    return abs(val) < tolerance


def fuzzyEquals(a, b, tolerance=1e-5):
    """\
    Compare two floating point numbers for equality with a degree of fuzziness.
    Copied from C++ implementation in https://yoda.hepforge.org/trac/browser/include/YODA/Utils/MathUtils.h.

    :param a: first floating point number
    :param b: second floating point number
    :param tolerance: fractional tolerance parameter, based on absolute values of the args a and b
    :return: True or False depending on whether a and b are compatible
    """

    absavg = (abs(a) + abs(b))/2.0
    absdiff = abs(a - b)
    rtn = (isZero(a) and isZero(b)) or absdiff < tolerance*absavg
    return rtn


def check_annotations_equal(s, s1):
    """\
    Check that annotations from two Scatter objects (Scatter1D, Scatter2D, Scatter3D) are compatible.

    :param s: a Scatter object
    :param s1: another Scatter object
    :return: True or False depending on whether annotations of Scatter objects are compatible
    """

    missing_annotations = [item for item in s.annotations if item not in s1.annotations]
    if missing_annotations:
        logger.warning('Missing annotations from HEPData: %s' % missing_annotations)

    missing_annotations1 = [item for item in s1.annotations if item not in s.annotations]
    if missing_annotations1:
        logger.warning('Missing annotations from Rivet: %s' % missing_annotations1)

    if missing_annotations + missing_annotations1:
       return False

    else:
        for annotation in s.annotations:
            if s.annotation(annotation) != s1.annotation(annotation):
                logger.warning('Different %s annotations (%s, %s)' %
                               (annotation, s.annotation(annotation), s1.annotation(annotation)))
                return False

    return True


if __name__ == "__main__":
    main()