lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]

#append two lists to each other, gives us both lists
#friends.extend(lucky_numbers) 
#print(friends)

#add something to the end of the list
#friends.append("Creed") 
#print(friends)

#puts the element you want at the specific position and pushes everything to the right one index position
#friends.insert(1, "Bob")
#print(friends) 

#removes an element from the list
#friends.remove("Jim")
#print(friends) 

#will delete everything from the list
#friends.clear()
#print(friends) 

#removes the last element in the list
#friends.pop()
#print(friends) 

#will tell me if this is in the list and return index
#print(friends.index("Toby")) 
#tell us how many times Jim is inlcuded int he list
#print(friends.count("Jim")) 

#sort the list in ascending order, in this case alphabetical
#friends.sort()
#print(friends)
#lucky_numbers.sort()
#print(lucky_numbers)

#reverse a list 
#lucky_numbers.reverse()
#print(lucky_numbers)

#create a copy of the list
friends2 = friends.copy()
print(friends2)