'''
A Python number guessing Program
'''
# Import for random numer generation and ceil function
import random
import math
#Variable intializations
guess_counter=0
low_limit=0
high_limit=10
attempts=0
allowed_attempts=5
player_win=False
low_limit=int(input("Enter the lower limit:"))
high_limit=int(input("Enter the upper limit:"))
allowed_attempts=math.ceil((high_limit-low_limit)/3)
def get_the_guess(low_int,high_int):
    return input("I have guesed a number can you guess?")

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
guess=get_the_guess(low_limit,high_limit)
while attempts<allowed_attempts:
    attempts+=1
    if compare_numbers(random_int,int(guess)):
        print("You made {} attempts to guess the number!".format(attempts))
        player_win=True
        break
    else:
        if allowed_attempts==attempts:
            break
        print("You are left with {} attempts".format(int(allowed_attempts-attempts)))
        guess=input("Try Again!")
        continue
if player_win == False:
    print("Sorry, you've used all {} turns. I assumed {}".format(int(allowed_attempts),random_int))
    
    
        
    
