# # {Key: Value}
#
# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
#     "Loop": "The action of doing something over and over again."
# }
#
# print(programming_dictionary["Bug"])
#
# #Adding new items to dictionary
# programming_dictionary["Loop2"] = "Loop 2 added"
#
# #Empty dictionary
# empty_dectionary = {}
#
# #Wipe existing dictionary
# #programming_dictionary = {}
#
# #Edit an item in a dictionary
# programming_dictionary["Bug"] = "New edited entry"
# print(programming_dictionary)
#
# #Loop through a dictionary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])
#
#

#
# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }
# # 🚨 Don't change the code above 👆
#
# # TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}
#
# # TODO-2: Write your code below to add the grades to student_grades.👇
# for key in student_scores:
#     if student_scores[key] <= 70:
#         student_grades[key] = "Fail"
#     elif student_scores[key] >= 71 and student_scores[key] <= 80:
#         student_grades[key] = "Acceptable"
#     elif student_scores[key] >= 81 and student_scores[key] <= 90:
#         student_grades[key] = "Exceeds Expectations"
#     elif student_scores[key] >= 91 and student_scores[key] <= 100:
#         student_grades[key] = "Outstanding"
# print(student_scores)
#
# # 🚨 Don't change the code below 👇
# print(student_grades)
#





#Nesting
# {
#     Key: [List]
#     Key2: {Dict}
#  }

#
# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin",
# }
# #Nesting a List in a Dictionary
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Dresden"]
# }
#
# #Nesting a Dictionary in a Dictionary
#
# travel_log2 = {
#     "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#     "Germany": {"cities_visited": ["Berlin", "Dresden"], "total_visits": 5}
# }
# print(travel_log2)
#
#
# #Nesting Dictionary in a List
#
# travel_log3 = [
#     {
#         "country": "France",
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 12
#     },
#     {
#         "country": "Germany",
#         "cities_visited": ["Berlin", "Dresden"],
#         "total_visits": 5
#     },
# ]




# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #🚨 Do NOT change the code above
#
# #TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇
# def add_new_country(country_visited, times_visited, cities_visited):
#   travel_log.append({"country": country_visited, "visits": times_visited, "cities": cities_visited})
#
#   #Another option
#   # new_country = {}
#   # new_country["country"] = country_visited
#   # new_country["visits"] = times_visited
#   # new_country["cities"] = cities_visited
#   # travel_log.append(new_country)
#
#
# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)



#HINT: You can call clear() to clear the output in the console.

# import Day9art
#
# print(f"{Day9art.logo} \n Welcome to the secret auction program.")
#
# end = False
# bid_dict = {}
# highest_bid = 0
# name_of_winner = ''
#
# while not end:
#     name = input("What is your name? ")
#     bid = int(input("What's your bid? $"))
#     count = input("Are there any others bidders? Type 'yes' or 'no'.")
#
#     bid_dict[name] = bid
#
#     if count == 'no':
#         for key, value in bid_dict.items():
#             # bid_dict[key]
#             # print(bid_dict[key])
#             if value > highest_bid:
#                 highest_bid = value
#                 name_of_winner = key
#         end = True
#         print(f"End of the game,{name_of_winner} max value is {highest_bid}")
#     else:
#         print("Clear() function called")


#second option with FUNCTION
import Day9art

print(f"{Day9art.logo} \n Welcome to the secret auction program.")

end = False
bid_dict = {}

def find_highest_bidder(bid_dict):
    highest_bid = 0
    for key in bid_dict:
        bid_amount = bid_dict[key]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = key
    print(f"End of the game, winner is {winner} with a bid of ${highest_bid}")

while not end:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    count = input("Are there any others bidders? Type 'yes' or 'no'.")

    bid_dict[name] = bid

    if count == 'no':
        find_highest_bidder(bid_dict)
        end = True
    else:
        print("Clear() function called")


