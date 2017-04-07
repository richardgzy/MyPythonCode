'''
Created on Nov 16, 2016

@author: Richard's Surface
'''
name = input('Enter input file name:')
infile = open(name)

for line in infile:
    'Change line to lower case'
    line = line.lower()
    print(line)
infile.close()