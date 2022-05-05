from art import logo
from art import vs
from game_data import data
import random

print(logo)

#Pick a random item from the dictionary. Print the name, description and location. 
choice_a = random.choice(list(data))
# print(choice_a)
print(f"Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}")  
# Store follower count in a variable
followers_a = (choice_a['follower_count'])
print(f"Psst this person has {followers_a} followers")
                 
print(vs)

#Pick another random item from the dictionary. Print the name, description and location. 
choice_b = random.choice(list(data))
print(f"Compare B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}")  
followers_b = (choice_b['follower_count'])
print(f"Psst this person has {followers_b} followers")


#Ask the user who has more followers. Who has more followers? Type 'A' or 'B': 
guess = input("Who has more followers? Type 'A' or 'B': ")

#If user is correct, give a point and continue.


# If user is correct, compare the winner of the comparison to a new random person.

#The game continues until the user guesses wrong

#If the user is wrong, end the game. Sorry, that's wrong.  Final score: 1














# print(f"Sorry, that's wrong.  Final score: {}")
# print(f"You're right! Current score: {}")