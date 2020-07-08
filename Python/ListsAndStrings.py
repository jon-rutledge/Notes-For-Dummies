#strings and lists

testList = list('Hello')
print(testList)
print(testList)

#strings are immutable data types, they cannot be modified
#if you need to modify a string value, you need to create a new string based the original

#References
#with one off variables you can do something like this

spam =  42
cheese = spam
spam = 100
print(cheese)

#cheese retains the value of 42 as it is not a reference to 'spam' but 
#instead its own variable and value

#with lists this does not work

spam = [0,1,2,3,4,5]
cheese = spam
cheese[1] = 'TEST'
print(cheese)
print(spam)

#spam also changes because the REFERENCES to the list is in both spam and cheese
#think of you assigning an set of addresses to spam and cheese
#by changing the value of something in the list, the addresses stay the same

#import Copy
#by using the copy module we can actually truly copy a list and act on it
#without modifiying the original list

import copy

spam = [1,2,3,4]

cheese = copy.deepcopy(spam)
cheese.append('TEST')
print(cheese)
print(spam)

#lists can also exist on multiple lines

spam = [1,
        2,
        3]


#also can conitnue on new lines by using \

print('This is line 1 and ' + \
'this is line 2')


