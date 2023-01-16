# with open('weather_data.csv') as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open ('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)


# import pandas

# data = pandas.read_csv('weather_data.csv')
# # print(data)
# # print(type(data))
# # print(data['temp'])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# data_temp = data['temp'].tolist()
# print(data_temp)

# sum_temp = 0
# average_temp = 0
#
# for i in data_temp:
#     sum_temp += i
#     average_temp = sum_temp / len(data_temp)
#
# print(average_temp)
#....................................
# average_temp = sum(data_temp) / len(data_temp)
# print(average_temp)
#..............................

# print(data['temp'].mean())
# print(data['temp'].max())

#Get Data in Colums
# print(data['condition'])
# print(data.condition)

#Get Data in Row
# print(data[data.day == 'Monday'])
# print(data[data.temp == data['temp'].max()])

# monday = data[data.day == 'Monday']
# # print(monday.condition)
# temp = (int(monday.temp) * 9/5) + 32
# print(f'Monday temperature is {temp}°F')


#Create a dataframe from a scratch
# data_dict = {
#     "students": ["Dani", "Kari", "Pyth"],
#     "scores": [76, 56, 65]
# }
#
# datas_dict = pandas.DataFrame(data_dict)
# datas_dict.to_csv("new_data.csv")
# print(datas_dict)
#
#


# //////////////////////////////////////

import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
# fur = data['Primary Fur Color'].tolist()
#
# gray_fur = 0
# black_fur = 0
# cinnamon_fur = 0
#
# for i in fur:
#     if i == "Gray":
#         gray_fur += 1
#     elif i == "Black":
#         black_fur += 1
#     else:
#         cinnamon_fur += 1
#
#
# data_dict = {
#     "Fur Color": ['grey', 'red', 'black'],
#     "Count": [gray_fur, cinnamon_fur, black_fur]
# }
# print(gray_fur)
#
# fur_dict = pandas.DataFrame(data_dict)
# fur_dict.to_csv("squirrel_count.csv")
# print(fur_dict)

# ---------------------------------
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count, red_squirrels_count, black_squirrels_count)

data_dict = {
    "Fur Color": ['grey', 'red', 'black'],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv('count.csv')