from art import logo, vs
from game_data import data
import random



def get_random_account():
  """Get data from random account"""
  return random.choice(data)

def format_data(account):
    """Takes the account data and returns the printable format"""
    name = account["name"]
    descr = account["description"]
    country = account["country"]
    return(f"{name}, a {descr},  from {country}")

def check_answer(guess, followers_a, followers_b):
    """Takes the users guess and the follower counts and returns if they got it right"""
    #If account_a has more followers and user guessed "a " return followers
    if followers_a > followers_b:
        return guess == "a"
    # If account_b has more followers and user guessed "b " return followers
    else:
        return guess == "b"


def game():
    #display logo
    print(logo)
    
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()
    
    
    #Make the game repeatable
    while game_should_continue: 
        #Generate a random account from the game data
        account_a = account_b
        account_b = get_random_account()
        
        
        while account_a == account_b:
            account_b = get_random_account()
        
        print(f"Compare A: {format_data(account_a)} ")
        print(vs)
        print(f"Against B: {format_data(account_b)} ")
        
        #Ask the user to guess who has more followers
        guess = input('Who has more followers? Type "A" or "B": ').lower()
    
        #Get the follower count for each account. 
        followers_a = (account_a["follower_count"])
        followers_b = (account_b["follower_count"])
        print(f"A: {followers_a} B: {followers_b}")
        is_correct = check_answer(guess, followers_a, followers_b)
    
        print(logo)
                                                                                                                              
        #Give user feedback on their guess.
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else: 
            game_should_continue = False
            print(f"Sorry, that's wrong.  Final score: {score}")
        
game()