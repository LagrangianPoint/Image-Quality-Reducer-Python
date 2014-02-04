#!/usr/bin/python

import os
import sys
import Image

if len(sys.argv) < 2:
	print "[ERROR] Missing arguments. Usage:"
	print "\tpython img-reduce-quality.py image1.jpg image2.jpg"
	sys.exit(1)

print " * * Script for reducing an image's quality * * "
nQuality = int(raw_input('What quality do you want for your images? [0-100] : '))

for strFile in sys.argv[1:]:
	strBase, strExt = os.path.splitext(strFile)
	strOutFile = strBase + '_small_' +  str(nQuality) + strExt
	Image.open(strFile).save(strOutFile, 'JPEG', quality=nQuality)
	nReduction = (1.0-(os.stat(strOutFile).st_size / float(os.stat(strFile).st_size))) * 100
	print "%s >>> %s  (%.2f%% reduction)" % (os.path.split(strFile)[1], os.path.split(strOutFile)[1], nReduction )

raw_input("Press enter to exit.")
