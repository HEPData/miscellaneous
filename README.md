# miscellaneous
Miscellaneous material not directly related to another HEPData repository

## [notebooks](notebooks)

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/HEPData/miscellaneous/main?filepath=notebooks)

### [count_inspire_records_with_hepdata.ipynb](notebooks/count_inspire_records_with_hepdata.ipynb)

This Jupyter notebook counts all [INSPIRE](https://inspirehep.net) records
that have an associated [HEPData](https://www.hepdata.net) record using the
[INSPIRE API](https://github.com/inspirehep/rest-api-doc).

Count publications per LHC experiment per year and see which fraction
has a HEPData record.

Written by Graeme Watt (Project Manager for HEPData) on 11th October 2017.
Updated for new INSPIRE API on 15th April 2021.

### [plot_submissions_per_coordinator.ipynb](notebooks/plot_submissions_per_coordinator.ipynb)

This Jupyter notebook makes some plots showing the number of HEPData
submissions in progress and finished by different experiments, including
a breakdown by the different ATLAS and CMS physics groups.  The input is
a CSV file obtained by running the command
`hepdata submissions write-stats-to-files`
in the production environment.

### [plot_submissions_with_date.ipynb](notebooks/plot_submissions_with_date.ipynb)

This Jupyter notebook makes a plot showing the number of "version 1"
HEPData submissions per month, with a linear fit overlaid.  Again, the
input is a (different) CSV file obtained by running the command
`hepdata submissions write-stats-to-files`
in the production environment.

### [investigate_hepdata_release_delay.ipynb](notebooks/investigate_hepdata_release_delay.ipynb)

This Jupyter notebook investigates the delay between arXiv publication, indicated by creation of
an [INSPIRE](https://inspirehep.net) record, and release of the first version of a corresponding
[HEPData](https://www.hepdata.net) record.  A histogram is plotted of these delays for a given
time period and experimental collaboration.

Written by Graeme Watt on 25th November 2022.

### [compare_inspire_and_hepdata.ipynb](notebooks/compare_inspire_and_hepdata.ipynb)

This Jupyter notebook investigates the consistency between the INSPIRE record numbers obtained from
either [INSPIRE](https://inspirehep.net) or [HEPData](https://www.hepdata.net).  Discrepancies usually
occur because an INSPIRE record has changed its record number.

### [compare_latex_to_unicode.ipynb](notebooks/compare_latex_to_unicode.ipynb)

This Jupyter notebook compares the LaTeX to Unicode conversions obtained with three different Python packages:
[latex2text](https://pylatexenc.readthedocs.io/en/latest/latex2text/),
[unicodeit](https://github.com/svenkreiss/unicodeit) and
[unicodeitplus](https://github.com/HDembinski/unicodeitplus).
Test data is obtained from the publication titles of all finished [HEPData](https://hepdata.net) records.
The intended application is to [tweet](https://twitter.com/HEPData) these titles when the HEPData records
are first released or later revised.

### [get_access_count.ipynb](notebooks/get_access_count.ipynb)

This Jupyter notebook gets the access count of all records in [HEPData](https://www.hepdata.net/) from the
ATLAS experiment.  It first makes a paginated search
"[collaborations:ATLAS](https://www.hepdata.net/search/?q=collaborations%3AATLAS&sort_by=date)"
to find the [INSPIRE](https://inspirehep.net) IDs.  Then the JSON format of individual records is retrieved
to get the access counts and associated metadata, using the `light=true` option to reduce the size of the
JSON by removing data tables.  See [JSON Endpoints](https://www.hepdata.net/formats#json_endpoints).  The output
is written to a CSV file for possible further analysis by Python, Excel, etc.