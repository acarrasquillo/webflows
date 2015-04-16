#!/usr/bin/env python

# Use print functions (Compatible with Python 3.0; Requires 2.6+)

from __future__ import print_function

# Import the PySiLK bindings
from silk import *

# Import Json Silk and json
import jsonsilk, json

for filename in FGlob(type="all", start_date="2015/03/09",
site_config_file="/data/conf-v9/silk.conf",
data_rootdir="/scratch/flow/rwflowpack/"):
    print (filename)
    recordList = list()
    for rec in silkfile_open(filename, READ):
	#convert the record to valid json serialisable dic
	serRec = jsonsilk.serializableRecord(rec.as_dict())
	#add the record to the list
	recordList.append(serRec)

    jsonlist = json.dumps(recordList)

    print (jsonlist)

    
