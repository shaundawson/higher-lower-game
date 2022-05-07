from art import logo
from art import vs
from game_data import data
import random

score = int(0)

def map_guess(followers_a, followers_b, guess):
    if guess == "a" and followers_a > followers_b:
        print("winner winner chicken dinner")
        return score + 1
    elif guess == "b" and followers_b > followers_a:
        print("winner winner chicken dinner")
        return score + 1
    elif guess == followers_a and guess == followers_b:
        print("it's a tie")
    else: 
        print("Sorry you lose.")
        return
  

def game():
 
    print(logo)

    choice_a = random.choice(list(data))
    print(f"Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}")  
    # Store follower count in a variable
    followers_a = (choice_a['follower_count'])
    print(f"Psst this person has {followers_a} followers")

    print(vs)

    #Pick another random item from the dictionary. Print the name, description and location. 
    choice_b = random.choice(list(data))
    print(f"Against B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}")  
    followers_b = (choice_b['follower_count'])
    
    print(f"Psst this person has {followers_b} followers")

    lower = min(followers_a, followers_b)

    guess = input('Who has more followers? Type "a" or "b": ')
   

       
game()