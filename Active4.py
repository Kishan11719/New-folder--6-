fristfile = input("Enter the name of frist file ")
secondfile = input("Enter the name of second file")

# opening both files in read only mode to read initial contents
f1 = open(fristfile, 'r')
f1 = open(secondfile, 'r')

# printing the contens of the file before appending 
print('content of frist file before appending -\n', f1.read())
print('content of second file before appending -\n', f1.read())

# closing the files
f1.close()
f2.close()

# openu