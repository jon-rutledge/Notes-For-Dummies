#! python3
#Files and Folders

#File Attributes
#filename
#filepath
#file extension


import os

#create a valid folder path using os.path.join() for any OS
print(os.path.join('folder1','folder2','folder3', 'test.py'))

#get current working directory
print(os.getcwd())

#change working directory
#os.chdir()


#absolute and relative file paths

#/home/jonr/Desktop/Projects/ATBS/test.py# is an absolute file path

###############################
#   Pathway shortcuts
###############################


#imagine we are trying to access the following path, but our working directory is folder1
#   root/folder1/folder2/spam.png

#we can do
#   ./folder2/spam.png

#to go up into the directory of root we can do
#this gives us the parent directory of the current working dir
#   ../someotherthing.png

###############################
#   OS module functions
###############################


print(os.path.abspath('ListsAndStrings.py'))
print(os.path.dirname(os.path.abspath('ListsAndStrings.py')))

print(os.path.exists(os.path.abspath('ListsAndStrings.py')))
print(os.path.exists(os.path.abspath('banana.py')))

print(os.path.getsize('ListsAndStrings.py'))
print(os.listdir('./'))

if not (os.path.exists('./peanuts/cream')):
    os.makedirs('./peanuts/cream')


###############################
#   writing plain text files
###############################

#plaintext files are simple txt files as we know them

#other type is binary program (pretty much everything!)

if not (os.path.exists('./filetest')):
    os.makedirs('./filetest')

#when opening a file, make sure you are opening it with the right param
#open, append, write, read, etc
# this is handled by the second param

helloFile = open('./filetest/pytest.txt', 'w')
#print(helloFile.read())
#print(helloFile.readlines())

helloFile.write('its a bird!\n')
helloFile.write('its a plane!\n')
helloFile.write('No! its a  python test!!\n')
helloFile.close()

helloFile = open('./filetest/pytest.txt', 'r')
print(helloFile.read())
print(helloFile.readlines())

helloFile.close()


###############################
#   shelve module
###############################

#shelve objects are similar to a dictionary
#can store dictionaires to a file very easily to access them later

import shelve

shelfFile = shelve.open('./filetest/mydata')
shelfFile['dogs'] = ['Buster', 'Phoenix', 'Taco']
shelfFile.close()

#i have saved this key and values to a file in the directory specified
#we can reaccess them with this

shelfFile = shelve.open('./filetest/mydata')
print(shelfFile['dogs'])
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()

###############################
#   copying and moving files
###############################

import shutil

if not (os.path.exists('./filetest/folder1')):
    os.makedirs('./filetest/folder1')

#copy the file to a directory
shutil.copy('./filetest/pytest.txt', './filetest/folder1')
#copy and rename it
shutil.copy('./filetest/pytest.txt', './filetest/folder1/pytestEXTRA.txt')

#copy directory to another and rename it!
#useful for taking backups

if not (os.path.exists('./filetest/folder1-Copy')):
    shutil.copytree('./filetest/folder1', './filetest/folder1-Copy')

#move file
#shutil.move('./filetest/pytest.txt', './filetest/folder1-Copy/MEGATEST.txt')

#name a file
shutil.move('./filetest/pytest.txt', './filetest/pytest-renamed.txt')

###############################
#   deleting files
###############################

#import os
#import shutil

#delete single file
os.unlink('./filetest/pytest-renamed.txt')

#delete an EMPTY directory
#os.rmdir('./filetest/pytest.txt')

#check a directory for files before deletion

for filename in os.listdir('./filetest/folder1-Copy'):
    print(filename)

#delete a popualted directory
shutil.rmtree('./filetest/folder1-Copy')

###############################
#   walking directory tree
###############################

#import os

for folderName, subfolders, fileNames in os.walk('./'):
    print('Folder: ' + folderName)
    print(subfolders)
    print(fileNames)
    





