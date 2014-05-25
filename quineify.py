import sys
import fileinput
import os.path
import pdb

def process_char(ch):
	if ch == '<': return '&lt'
	if ch == '>': return '&gt'
	if ch == '\n': return '\\n'
	if ch == '\t': return '\\t'
	return ch

def process_line(line):
	processed_line = ""
	for ch in line:
		processed_line += process_char(ch)
	return processed_line

def whole_file_processed():
	whole_file = ""
	for line in open("src.html", "r"):
		whole_file += process_line(line)
	return whole_file

def insert_quine(line):
	i = line.index(';')
	return line[0:i] + "\"" + whole_file_processed() + "\"" + line[i:]

def is_quine_line(line):
	return "file = ;" in line

def make_quine():
	quine = ""
	for line in open("src.html", "r"):
		if is_quine_line(line):
			quine += insert_quine(line)
		else:
			quine += line
	return quine

outfile = open("index.html", "w")
outfile.write(make_quine())
