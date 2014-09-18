#!/usr/bin/env python

#Filters passwords.txt to match snapchat password requirments puts the output in parsed.txt

f = open("passwords.txt","r")
p = open("parsed.txt", "w")
for l in f:
	if (l.lower()!=l and l.upper()!=l):
		p.write(l)
		print(l)
	
