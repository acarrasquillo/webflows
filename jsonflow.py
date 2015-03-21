from silk import *


####
#	Convert a Flowv5 record to silk record
#	
#	http://www.cisco.com/c/en/us/td/docs/net_mgmt/netflow_collection_engine/3-6/user/guide/format.html#wp1006186
#	
#
#	rwpdu2silk --xargs=/home/abimael/netflow2silk/files.txt --silk-output=/home/abimael/netflow2silk/silkflow4 --print-statistics --log-destination=/home/abimael/netflow2silk/logs/rwpdu2silk_log --log-flags=all
#
#
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

###########################################################
#	function: fRecTosRec(**kwargs)
#	
#	recieves: **kwargs NetFlow v5 dictionary with NetFlow v5 key fields and their values
#	
#	returns: A silkRWRec from the NetFlow v5 dictionary
#
###########################################################
def fRecTosRec(**kwargs):

	# dict to construct a silk.RWRec from the NetFlow v5 dict
	rec = dict()

	if 'srcaddr' in kwargs:
		rec['sip'] = silk.IPAddr(kwargs['srcaddr'])

	if 'dstaddr' in kwargs:
		rec['dip'] = silk.IPAddr(kwargs['dstaddr'])

	if 'nexthop' in kwargs:
		rec['nhip'] = silk.IPAddr(kwargs['nexthop'])

	if 'input' in kwargs:
		rec['input'] = kwargs['input']

	if 'output' in kwargs:
		rec['output'] = kwargs['output']

	if 'dpkts' in kwargs:
		rec['packets'] = kwargs['output']

	if 'dpctets' in kwargs:
		rec['bytes'] = kwargs['dOctets']

	if 'first' in kwargs:
		rec['stime'] = kwargs['first']

	if 'last' in kwargs:
		rec['etime'] = kwargs['last']

	if 'srcport' in kwargs:
		rec['sport'] = kwargs['srcport']

	if 'dstport' in kwargs:
		rec['dport'] = kwargs['dstport']

	if 'tcp_flags' in kwargs:
		rec['tcp_flags'] = silk.TCPFlags(kwargs['tcp_flags'])

	if 'prot' in kwargs:
		rec['protocol'] = kwargs['prot']

	try:
		rec = silk.RWRec(rec)
	except Exception, e:
		raise "Error constructing Netflow v5 to RWRec: \n\t %s \n" % rec, e

	return rec