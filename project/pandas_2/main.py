
#Example 1

# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#
# print(data)

# Example 2

# import csv
# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


# Example 3
# import pandas
# data = pandas.read_csv("weather_data.csv")
# print(data)

# dic_data = data.to_dict()
# print(dic_data)

# Find the mean/average of the temperature
# list_data = data["temp"].to_list()
# print(list_data)
# # average = 0
# # for avg in list_data:
#     # average += avg
# # print(average/len(list_data))
# average = data["temp"].mean()
# print(average)

# Find the largest number from Temperature
# large = data["temp"].max()
# print(large)
# monday = data[data.day == 'Monday']
# print(monday.temp)


# How to convert dictinoary to CSV or convert to panda data frame

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("writing_local.csv")

# Like a Fresher coder

# import pandas as pd
# data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# color_list = []
# count = [0, 0, 0]
#
# for color in data['Primary Fur Color']:
#     if color not in color_list:
#         color_list.append(color)
#     if color == 'Gray':
#         count[0] += 1
#     elif color == 'Cinnamon':
#         count[1] += 1
#     elif color == 'Black':
#         count[2] += 1

# color_list.pop(0)
#
# colors = {"Fur Color": color_list, "Count": count}

# data = pd.DataFrame(colors)
# data.to_csv("squirrel_count.csv")

# Alternative method


import pandas as pd
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel = len(data[data["Primary Fur Color"] == "Black"])

dict_construction = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel, red_squirrel, black_squirrel]
}

new_data = pd.DataFrame(dict_construction)
new_data.to_csv("updated_squirrel.csv")