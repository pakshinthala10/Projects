is_male = True 
is_tall = True

#if is_male == True or is_tall == True: 
   # print("ew.")
#else:
   # print("good.")

if is_male and is_tall:
    print('You are a tall male')
elif is_male and not(is_tall):
    print("You are a short male.")
elif not(is_male) and is_tall: 
    print("You are tall.")
else: 
    print("You are either not male and not tall")