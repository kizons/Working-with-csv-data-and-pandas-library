import pandas

# with open("weather_data.csv") as weather:

#     data = weather.readlines()
#     print(data)


# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)



# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)

# avg_temp = sum(temp_list) / len(temp_list)
# print(avg_temp)
#
# print(data["temp"].mean())
#
# print(data["temp"].max())
#
# # get data in column
# print(data["condition"])
# print(data.condition)

# print(data[data.day == "Monday"])
#
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# print(int(monday.temp) * 9/5 + 32)

# Create a dataframe from scratch

# data_dict = {
#     "Students": ["Amy", "James", "Angela"],
#     "Score": [30, 40, 60]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

# counting number of squirrels according to their color
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data(1).csv")
#
# color_data = data["Primary Fur Color"]
#
# squirrel_colors = data["Primary Fur Color"].value_counts()
# print(squirrel_colors)
#
# squirrel_colors.to_csv("squirrel_count.csv")

# OR

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
# print(gray_squirrels_count)
# print(red_squirrels_count)
# print(black_squirrels_count)

data_dict = {"Fur Color": ["gray", "red", "black"],
             "count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
             }
# print(data_dict)

df = pandas.DataFrame(data_dict)
print(data)
df.to_csv("squirrel_count.csv")