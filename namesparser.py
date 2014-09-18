#!/usr/bin/env python

import os
import sys
import re
#Reads names from users.csv and outputs them to users.txt

i = open("users.csv","r")
o = open("users.txt","w")

for l in i:
	match = re.search(r',"(.+)",',l)
	print(match.group(1))
	o.write(match.group(1)+"\n")

