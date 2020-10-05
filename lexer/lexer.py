#! /usr/bin/env python

import sys

KEYWORDS = [
	'say',
	'shout',
	'if',
	'for',
	'while'
]

OPERATORS = [
	'=',
	'+',
	'-',
	'*',
	'/',
	'^',
	'(',
	')',
]

if len(sys.argv) == 2:
	filename = sys.argv[1]

	f = open(filename, 'r')
	for line in f:
		if line[0] != '#' and line != '':
			print line
			chunks = line.split(' ')
			if chunks[0] == 'say':
				print 'say'
				the_string = ''
				start = False
				for character in line:
					if character == '\'' and not start:
						start = True
					elif start:
						if character != '\'':
							the_string += character
						else:
							break
				print the_string
			else:
				print 'Identifier ' + chunks[0]
				if chunks[1] == '=':
					print 'equals '
					if int(chunks[2]):
						print 'int ' + chunks[2]
		print '\n'
					
else:
	print "invalid args! use format: ./lexer.py <filename>"
