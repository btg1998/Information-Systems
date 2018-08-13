'''
A Python number guessing Program
'''
# Import for random numer generation and ceil function
import random
import math
import sys
#Variable intializations
low_limit=0
high_limit=10
attempts=[]
allowed_attempts=5
player_win=False
def check(a):
    if(not a.isalpha()):
        print("Name only contains Alphabets.")
        sys.exit(0)
fname=input("Enter your First Name: ")
check(fname)
lname=input("Enter your Last Name: ")
check(lname)
name=fname+" "+lname
print("Welcome "+name+" to the game.")
dict={"firstname":fname,"lastname":lname}
low_limit=int(input("Enter the lower limit:"))
high_limit=int(input("Enter the upper limit:"))
allowed_attempts=math.ceil((high_limit-low_limit)/3)
if (allowed_attempts<=0):
    print("Enter valid limits.")
    sys.exit(0)
print("You have {} attempts to guess the number.".format(allowed_attempts))
def get_the_guess(low_int,high_int):
    return input("I have guesed a number can you guess?")
#Function for validating guess and giving clues
def compare_numbers(target_int,guessed_int):
    if guessed_int < target_int:
        print("Oh it's a little higher!")
        return False
    elif guessed_int > target_int:
        print("You need to think of a lower number!")
        return False
    else:
        print("Wow, you got it!!")
        return True
random_int=random.randint(low_limit,high_limit)
attempts.append(int(get_the_guess(low_limit,high_limit)))
while len(attempts)<allowed_attempts:
    if compare_numbers(random_int,attempts[-1]):
        print("You made {} attempts to guess the number! You're guesses were: ".format(len(attempts)),attempts)
        print("Good Bye,",dict["firstname"],dict["lastname"],".")
        player_win=True
        break
    else:
        if allowed_attempts==attempts:
            break
        print("You are left with {} attempts".format(int(allowed_attempts-len(attempts))))
        attempts.append(int(get_the_guess(low_limit,high_limit)))
        continue
if player_win == False:
    print("Sorry, you've used all {} turns. I assumed {} Your guesses were: ".format(allowed_attempts,random_int),attempts)
    print("Good Bye,",dict["firstname"],dict["lastname"],".")
    
    
        
    
