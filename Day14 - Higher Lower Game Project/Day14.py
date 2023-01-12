from art import logo
from art import vs
from game_data import data
import random
import os

#print(logo)

# game_over = False
#
# compare_a = random.choice(data)
# compare_b = random.choice(data)
# compare_c = {}
#
#
# while not game_over:
#     for key in range(data):
#         print(f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']} ")
#         print("vs")
#         print(f"Compare B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']} ")
#         answer = input("Who has more followers? Type 'A' or 'B': ")
#         print(f" User Answer is {answer}")
#
#         if answer == 'A':
#             if compare_a['follower_count'] > compare_b['follower_count']:
#                 print(f"compare_a flowers is {compare_a['follower_count']}")
#                 print(f"compare_a flowers is {compare_b['follower_count']}")
#                 print("You win")
#                 compare_c = compare_a
#                 game_over = False
#             else:
#                 print("You Lose")
#                 game_over = True
#         else:
#             print("WTF")





# =========================================================


print(logo)

score = 0
account_b = random.choice(data)

#Make the game repeatable
game_over = False

while not game_over:

    #Generate a random account from the game data.
    #Making account at position B become the next account at position A
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)


    def format_data(account):
        """Format data into printable format and return the printable format"""
        account_name = account['name']
        account_description = account['description']
        account_country = account['country']
        return(f"{account_name}, a {account_description}, from {account_country} ")

    def check_answer(answer, a_followers, b_followers):
        """Take a user answer and follower counts and check, return if they got it right"""
        if a_followers > b_followers:
            return answer == 'a'
        else:
            return answer == 'b'

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    #Ask user for a guess
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    #Check if the user is correct
    ##Get follower count of each account
    a_folower_count = account_a['follower_count']
    b_folower_count = account_b['follower_count']

    # def check_answer(answer, a_followers, b_followers): call to check
    is_correct = check_answer(answer, a_folower_count, b_folower_count)

    os.system('clear')
    print(logo)

    #Give user feedback on their guess
    #Keep the score
    if is_correct == True:
        score += 1
        print("You're right!")

        game_over = False
    else:
        game_over = True
        print(f"Wrong!. Final score is {score}")


