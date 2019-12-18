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

### [plot_submissions_per_coordinator.ipynb](notebooks/plot_submissions_per_coordinator.ipynb)

This Jupyter notebook makes some plots showing the number of HEPData
submissions in progress and finished by different experiments, including
a breakdown by the different ATLAS and CMS physics groups.  The input is
a CSV file obtained by running the command
`hepdata submissions write_stats_to_files`
in the production environment.

### [plot_submissions_with_date.ipynb](notebooks/plot_submissions_with_date.ipynb)

This Jupyter notebook makes a plot showing the number of "version 1"
HEPData submissions per month, with a linear fit overlaid.  Again, the
input is a (different) CSV file obtained by running the command
`hepdata submissions write_stats_to_files`
in the production environment.

## [scripts](scripts)

Note added: updated versions of the `rivet-diffhepdata` and
`rivet-diffhepdata-all` scripts linked below are now included
in the official [Rivet](http://rivet.hepforge.org) distribution.

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

### [rivet-diffhepdata-all](scripts/rivet-diffhepdata-all)

This Python script loops over all INSPIRE IDs given in
[analyses.json](http://rivet.hepforge.org/analyses.json) and compares
each [Rivet](http://rivet.hepforge.org) `.yoda` file with the
corresponding HEPData download.  It calls functions from the previous
[rivet-diffhepdata](scripts/rivet-diffhepdata) script which in turn calls
[yodadiff](https://yoda.hepforge.org/trac/browser/bin/yodadiff).  See example
[output](http://www.ippp.dur.ac.uk/%7Ewatt/RivetDiffHEPData/Rivet-2.6.0/).