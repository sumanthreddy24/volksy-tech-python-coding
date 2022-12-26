#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
x =number%10
if ( x == 0 ):
   print( " last digit of {} is".format(number),x, " and it is 0" )
elif ( number < 0 and x < 6 ):
   x = x-10
   print(" last digit of {} is ".format(number),x, "and is less than 6 and not 0" )
else:
    print(" last digit of {} is".format(number),x, "and it is greater than 5")
