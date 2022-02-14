# Author: SMR (AMDG) 2/8/22
# Opens the text file in directory
my_file = open("alma_mater.txt", "r")
# While Statement
while True:
    # Creating function set = to variable file    
        line = my_file.readline()
    # If leng of line equals 0 stop    
        if len(line) == 0:
            break       
    # Print line    
        print (line, end="")
    # Add space    
        print(" ")
my_file.close()

