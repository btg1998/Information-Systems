'''
A Python number guessing Program
'''
import random
import math
import sys
low_limit=0
high_limit=10
attempts=[]
allowed_attempts=5
player_win=False
fname=None
try:
    fname=input("Enter your First Name: ")
    if not fname:
        fname = None
        raise Exception("-_-")
    if not fname.isalpha():
        raise ValueError("First name should contain alphabets only.")
except ValueError as err1:
    print(err1)
except ValueError as err2:
    print(err2)
lname=None
try:
    lname=input("Enter your Last Name: ")
    if not lname:
        lname = None
        raise Exception("-_-")
    if not lname.isalpha():
        raise ValueError("Last name should contain alphabets only.")
except ValueError as err1:
    print(err1)
except ValueError as err2:
    print(err2)
name=fname+" "+lname
print("Welcome "+name+" to the game.")
dict={"firstname":fname,"lastname":lname}        
try:
    low_limit=int(input("Enter the lower limit:"))
    break
except ValueError:
    print("Oops!  That was no valid number.  Try again...")
try:
    high_limit=int(input("Enter the upper limit:"))
    break
except ValueError:
    print("Oops!  That was no valid number.  Try again...")
allowed_attempts=math.ceil((high_limit-low_limit)/3)
if (allowed_attempts<=0):
    print("Enter valid limits.")
    sys.exit(0)
print("You have {} attempts to guess the number.".format(allowed_attempts))
def get_the_guess(low_int,high_int):
    return input("I have guesed a number can you guess?")
def compare_numbers(target_int,guessed_int):
    try: 
        if guessed_int < target_int:
            print("Oh it's a little higher!")
            return False
        elif guessed_int > target_int:
            print("You need to think of a lower number!")
            return False
        else:
            print("Wow, you got it!!")
            return True
    except:
        print("No, it is a fraction or not a number.")
        return False
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
    
    
        
    
