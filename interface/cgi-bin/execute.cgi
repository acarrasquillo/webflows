#!/usr/bin/env python
import __future__
import cgi,os,sys,json, silk, jsonsilk
import cgitb; cgitb.enable()  # for troubleshooting

print "Content-type: text/html"
print
length = os.environ["CONTENT_LENGTH"] 
jsonData =  sys.stdin.read(int(length))
queryDict = json.loads(jsonData)
# take the query values out and do input validation
ipValue = queryDict['ipValue'] if 'ipValue' in queryDict else False
portValue = queryDict['portValue'] if 'portValue' in queryDict else False
nexthopValue = queryDict['nexthopValue'] if 'nexthopValue' in queryDict else False
outputValue = queryDict['outputValue'] if 'outputValue' in queryDict else False
inputValue = queryDict['inputValue'] if 'inputValue' in queryDict else False
dOctetsValue = queryDict['dOctetsValue'] if 'dOctetsValue' in queryDict else False
firstValue = queryDict['firstValue'] if 'firstValue' in queryDict else False
lastValue = queryDict['lastValue'] if 'lastValue' in queryDict else False
tcpFlagsValue = queryDict['tcpFlagsValue'] if 'tcpFlagsValue' in queryDict else False
protValue = queryDict['protValue'] if 'protValue' in queryDict else False

results = dict()
recordList = list()
failInfo = list()
for filename in silk.FGlob(type="all", start_date="2015/03/09", site_config_file="/data/conf-v9/silk.conf", data_rootdir="/scratch/flow/rwflowpack/"):
    for rec in silk.silkfile_open(filename, silk.READ):

        flag, info = jsonsilk.checkRec(rec,queryDict)
        
        if flag:

            # convert the record to valid json serialisable dic
            serRec = jsonsilk.serializableRecord(rec.as_dict())
            #add the record to the list
            recordList.append(serRec)   
        else:
            failInfo.append(info)

# if records found return the result
if len(recordList) > 0:
    results["count"] = len(recordList)
    results["result"] = recordList
    jsonResult = json.dumps(results)
# else return the information of failure
else:
    results["count"] = len(failInfo)
    results["fails"] = failInfo
    jsonResult = json.dumps(results)

print jsonResult 