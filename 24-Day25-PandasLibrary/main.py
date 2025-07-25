import csv
import pandas



# with open("002 weather-data.csv") as weather_data:
#     weather_content = weather_data.readlines()
#     print(weather_content)



# with open("002 weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     temp = []
#     for row in data:
#         # print(row[1])
#         if row[1] != 'temp':
#             temp.append(int(row[1]))
#     print(temp)

data = pandas.read_csv("002 weather-data.csv")
print(data)
print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

sum_of_all_temps = 0
for temp in data["temp"]:
    sum_of_all_temps += temp

avg_temp = sum_of_all_temps / len(data["temp"])
print("Average temprature is: ", avg_temp)

print(data["temp"].mean())
print(data["temp"].max())

# get column
print(data.condition)
# get row
print(data[data.day == "Thursday"])
print(data[data.temp == data["temp"].max()])


players_dict = {
    "Players": ["Virat", "Roy", "Smith"],
    "Country": ["Ind", "Eng", "Aus"],
    "roles": ["Middle Order", "Opener", "Middle Order"],
    "Status": ["Moderate", "Aggresive", "Moderate"]
}

players_record = pandas.DataFrame(players_dict)
players_record.to_csv("players_record.csv")
print(players_record)
