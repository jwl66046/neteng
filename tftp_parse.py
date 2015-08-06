#!/usr/bin/env python3

"""
This script was written to test CiscoConfParse functionality.  It is meant to be
run against a repository of configuration files, e.g. a TFTP server.  The script
will find a parent, and return it's child phrases as a dictionary data set.

In this example, I used my GNS3 lab, which has a TFTP server.   The script runs
in the TFTP directory, iterates through each of the files looking for the 
physical console (line con 0) settings, then returns each the results as an
ordered pair in a dictionary.

~John Lawrence
August 2015
"""


### necessary modules
import os
from ciscoconfparse import CiscoConfParse
import pprint


### Enter your TFTP server path here
tftp_path = '/var/lib/tftpboot/'


### record all files in the TFTP as inventory  -- this is for debugging purposes
inventory = []

for filename in os.listdir(tftp_path):
	inventory.append(filename)
		
print("\n\n This is here for debugging purposes:\n")   # This is for debugging purposes
pprint.pprint(inventory)

print("End Debugging for filename collection\n\n")

### Begin parsing through configurations

#create empty dictionary
testdict = {}

#work out of the TFTP server directory
os.chdir(tftp_path)

#look in each file for the parent
for filename in os.listdir(tftp_path):
	parse = CiscoConfParse(filename)
	line_con = parse.find_children("line con")   # this is the "parent" you are looking for
	testdict[filename] = line_con

pprint.pprint(testdict)
