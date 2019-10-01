#!/bin/python

def remove_empty_lines():
	infile = input("Name of file with spaces: ")
	outfile = input("Name of file to output (needs to exists) ")

	filename = open(str(infile), "r")
	lines = filename.readlines()	
	for x in lines:
		if x.rstrip():
			file=open(outfile,"a")
			file.write(x)

def remove_lines_and_text():
	infile = input("Name of file with spaces: ")
	outfile = input("Name of file to output (needs to exists) ")
	todelete = input("What words need to be deleted?")

	delete_list = [todelete] #create a list of the strings to remove
	fin = open(infile)
	fout = open(outfile, "w+")
	for line in fin:
	    for word in delete_list:
	        line = line.replace(word, "")
	    fout.write(line)
	fin.close()
	fout.close()


just_spaces = input("Do you want to just remove empty lines? ")


if just_spaces == "yes" or just_spaces == "y":
	remove_empty_lines()

else:
	print("Ok will also remove un-needed text.")
	remove_lines_and_text()

