#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
x = abs(number)%10
if (x <6 ):
   print(" last digit of {} is ".format(number),x, "and is less than 6 and not 0" )
elif ( x == 0 ):
   print(" last digit of {} is".format(number),x, "and it is 0" )
else:
    print(" last digit of {} is".format(number),x, "and it is greater than 5")
