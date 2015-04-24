#!/usr/bin/env python
import cgi,os,sys,json
import cgitb; cgitb.enable()  # for troubleshooting

print "Content-type: text/html"
print
length = os.environ["CONTENT_LENGTH"] 
data =  sys.stdin.read(int(length))
print data