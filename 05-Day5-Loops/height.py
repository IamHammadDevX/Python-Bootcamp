# tale input of student heights
stdHeights = input("Enter the height of all students: ").split()

# print(stdHeights)
# print(type(stdHeights))
# print(len(stdHeights))

for n in range(0, len(stdHeights)):
    stdHeights[n] = int(stdHeights[n])

# # calculate the sum og heights
totalHgt = 0
for height in stdHeights:
    totalHgt += height

# calcualte the length
cnt = 0
for stdCount in stdHeights:
    cnt += 1

avg = round(totalHgt / cnt)
print(avg)