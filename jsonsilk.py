#! /usr/bin/python

# Import the PySiLK bindigs
from silk import *

# Import datetime, json (JavaScript Object Notation)
import datetime, json

##################################################
#	Function: is_int(s)
#		Recieves: 
#			a String
#		Returns:
#			Boolean - True if s is a integer, otherwise False
##################################################
def is_int(s):
  try:
    int(s)
    return True
  except ValueError:
    return False
##################################################
#	Function: validRWRecDict(recDict)
#		recieves:  
#			a python dictionary with the record data
#		returns:
#			a valid python dictionary to create a silk.RWRec
#			
#	See the RWRec object instance attributes:
#		https://tools.netsa.cert.org/silk/pysilk.html#RWRec-Object
##################################################
def validRWRecDict(recDict):

	# Insert the silk object using the object string representation
	
	# Convert the string ipAddress to silk.IPAddress objects
	if 'sip' in recDict:
		recDict['sip'] = IPAddr(recDict['sip'])
	
	if 'nhip' in recDict:
	 	recDict['nhip'] = IPAddr(recDict['nhip'])
	
	if 'dip' in recDict:
	 	recDict['dip'] = IPAddr(recDict['dip'])

	# Convert the date strings to python Datetime Objects
	
	fmtDatetime = "%Y-%m-%d %H:%M:%S.%f"
	fmtTimeDelta = "%H:%M:%S.%f"
	
	# Convert the start time string back to python Datetime Object
	if 'stime' in recDict:
		recDict['stime'] = datetime.datetime.strptime(recDict['stime'], fmtDatetime)
	
	# Convert the end time string back to python Datetime Object
	if 'etime' in recDict:
		recDict['etime'] = datetime.datetime.strptime(recDict['etime'], fmt)

	# The record duration time
	if 'duration' in recDict:
		# Get the string datetime object representation
		t = datetime.datetime.strptime(recDict['duration'], fmtTimeDelta)

		# Create the timedelta object from the datetime object
		recDict['duration'] = datetime.timedelta(hours= t.hour, minutes= t.minute, seconds= t.second)

	# Convert the TCPFlags objects to string
	
	if 'tcpflags' in recDict:
		recDict['tcpflags'] = TCPFlags(recDict['tcpflags'])

	if 'initial_tcpflags' in recDict:
		recDict['initial_tcpflags'] = TCPFlags(recDict['initial_tcpflags'])

	if 'session_tcpflags' in recDict:
		recDict['session_tcpflags'] = TCPFlags(recDict['session_tcpflags'])


	return recDict

##################################################
#	Function: serializableRecord(recDict)
#		recieves:  
#			a silk.RWRec.as_dict() dictionary representation of a silk record
#		returns:
#			a silk record dictionary json serializable.
#			
#	See the RWRec object instance attributes:
#		https://tools.netsa.cert.org/silk/pysilk.html#RWRec-Object
##################################################
def serializableRecord(recDict):

	# Insert the string representation of objects in the record dictionary
	
	# Convert the IPAddress objects to string
	if 'sip' in recDict:
		recDict['sip'] = str(recDict['sip'])
	
	if 'nhip' in recDict:
		recDict['nhip'] = str(recDict['nhip'])
	
	if 'dip' in recDict:
		recDict['dip'] = str(recDict['dip'])

	# Conver the Datetimes objects to string
	
	if 'stime' in recDict:
		recDict['stime'] = str(recDict['stime'])
	
	if 'duration' in recDict:
		recDict['duration'] = str(recDict['duration'])

	if 'etime' in recDict:
		recDict['etime'] = str(recDict['etime'])

	# Convert the TCPFlags objects to string
	
	if 'tcpflags' in recDict:
		recDict['tcpflags'] = str(recDict['tcpflags'])

	if 'initial_tcpflags' in recDict:
		recDict['initial_tcpflags'] = str(recDict['initial_tcpflags'])

	if 'session_tcpflags' in recDict:
		recDict['session_tcpflags'] = str(recDict['session_tcpflags'])
	
	# Return the new dictionary
	return recDict

##################################################
#	Function: dumps(record)
#		recieves:  
#			a silk.RWRec, a silk record
#		returns:
#			a silk record json.
##################################################
def dumps(record):
	# Get the dictionary representation of the record
	recDict = record.as_dict()

	# We need the string representation of some values in the dictionary to convert it to JSON
	recDict = serializableRecord(recDict)

	# serialize the record to json
	jsonRec = json.dumps(recDict)

	# return the record json representation
	return jsonRec

##################################################
#	Function: loads(jsonrecord)
#		recieves:  
#			a json silk record
#		returns:
#			a silk record dictionary, silk.RWRec.as_dict().
##################################################
def loads(jsonRec):

	# Deserialize the json
	recDict = json.loads(jsonRec)

	# Convert it to a valid silk.RWRec dictionary representation
	recDict = validRWRecDict(recDict)

	# Return the dictionary
	return recDict


###########################################################
#	function: fRecTosRec(**kwargs)
#	
#	recieves: **kwargs NetFlow v5 dictionary with NetFlow v5 key fields and their values
#	
#	returns: A silkRWRec from the NetFlow v5 dictionary
#
###########################################################
"""
					NetFlow v5 format 												  | Silk Record

Bytes 	Contents 	Description															Required	SiLKField

0-3 	srcaddr 	Source IP address													Yes    		sip

4-7 	dstaddr 	Destination IP address												Yes 		dip

8-11 	nexthop 	IP address of next hop router										Yes 		nhip

12-13	input 		SNMP index of input interface										Yes 		input

14-15 	output 		SNMP index of output interface										Yes 		output

16-19 	dPkts 		Packets in the flow 												Yes 		packets

20-23 	dOctets 	Total number of Layer 3 bytes in the packets of the flow 			Yes 		bytes 		

24-27 	First 		SysUptime at start of flow 											Yes  		stime		

28-31 	Last 		SysUptime at the time the last packet of the flow was received 		Yes  		etime	

32-33 	srcport 	TCP/UDP source port number or equivalent 							Yes 		sport

34-35 	dstport 	TCP/UDP destination port number or equivalent 						Yes 		dport

36 		pad1 		Unused (zero) bytes 												No 			-

37 		tcp_flags 	Cumulative OR of TCP flags 											Yes 		tcpflags

38 		prot 		IP protocol type (for example, TCP = 6; UDP = 17) 					Yes 		protocol

39 		tos 		IP type of service (ToS) 											No 			N/A

40-41 	src_as 		Autonomous system number of the source, either origin or peer 		No 			N/A

42-43 	dst_as 		Autonomous system number of the destination, either origin or peer 	No 			N/A

44 		src_mask 	Source address prefix mask bits 									No 			N/A

45 		dst_mask 	Destination address prefix mask bits 								No 			N/A

46-47 	pad2 		Unused (zero) bytes 												No 			-
"""
def fRecTosRec(srcaddr, dstaddr, index_input, index_output, dpkts, doctets, first, last, srcport, dstport,prot, **kwargs):

	# dict to construct a silk.RWRec from the NetFlow v5 dict
	rec = dict()
		
	rec['sip'] = srcaddr

	rec['dip'] = dstaddr
	
	rec['input'] = index_input

	rec['output'] = index_output

	rec['packets'] = dpkts

	rec['bytes'] = doctets

	rec['stime'] = first

	rec['etime'] = last

	rec['sport'] = srcport

	rec['dport'] = dstport

	rec['protocol'] = prot

	rec = serializableRecord(rec)

	try:
		rec = silk.RWRec(rec)
	except Exception, e:
		raise "Error constructing Netflow v5 to RWRec: \n\t %s \n" % rec, e

	return rec
