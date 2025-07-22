
# OPEN AND READ A FILE
with open("D:\\100DaysToCodePython\\23-Day24-FileSystem\\my_file.txt") as my_file:
# my_file = open("my_file.txt")
    contents = my_file.read()
    print(contents)



# Write to a file
# with open("my_file.txt", mode="a") as file:
#     file.write("\nFile changes or tempered!")

# my_file.close()