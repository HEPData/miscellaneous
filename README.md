# miscellaneous
Miscellaneous material not directly related to another HEPData repository

## [notebooks](notebooks)

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/HEPData/miscellaneous/master?filepath=notebooks)

### [count_inspire_records_with_hepdata.ipynb](notebooks/count_inspire_records_with_hepdata.ipynb)

This Jupyter notebook counts all [Inspire](https://inspirehep.net) records
that have an associated HEPData record using the
[Inspire API](https://inspirehep.net/info/hep/api).

Count publications per LHC experiment per year and see which fraction
has a HEPData record.

Written by Graeme Watt (Project Manager for HEPData) on 11th October 2017.

## [scripts](scripts)

### [yoda_compare_hepdata.py](scripts/yoda_compare_hepdata.py)

This Python script checks compatibility of a [YODA](http://yoda.hepforge.org)
reference data file, intended for inclusion in [Rivet](http://rivet.hepforge.org),
with the YODA file downloaded from [HEPData](https://hepdata.net).

### [rivet-diffhepdata](scripts/rivet-diffhepdata)

This Python script does much the same as
[yoda_compare_hepdata.py](scripts/yoda_compare_hepdata.py) but it uses
the [yodadiff](https://yoda.hepforge.org/trac/browser/bin/yodadiff)
script distributed with [YODA](http://yoda.hepforge.org).  It is
intended for possible future inclusion in the
[Rivet](http://rivet.hepforge.org) distribution.