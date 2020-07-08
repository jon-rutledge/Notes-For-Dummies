#Dictionary data types

myDict = {
    #key value pairs, size = key and fat = value
    'size' : 'fat',
    'color' : 'red',
    1234: 'number'
}

print(myDict['color'])
print(myDict[1234])

print(myDict)

#dictionaries have no order!

myOtherDict = {
    #key value pairs, size = key and fat = value
    1234: 'number',
    'color' : 'red',
    'size' : 'fat'
}

print(myDict == myOtherDict)

#Can check if a key is in a dict using 'in'
print(1234 in myDict)


#can use the dictionaries like these below:

print(list(myDict.keys()))

for k in myDict.keys():
    print(k)

for v in myDict.values():
    print(v)

for k, v in myDict.items():
    print(str(k) + ': ' + str(v))

print(myOtherDict.get('color', 'No color key found'))
print(myOtherDict.get('fruit', 'No fruit key found'))

#set Default is a good way to always make sure there is a key pair in your dictionary
def countCharacters(input):
    import pprint
    count = {}
    for char in input:
        count.setdefault(char, 0)
        count[char] = count[char] + 1
    pprint.pprint(count)
    #return(count)

countCharacters('I am the largest banana in the world!')