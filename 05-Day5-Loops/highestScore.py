stdScrs = input("Enter Student scores: ").split()

for n in range(0, len(stdScrs)):
    stdScrs[n] = int(stdScrs[n])

highestHeight = 0
for height in stdScrs:
    if height > highestHeight:
        highestHeight = height


print(f"The highest score is {highestHeight}")