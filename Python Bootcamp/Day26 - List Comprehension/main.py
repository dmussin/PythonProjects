#new_list = [new_item for item in list]

# numbers = [1, 2, 3]
# new_list = [n+1 for n in numbers]
#
# print(new_list)

# name = "Dani"
# new_list = [letter for letter in name]
# print(new_list)
#
# new_range_list = [i * 2 for i in range(1,5)]
# print(new_range_list)
#
#
# #new_list = [new_item for item in list if test]
#
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Freddie']
# short_names = [name for name in names if len(name) < 5]
#
# uppercase_names = [name.upper() for name in names if len(name) > 5]
# print(uppercase_names)


# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above 👆
#
# #Write your 1 line code 👇 below:
#
# squared_numbers = [num * num for num in numbers]
#
# #Write your code 👆 above:
#
# print(squared_numbers)






# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above
#
# #Write your 1 line code 👇 below:
#
# result = [num for num in numbers if (num % 2) == 0]
#
# #Write your code 👆 above:
#
# print(result)








# with open('file1.txt') as data1:
#     data1 = data1.readlines()
#
# with open('file2.txt') as data2:
#     data2 = data2.readlines()
#
# result = [int(num) for num in data1 if num in data2]
# print(result)






#---------------------------------------------------------
# Dictionary Comprehension

# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}

# import random
#
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Freddie']
# students_scores = {student:random.randint(1, 100) for student in names}
#
# print(students_scores)
#
# passed_students = {student:score for (student, score) in students_scores.items() if score > 60}
# print(passed_students)
# #





# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆
#
# # Write your code below:
#
# result = {word: len(word) for word in sentence.split()}
#
# print(result)



# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# # 🚨 Don't change code above 👆
#
#
# # Write your code 👇 below:
#
# weather_f = {weekday: (temp * 9/5) + 32 for (weekday, temp) in weather_c.items()}
#
# print(weather_f)




# -------------

# import random
# import pandas
#
# student_dict = {
#     "student": ['Alex', 'Beth', 'Caroline', 'Dave', 'Freddie'],
#     "score": [56, 78, 97, 87, 69]
# }
#
#
# #Looping thought dictionaries:
# # for (key, value) in students.items():
# #     print(value)
#
# students_data_frame = pandas.DataFrame(student_dict)
# print(students_data_frame)
#
# #Loop throught a data frame
# # for (key, value) in students_data_frame.items():
# #     print(value)
#
# # Loop through rows of a data frame
# for (index, row) in students_data_frame.iterrows():
#     if row.student == "Alex":
#         print(row.score)




