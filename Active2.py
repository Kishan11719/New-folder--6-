# open the file in read mode
file_read = open('Codingal (3).txt','r')
print("File in Read Mode -")
print(file_read.read())
file_read.close()

# open the file in write mode
file_write = open('Codingal (3).txt', 'w')
# write in the file
file_write.write(" File in write mode ....")
file_write.write("Hi I am Penguin. I am 1 yr. old")
file_write.close()

# open the file in append mode
file_append = open('Codingal (3).txt', 'a')
file_append.write("\n File in append mode ....")
file_append.write("Hi! I am Penguin. I am 1 yr.old")
file_append.close()