import pandas


data = pandas.read_csv("004 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
gray_squirel_count = len(data[data["Primary Fur Color"] == "Gray"])
cinamon_squirel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirel_count = len(data[data["Primary Fur Color"] == "Black"])


data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirel_count, cinamon_squirel_count, black_squirel_count]
}


make_csv_file = pandas.DataFrame(data_dict)
make_csv_file.to_csv("Squirrel.csv")
