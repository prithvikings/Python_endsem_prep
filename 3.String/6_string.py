#STRING

"""A string is a collection of one or more character put in a
single quote,double-quote or triple quote"""
"""multi-line string can be denoted using triple quoted"""


s="This is a string"
print(s,type(s))

s='''A multiline string'''
print(s,type(s))

s='''
hello
worlds'''
print(s,type(s))

s='10'
print(s,type(s))#this will be string because 10 has single quotation marks