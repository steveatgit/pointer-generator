#!/usr/bin/python

import sys
import os

dec_in = "decoded"
ref_in = "reference"
file_out = "out.txt"
fp_out = open(file_out, 'w')

dec_files = os.listdir(dec_in)
dec_files.sort()
ref_files = os.listdir(ref_in)
ref_files.sort()

dec_list = []
for dec_file in dec_files:
	with open(os.path.join(dec_in, dec_file), 'r') as fp:
		line = fp.readline()
		dec_list.append(line)

ref_list = []
for ref_file in ref_files:
	with open(os.path.join(ref_in, ref_file), 'r') as fp:
		line = fp.readline()
		ref_list.append(line)

art_list = open('test_art', 'r').readlines() 

for idx, dec in enumerate(dec_list):
	fp_out.write("###### abstract: {}".format(art_list[idx]))
	fp_out.write("reference query: {}\n".format(ref_list[idx]))
	fp_out.write("generate  query: {}\n\n".format(dec))
fp_out.close()
		


