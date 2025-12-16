employee_file = open("employees.txt", "r") #read information from the file
#open("employees.txt", "w") #write information: change the file, new information, change exisiting info
#open("employees.txt", "a") #append information onto the end of the file 
#open("employees.txt", "r+") #read and write 

#employee_file.close() #you should close a file that you open at some point too 

print(employee_file.readable())
#this isn't working and idk why 

print(employee_file.read())

print(employee_file.readline()) # read a specific line 
print(employee_file.readline()) #having the two back to back will show two back to back 

print(employee_file.readlines()) #take all the lines in the file and put them into an array 

print(employee_file.readlines()[1]) #access the specific line in the index you're calling

