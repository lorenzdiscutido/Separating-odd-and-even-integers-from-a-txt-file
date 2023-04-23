#create a text file named numbers.txt

with open("numbers.txt") as hotdog:
    for line in hotdog:
        print(line.strip())

print("")

