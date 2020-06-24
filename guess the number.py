# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 18:51:17 2019

@author: vamshi
"""
import random
randomNumber = random.randrange(0,100)
print("Random number has been generated")
guessed = False
while guessed==False:
    userInput = int(input("Your guess pleas: "))
    if userInput==randomNumber:
        guessed = True
        print("Well done!")
    elif userInput>100:
        print("Our guess range is between 0 and 100, please try a bit lower")
    elif userInput<0:
        print("Our guess range is between 0 and 100, please try a bit higher")
    elif userInput>randomNumber:
        print("Try one more time, a bit lower")
    elif userInput < randomNumber:
        print("Try one more time, a bit higher")

print("End of program")