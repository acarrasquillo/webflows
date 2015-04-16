#! /usr/bin/python

# Import the PySiLK bindigs
from silk import *

# Import the sys command line arguments
import sys

# Import the JSON Silk library
import jsonsilk

# Main function
def main():

	if len(sys.argv) != 3 :
		print ("Usage: %s infile outset" % sys.arg[0])
		sys.exit(1)

	# open an solk file for reading
	infile = silkfile_open(sys.argv[1], READ)

	# Create an empty IPset
	destset = IPSet()

	# Loop over records in the file
	for rec in infile:

		# Do comparisons based on rwrec field value
		#if (rec.protocol == 6 and rec.sport in [22,8080] and rec.packets > 3 and rec.bytes > 120):

			# Add the dest IP of the record to the IPset
		
		try:
		 	print "\n------RECORD------\n"
		 	print rec.classtype
		 	jsonRec = jsonsilk.dumps(rec)
		 	print jsonRec
		 	print "\n------DICTIONARY------\n"
		 	recDict = jsonsilk.loads(jsonRec)
		 	print recDict
		 	print "\n------silk-RWREC------\n"
		 	rec2 = RWRec(recDict)
		 	print rec2
		except Exception, e:
		 	print (e, rec.as_dict()) 
		# print "------------STRING------------\n"
		# print str(rec)

		# print "\n------------DICTIONARY------------\n"
		# print rec.as_dict()

	# Save the IPset for future use
	try:
		destset.save(sys.argv[2])
	except Exception, e:
		sys.exit("Unable to write to %s \n Exception('%s')" % (sys.argv[2],e))

	#count the items in the set
	count = 0
	for addr in destset:
		count = count + 1

	print ("%d addresses" % count)

	# Another way to do the same
	print ("%d addresses" % len(destset))

	# Print the ip blocks in the set
	for base_prefix in destset.cidr_iter():
		print("%s/%d" % base_prefix)

# Call the main() function when this program is started
if __name__ == '__main__':
	main()