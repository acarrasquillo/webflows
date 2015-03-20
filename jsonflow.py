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
Bytes 	Contents 	Description

0-3 	srcaddr 	Source IP address

4-7 	dstaddr 	Destination IP address

8-11 	nexthop 	IP address of next hop router

12-13	input 		SNMP index of input interface

14-15 	output 		SNMP index of output interface

16-19 	dPkts 		Packets in the flow

20-23 	dOctets 	Total number of Layer 3 bytes in the packets of the flow

24-27 	First 		SysUptime at start of flow

28-31 	Last 		SysUptime at the time the last packet of the flow was received

32-33 	srcport 	TCP/UDP source port number or equivalent

34-35 	dstport 	TCP/UDP destination port number or equivalent

36 		pad1 		Unused (zero) bytes

37 		tcp_flags 	Cumulative OR of TCP flags

38 		prot 		IP protocol type (for example, TCP = 6; UDP = 17)

39 		tos 		IP type of service (ToS)

40-41 	src_as 		Autonomous system number of the source, either origin or peer

42-43 	dst_as 		Autonomous system number of the destination, either origin or peer

44 		src_mask 	Source address prefix mask bits

45 		dst_mask 	Destination address prefix mask bits

46-47 	pad2 		Unused (zero) bytes
"""

