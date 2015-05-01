#!/usr/bin/env python
import cgi,os,sys,json
import cgitb; cgitb.enable()  # for troubleshooting

from __future__ import print_function

# Import the PySiLK bindings
from silk import *

# Import Json Silk and json
import jsonsilk, json

print "Content-type: text/html"
print
length = os.environ["CONTENT_LENGTH"] 
jsonData =  sys.stdin.read(int(length))
# convert the json to a python object()
queryDic = json.loads(jsonData)
# take the query values out
recordList = list()
for filename in FGlob(type="all", start_date="2015/03/09", site_config_file="/data/conf-v9/silk.conf", data_rootdir="/scratch/flow/rwflowpack/"):
    for rec in silkfile_open(filename, READ):
		#convert the record to valid json serialisable dic
		serRec = jsonsilk.serializableRecord(rec.as_dict())
		#add the record to the list
		recordList.append(serRec)

jsonlist = json.dumps(recordList)

print jsonlist