# Author: SMR (AMDG) 2/14/22
# Opens file from directory
file = open("alma_mater.txt", "r")
# While True
while True:
    # Set function equal to variable 'lines' 
     lines = file.readlines()
    # For lines in reversed(which is a class that reverses)
     for lines in reversed(lines):
    # Print the lines now reversed       
           print(lines)