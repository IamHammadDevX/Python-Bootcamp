
number_list = [1, 2, 3]


new_list = [item for item in number_list]
new_list.append(4)
print(new_list, number_list)

name = "Jason"

new_name_list = [letter for letter in name]
print(new_name_list, name)

range_lst = [num * 2 for num in range(1, 5)]
print(range_lst)

names = ["Beth", "Dave", "Eleanor", "Jason", "Elon", "Julian"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

# Exercise # 1
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
square_list = [n**2 for n in numbers]
print(square_list)
# Exercise # 2
even_list = [num for num in numbers if num%2 == 0]
print(even_list)