
# try:
#     file = open("a_file.txt")
#     dict = {"john": 123}
#     print(dict["abc"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as msg_error:
#     print(f"The msg {msg_error} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error i made up")

height = int(input("Enter height: "))
weight = int(input("Enter weight: "))

if height > 3:
    raise TypeError("Human height does not over 3 meter")

bmi = weight / height**2
print(bmi)