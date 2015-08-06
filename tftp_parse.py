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

######################
### install necessary modules
######################

import os
from ciscoconfparse import CiscoConfParse
import pprint

# Enter your TFTP server path here
tftp_path = '/var/lib/tftpboot/'


#######################
### Begin parsing through configurations
#######################

#create empty dictionary
testdict = {}

#change working directory to TFTP server location
os.chdir(tftp_path)

#look in each file for the parent's stanza text
for filename in os.listdir(tftp_path):
	parse = CiscoConfParse(filename)
	line_con = parse.find_children("line con 0")   # this is the "parent" text you are looking for
	testdict[filename] = line_con

pprint.pprint(testdict)
