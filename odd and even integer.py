#create a text file named numbers.txt
#open numbers.txt(read), open even.txt(append), open odd.txt(append)
with open("numbers.txt") as input_file, open("even.txt", "a") as output_even, open("odd.txt", "a"):

#read the lines and identify if:
    for line in input_file:
        given_num = line
#it's even
        if given_num %2 == 0:
            output_even.write(given_num)
#write to even.txt
#its's odd
#write to odd.txt

