import pandas
import random

names = ["Beth", "Dave", "Eleanor", "Jason", "Elon", "Julian"]
std_scores = {student:random.randint(1, 100) for student in names}
print(std_scores)

passed_std = {key:value for (key, value) in std_scores.items() if value >= 40}
print(passed_std)

# exercise 1
# string number count
sentence = "What is the Airspeed velocity of an unladen swallow?"

result = {word:len(word) for word in sentence.split()}
print(result)


# Exercise 2
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day:(temp_c*9/5) + 32 for (day, temp_c) in weather_c.items()}
print(weather_f)

student_dict = {
    "student": ["Angela", "Yu", "Beth", "Devin"],
    "score": [76, 45, 68, 89]
}
# loop through dictionary
# for (key, value) in student_dict.items():
#     print(key, value)

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# loop through pandas
for (index, row) in student_data_frame.iterrows():
    print(row)