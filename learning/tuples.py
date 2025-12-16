#tuple is a type of data structure
#a container that we can store values in 
#key differences from lists: can't modify, 
#                            uses different paranthesis, 
#                            tuples for data that's never gonna change
#                            

#create a tuple 
#common edample is coordinates
coordinates = (4, 5) #use open and close paranthesis to create tuple
#tuples are immutable -- once you create it you can't modify it 

print(coordinates[0]) #access specific elements inside tuple 

# coordinates[1] = 10 #can't do this because it's an error 

#can make a list of tuples but the tuples themlseves can't be modified 
coordinates = [(90, 4), (34, 2), (10, 9), (67, 87)]

