#Advanced Strings

#escape characters
#example how do we handle a single qoute inside of the string?
string = "This is Jon's dog"  #use double quotes
string = 'This is Jon\'s dog'  #use escape backslash character quotes
print(string)

#raw strings
#ignore escape characters
rawstring = r'This is a raw string'
rawstring = r'This is Jon\'s dog'
print(rawstring)

#triple quotes (single or double)
#can allow multiline string
string = """
            Dear Friendo,
                This is a multi line string.
                Check em 
        """

string = '''
            Dear Friendo,
                This is a multi line string.
                Check em 
        '''
        
print(string)



#String Methods
#lower and upper case methods
string = 'BaNaNa'
string = string.lower()
print(string)

string = string.upper()
print(string)


#multiple method calls
string = 'BaNaNa'
print(string.lower().isupper())

#isalpha() - letters only?
#isalnum() - letters and numbers only?
#isdecimal() - numbers only?
#isspace() - whitespace only?
#istitle() - title case only?  upper case on first letter of each word but then lower case for rest


#join method

stringlist = ['boom', 'crash', 'banana']
print(', '.join(stringlist))


#split method
string = 'My name is jon, yo'
print(string.split())
print(string.split(','))

#right and left jsutify
#rjust and ljust
string = 'My name is jon, yo'
print(string.rjust(30))
print(string.rjust(30, '-'))
print(string.center(30, '-'))


#strip methods
string = string.rjust(30)
print(string)
print(string.strip())

#we can also pass a set of letters to be stripped from left and right side
#note they do not have to be in order
string = 'SpamSpamBananaSpamBaconSpamSpam'
print(string.strip('aSpm'))

#replace is a useful function as well.  see any of my other projects for replace
print(string.replace('Spam', 'Z'))

#using PYPERCLIP module
#can copy and paste from computer clipboard
#pip install pyperclip

#useful for copying from script and then can paste to notepad


#import pyperclip
#pyperclip.copY('copied text')
#pyperclip.paste()


#insert values into a string
val1 = 'one'
val2 = 2
string  = 'Value 1: %s\nValue 2:  %i' % (val1, val2) 
print(string)