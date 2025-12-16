#special strucutre in python allowing us to store info in key value pairs
#when you want to access specific info you can just refer to the key
#in a reg dictionary the word would be the key and the value would be the definiton

monthconversions = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December",
}

#way to access the keys
print(monthconversions["May"])
#way to access a key that gives us a default value
print(monthconversions.get("Luv", "Not a valid key")) 

