# miscellaneous
Miscellaneous material not directly related to another HEPData repository

## [notebooks](notebooks)

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/HEPData/miscellaneous/master?filepath=notebooks)

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