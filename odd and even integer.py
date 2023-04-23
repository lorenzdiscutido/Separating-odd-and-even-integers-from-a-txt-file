#create a text file named numbers.txt
#open numbers.txt(read), open even.txt(append), open odd.txt(append)
with open("numbers.txt") as hotdog, open("even.txt", "a") as output_even, open("odd.txt", "a"):

#read the lines and identify if:
#it's even
#write to even.txt
#its's odd
#write to odd.txt
    for line in hotdog:
        print(line.strip())()

print("")

