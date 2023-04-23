#create a text file named numbers.txt
#open numbers.txt(read), open even.txt(append), open odd.txt(append)
with open("numbers.txt") as input_file, open("even.txt", "a") as output_even, open("odd.txt", "a") as output_odd:

#read the lines and identify if:
    for line in input_file:
        given_num = int(line)
#it's even
        if given_num %2 == 0:
#write to even.txt
            output_even.write(str(given_num))
#its's odd
        else:
#write to odd.txt
            output_odd.write(str(given_num))
