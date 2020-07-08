##############################
# Raise
##############################

#raise Exception('This is an Error!')
# Traceback (most recent call last):
#   File "Errors.py", line 5, in <module>
#     raise Exception('This is an Error!')
# Exception: This is an Error!


##############################
# Try and Except
##############################

#allows you to try something and catch and error to prevent the program from stopping
#Can also use traceback module to write to an error log if needed

import traceback
try:
    raise Exception('Boom')
except:
    print('ya goof!')
    errorFile = open('error_log.txt', 'a')
    errorFile.write(traceback.format_exc())

#ya goof!


##############################
# Assert
##############################

# asserts can be set up to crash the program if its condition is False

def AssertTest(val=True):
    if val:
        print('Val is True!')
        return True
    assert False, 'Val is set to False!'

AssertTest()
#AssertTest(val = False)

# Val is True!
# Traceback (most recent call last):
#   File "Errors.py", line 24, in <module>
#     AssertTest(val = False)
#   File "Errors.py", line 21, in AssertTest
#     assert False, 'Val is set to False!'
# AssertionError: Val is set to False!


##############################
# Logging
##############################

# We can use the LOGGING module to track our code through its run time
# Logging is better than print because we can turn it off without modifying the code!
# See below

import logging

#start with this
#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

#can write this to a file by using this instead:
logging.basicConfig(filename = 'Log.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')



#this turns off the debugging below critical, comment it out and run again to see logging
#logging.disable(logging.CRITICAL)

#this turns on only info and above
logging.disable(logging.DEBUG)

logging.debug('Start here')
def factorialTest(num):
    val = 1
    logging.debug('loop starts')
    for i in range(num):
        val = val * (i+1)
        logging.info('i == %s, total == %s' % (i, val))
    return val
print(factorialTest(7))

#Levels of debugging:
#debug (lowest)
#info
#warning
#error
#critical (highest)

#can use different logging.error() logging.debug() etc functions to write functions at different levels








