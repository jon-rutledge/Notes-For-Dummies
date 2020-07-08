#! python3
#Methods

#functions specific to an data type
#the following examples are LIST type methods

#Example: .index(val)  
spamList = ['hello' , 'hi', 'howdy', 'hi']
print(str(spamList.index('hi')))

#Example: .append(val)
spamList.append('appended')
print(spamList)

#Example: .insert(pos, val)
spamList.insert(1, 'inserted')
print(spamList)

#example: .remove(val)
spamList.append('howdy')
spamList.append('howdy')
spamList.remove('howdy')
print(spamList)

#Example:  .sort()
#sorted values must all be same datatype
#ASCII-betical order
spamList.sort()
print(spamList)
spamList.sort(reverse = True)
print(spamList)

#to sort by true alphabetical order
spamList.sort(key=str.lower)
