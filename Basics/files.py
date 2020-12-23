#File handling is an important part of any web application.

#we must use the name of the file and "r" to read from a file
file = open("example.txt","r")
print(file.read())
file.close()

#we must use the name of the file and "w" to write in a file
file = open("example.txt","w")
file.write("More text")
file.close()

#we must use the name of the file and "a" to append text in a file
file = open("example.txt","a")
file.write("More text")
file.close()    

#we must use the name of the file and "x"  to create  text in a file
file = open("example2.txt","x")
file.write("More text")
file.close()    

#to delete file we must import os

import os
os.remove("example2.txt")
