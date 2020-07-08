
#! python3

###############################
#Regular Expressions
###############################

#these are similar to Ctrl+F commands in a browser, but can look for patterns
#not just specific strings

#non regular expression example
#look at how much we have to add if we want to check to see if something is a valid phone number

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range (0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range (4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range (8,12):
        if not text[i].isdecimal():
            return False
    return True

string = '415-555-1234'
print(isPhoneNumber(string))
string = '415-bana-1234'
print(isPhoneNumber(string))


message = 'Call me at 415-555-1234'
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone Number found!')
        foundNumber = True

if foundNumber == False:
    print('no number found')


#now lets do this with regular expressions
#Steps:
#Import re module
#create the string value you wish to search
#create the regex compile object
#use the search or findall functions to return values!

import re

message = 'Call me at 415-555-1234,  or 555-555-5555'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
match = phoneNumRegex.search(message)
print(match.group())

#NOTE: you usually pass raw strings to re.compile()

#this returns the first instance of this patter
#we can also use find all instead!
match = phoneNumRegex.findall(message)
print(match)

###############################
#GROUPS
###############################
#what if we wanted to get only the area code?
#we can use parantheses to divide the returned match into groups
#those groups can then be returned individually using match.group(#)

message = 'Call me at 415-555-1234,  or 555-555-5555'

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
match = phoneNumRegex.search(message)
print(match.group(1))
print(match.group(2))

#by using an escape character we can actually treat a parantheses as a character in
#our target string pattern

###############################
#Pipe Characters
###############################
message = 'I am the Batman and I drive a Batcopter, also Batbat'

batNumRegex = re.compile(r'Bat(man|copter|bat)')

#returns first instance of compound word: Batman
match = batNumRegex.search(message)
print(match.group())

#this only returns the suffixes: 
match = batNumRegex.findall(message)
print(match)

###############################
#Optional Portions  '?' and '*' syntax
###############################

#I want to search for a pattern that may or may not include something in the middle

message = 'I am the Batman and I drive a Batcopter, also Batwoman is cool, Batwowoman'
batNumRegex = re.compile(r'Bat(man|woman)')
match = batNumRegex.findall(message)
print(match)

#I can also do :
batNumRegex = re.compile(r'Bat(wo)?man')
match = batNumRegex.search(message)
print(match.group())

# the (wo)? means this middle string can occur or not occur bt will still be included

#can we apply this to the phone number one to make area code optional?

message = 'Call me at 415-555-1234,  or 555-555-5555'

phoneNumRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
match = phoneNumRegex.search(message)
print(match.group())
match = phoneNumRegex.findall(message)
print(match)

#using the * character instead of ?, we can search for any number of repetitions

message = 'I am the Batman and I drive a Batcopter, also Batwoman is cool, Batwowoman'
batNumRegex = re.compile(r'Bat(wo)*man')
match = batNumRegex.findall(message)
print(match)


###############################
#Required Portions  '+' syntax
###############################

#The + character instead of * or ? means that the portion must appear at least once

message = 'I am the Batman and I drive a Batcopter, also Batwoman is cool, Batwowoman'
batNumRegex = re.compile(r'Bat(wo)+man')
match = batNumRegex.findall(message)
print(match)

###############################
#Required Portions with exact # of repetitions  '{}' syntax
###############################

#Having a {#} after a (pattern) says only find instances where it occurrs # of times exactly

message = 'Ha HaHa HaHaHa HaHaHaHa'
HaRegex = re.compile(r'(Ha){3}')
match = HaRegex.findall(message)
print(match)


#you can also add another param to {} to set  a max value

message = 'Ha HaHa HaHaHa HaHaHaHa'
HaRegex = re.compile(r'(Ha){3,5}')
match = HaRegex.findall(message)
print(match)

#you can add a ? at the end of the {} to do a NON greedy match

#this one finds the will go to the max length on the first valid instance of 3 to 5 numbers
#GREEDY
message = '123456789'
numRegex = re.compile(r'(\d){3,5}')
match = numRegex.search(message)
print(match.group())

#This one will return the first valid options, which would be 3 numbers
#NON-GREEDY
numRegex = re.compile(r'(\d){3,5}?')
match = numRegex.search(message)
print(match.group())



###############################
# .findall()
###############################


message = 'Call me at 415-555-1234,  or 555-555-5555'

phoneNumRegex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
#only returns first instance
match = phoneNumRegex.search(message)
print(match.group())

#returns all instances but returned data types are a little different than normal
#groups can change how they items are returned
#see example below
match = phoneNumRegex.findall(message)
print(match)
# [('415-555-1234', '415', '555-1234'), ('555-555-5555', '555', '555-5555')]


###############################
#   Character Classes
###############################

#number
# \d
#anything BUT a number
# \D
#any letter, number, underscore
# \w
#anything BUT letter, number, underscore
# \W
#any space, tab, newline
#\s
#anything BUT space, tab, newline
#\S


lyrics = '12 drummers drumming, 11 pipers piping, 10 lords a leaping'

xmasRegex = re.compile(r'\d+\s\w+')
match = xmasRegex.findall(lyrics)
print(match)
# ['12 drummers', '11 pipers', '10 lords']

#create your own character class using []

#all lower case letters a to z
letterRegex = re.compile(r'[a-z]')

#all vowels
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('RoboCop eats baby food!'))

#all vowels that occur twice in a row
vowelRegex = re.compile(r'[aeiouAEIOU]{2}')
print(vowelRegex.findall('RoboCop eats baby food!'))

#we can also do the anything BUT our choices using '^'
#includes ALL other characters
vowelRegex = re.compile(r'[^aeiouAEIOU]{2}')
print(vowelRegex.findall('RoboCop eats baby food!'))


###############################
#   regex with begins and ends
###############################
#this returns a result
message = 'Hello there!'
beginsRegex = re.compile(r'^Hello')
print(beginsRegex.findall(message))
#['Hello']

#this does not
message = 'oh hello!'
beginsRegex = re.compile(r'^Hello')
print(beginsRegex.findall(message))
#[]


#Ends with uses $ instead of ^

#this does not
#this returns a result
message = 'Hello! there!'
endsRegex = re.compile(r'Hello!$')
print(endsRegex.findall(message))
#[]

#this returns a result
message = 'oh Hello!'
endsRegex = re.compile(r'Hello!$')
print(endsRegex.findall(message))
#['Hello!']


#can also do this with pattens and combine

message = '12oh Hello!34'
endsRegex = re.compile(r'^(\d)+(\w)+(\s)Hello!(\d)+$')
print(endsRegex.findall(message))
#[('2', 'h', ' ', '4')]



###############################
#   wildcards   '.'
###############################
message = 'cat bat flat'
atRegex = re.compile(r'.at')
print(atRegex.findall(message))
atRegex = re.compile(r'.{1,2}at')
print(atRegex.findall(message))


# '.*' means ALL characters
message = 'First Name: Bob Last Name: Smith'
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
print(nameRegex.findall(message))
#[('Bob', 'Smith')]

#Be aware of GREEDY vs NON-GREEDY
message = '<First Name: Bob> Last Name: Smith>'
nameRegex = re.compile(r'<(.*)>')
print(nameRegex.findall(message))
#['First Name: Bob> Last Name: Smith']
nameRegex = re.compile(r'<(.*?)>')
print(nameRegex.findall(message))
#['First Name: Bob']

#new lines '\n' are not included in .*
message = 'First Name: Bob\nLast Name: Smith'
nameRegex = re.compile(r'(.*)')
print(nameRegex.findall(message))
['First Name: Bob', '', 'Last Name: Smith', '']

#returns the full line
#include re.DOTALL in compile object
nameRegex = re.compile(r'(.*)', re.DOTALL)
print(nameRegex.findall(message))
#['First Name: Bob\nLast Name: Smith', '']

# there are other parameters you can use like:
# re.IGNORECASE to ignore the case sensitivity


###############################
#   sub()
###############################

#can also use sub() for only some pieces of the targets

message = 'Agent Alice shot Agent Bob'
namesRegex = re.compile(r'Agent (\w+)')
print(namesRegex.findall(message))
#['Agent Alice', 'Agent Bob']
print(namesRegex.sub('REDACTED', message))
#REDACTED shot REDACTED

namesRegex = re.compile(r'Agent (\w)\w*')
print(namesRegex.sub(r'Agent \1******', message))
#Agent A****** shot Agent B******


###############################
#   VERBOSE Reg expressions
###############################

#sometimes reg expressions can get really long
#we can use verbose mode to combat this
#this just means we use a multi line string and use comments to describe
#need to 


re.compile('\d\d\d-\d\d\d-\d\d\d\d')

#after verbose

verbosePhoneRegex = re.compile(r''' 
    \d\d\d      #area code
    -           #dash 1
    \d\d\d      #digits 4-6
    -           #dash 2
    \d\d\d\d    #digits 8-10
    ''', re.VERBOSE)   # need to include re.VERBOSE param

###############################
#   RegEx multiple params usage 
###############################

#separte options with | character in param 2
#only used in the 're' module

verbosePhoneRegex = re.compile(r''' 
    \d\d\d      #area code
    -           #dash 1
    \d\d\d      #digits 4-6
    -           #dash 2
    \d\d\d\d    #digits 8-10
    ''', re.VERBOSE | re.IGNORECASE | re.DOTALL)   # need to include re.VERBOSE param





