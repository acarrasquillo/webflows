---
author:
- |
    Abimael Carrasquillo-Ayala\
    `abimael.carrasquillo@gmail.com`\
    **advisor**\
    José Ortiz-Ubarri\
    `cheo@hpcf.upr.edu`\
    University of Puerto Rico, Río Piedras\
    School of Natural Sciences\
    Department of Computer Science\
    Computer Security Lab (CSLab)
date: |
    **CCOM 4995 | Spring 2015**\
    Undergraduate Research\
title: |
    **WebFlows**\
    Interface to filter Network Flows
...

Network flow data (or network flow) is a generalization of NetFlow.
NetFlow^^ is a traffic-summarizing format that was first implemented by
Cisco System^^ Network flow data is collected to support several
different types of analyses of network traffic. WebFlows is a web based
application that allows to query network flow data, where the results
are provided in JSON format. This will allow to utilize open source
data-visualization libraries for network flow data anlysis.

Introduction
============

System for Internet Level Knowledge (or SiLK) tool suite is a highly
scalable flow-data capture and analysis system developed by the Network
Situational Awareness group (NetSA) at Carnegie Mellon University`'`s
Software Engineering Institute(SEI). SiLK tools provide network security
analysts the ability to understand, query, and summarize both recent and
historical traffic data represented as network flow records.

What is network flow data
-------------------------

Network flow collection differs from direct packet capture, in that it
builds a summary of communication between sources and destinations on a
network. For NetFlow, this summary covers seven relevant keys: *source*
and *destination* IP addresses, *source* and *destination* ports, the
*Transport-layer protocol*, the type of *service* and *interface*. SiLK
utilizes five of this keys, the *Transport-layer protocol* with the
*source* and *destination* IP addresses and ports.

### What information provides network flow data

Why is network flow data captured and analyzed? , Well here are some of
the questions that network flow data analysis can answer.

-   What is on the network?

-   What happened before an event?

-   Where are the policy violations occurring?

-   Which are the most popular web servers?

-   Do my users browse known infected web servers?

-   Do I have a spammer on my network?

-   When did my web server stop responding to queries?

-   Is my organization routing undesired traffic?

-   Who uses my public Domain Name System (DNS) server?

Network flow data offers a deep understanding of whats happening over
your network. This facilitate the process of solving problems in a
network. Thas why it’s usefull to utilize a system like SilLK over a
large network infrastructure.

SiLK tool suite {#sec:silktoolsuite}
---------------

eThe SiLK analysis suite consist of over 60 command-line UNIX tools
(including flow collection tools) that rapidly process flow records or
manipulate additional data. Two of the basic commands are *rwfilter*
that is the most commonly used SiLK command and serve as a starting
point for most analyses. It both retrieves data and partitions data to
isolate flow records of interest, Figure \[fig:rwfilter\] shows an
example. The command *rwcut* reads Silk Flow data and display it as
text. Like this two commands there are others that can be combined to do
Silk Flow data analysis, the tool suite utilizes the command line *pipe*
that allows to pass to one command the output of another command, for
example the next bash snippet shows how to use the *pipe* to pass
`command#2` the result of `command#1`:

    $ command#1 | command#2


### PySiLK

PySiLK is an extension to the SiLK tool suite that allows additional
functionality expressed via scripts written in the Python programming
language. The purpose is to support analytical use cases that are
difficult to express, implement, and support with the capabilities built
into SiLK. This project utilizes PySiLK to read and filter netflow data
and provide the results on JSON format.

Problem
=======

It’s needed to provide netflow data in a format that will allow to use
open source visualization libraries. As said on section
\[sec:silktoolsuite\]. The commands of the SiLK tool suite output
results on text format. This complicates the process of utilizing
visualizations libraries that recieve as input a different data format.

Methodology
===========

It would be good to have the data in a format that would be easy to
process and analyze. For this we implemented:

1.  A functions library to convert SiLK records to JSON format.

2.  A web interface that will allow to query the flows data and provide
    the results on JSON format.

WebFlows is a web application that runs utilizing a CGI server, the web
interface (Figure \[fig:interface\]) allows to construct a query by
providing values and logic between all the fields of a SiLK record. The
user can select cero or more fields to match and filter the netflow
data, see Figure \[fig:queryint\]. The output format is provided on JSON
format, this will allow to combine open-source visualization libraries
that use as input JSON data. This is the third step of this methodology,
to provide data visualization on the web interface.

Code example
------------

The process of filtering SiLK records, utilizing the WebFLows interface
consist of building the query utilizing the provided form and submiting
the query to return all the records that match the query parameters. The
next *Python* snippet shows part of the code that recieves the query
parameters and verifies if the saved SiLK records match the query.\
`excecute.cgi`: Line 20 - 26

    20 recordList = list()
    21 for filename in FGlob(type="all",
                            start_date="2015/03/09", 
                            site_config_file="silk.conf", 
                            data_rootdir="/rwflowpack/"):
                            
    22     for rec in silkfile_open(filename, READ):

               # if the record pass the query parameters
               
    23         if jsonsilk.checkRec(rec,query) == True:

                     #convert the record to valid json serialisable dic
                     
    24             serRec = jsonsilk.serializableRecord(rec.as_dict())

                     #add the record to the list
                     
    25              recordList.append(serRec)

    26 jsonlist = json.dumps(recordList)

-   **Line \#20:** Creates a list to store the results.

-   **Line \#21:** Uses the PySiLK *FGlob()* routine to iterate over all
    the files on the SiLK repository containing netflow data.

-   **Line \#22:** On each file open, iterate over each SiLK record on
    the file.

-   **Line \#23:** Checks if the given SiLK record match the
    query recieved.

-   **Line \#24:** If the SiLK record match the query, it is modified to
    support JSON format conversion.

-   **Line \#25:** The SiLK record that supports JSON format conversion
    is added to the list containing the results.

-   **Line \#26:** Converts the result list in a JSON containing all
    the results.

Future work
===========

With the job already done, there are less tasks needed to complete the
project. The next steps are:

-   Combine, data visualization with the interface.

-   Integrate WebFlows with the CSLab TOA project.

-   Provide the funtionality to construct complex queries that require
    more logic betwen the SiLK records fields.

Conclusion
==========

WebFlows provides the functionality of filtering flow data utilizing a
web interface to construct a query. The output format is JSON, that
allows to use open source visualization libraries that recieve as input
JSON data. In comparision to the SiLK command line tools that output
results in text format, this will facilitate flow data analysis and
extend the posibilities of data visualization.

Acknowledgement
===============

This work is supported by the scholarship Academics and Training for the
Advancement of Cybersecurity Knowledge in Puerto Rico (ATACK-PR)
suported by the National Science Foundation under Grant No. DUE-1438838.

References
===============

<span>widestlabel</span> Ron Bandes, Timothy Shimeall, Matt Heckathorn,
Sidney Faber (2014). *Using SiLK for Network Traffic Analysis*\
*source:* `http://tools.netsa.cert.org/silk/analysis-handbook.pdf`

Google inc.*AngularJS API Docs*\
*source:* `https://docs.angularjs.org/api`

