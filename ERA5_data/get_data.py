# **************************** LICENSE START ***********************************
#
# Copyright 2022 ECMWF. This software is distributed under the terms
# of the Apache License version 2.0. In applying this license, ECMWF does not
# waive the privileges and immunities granted to it by virtue of its status as
# an Intergovernmental Organization or submit itself to any jurisdiction.
#
# ***************************** LICENSE END ************************************
import cdsapi
 
c = cdsapi.Client()
 
c.retrieve('reanalysis-era5-complete', {
 
    'class': 'ea',
 
    'date': '2021-09-02',
 
    'expver': '1',
 
    'levelist':'1/to/137',
 
    'levtype': 'ml',
 
    'param': '130/152',
 
    'step': '0',
 
    'stream': 'oper',
 
    'time': '00:00:00',
 
    'type': 'an',
 
    'grid': '0.25/0.25'
 
}, 'output_00_06_130_152_1x1.grib')