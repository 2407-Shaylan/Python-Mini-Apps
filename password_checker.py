password = input("Enter your password: ") #userinput
counter = 0 #introducing_a_counter_for_last_sentence
haveLength = False  #initalise_variable_as_false
#if not (len(password)>= 6):
    #print("This password must have 6 characters or more!") #error_add_6_or_more_characters
#else:
    #print("Good, this password has more than 6 characters.") #correct_for_password

upCase = False #initalise_variable_as_false
if not any(char.isupper() for char in (password)): 
    print("Error: This password must have one uppercase letter!!!") #add_one_upCase_letter
else:
    print("Good, this password does have at least one uppercase letter.") #correct_for_password

lowCase = False #initalise_variable_as_false
if not any(char.islower() for char in (password)): 
    print("Error: This password must have one lowercase letter!!!") #add_one_lowCase_letter
else:
    print("Good, this password does have at least one lowercase letter.") #correct_for_password
    
haveNum = False #initalise_variable_as_false
if not any(char.isdigit() for char in (password)): 
    print("Error: This password must have at least one numerical digit!!!") #add_one_numerical_digit
else:
    print("Good, this password does have at least one numerical digit.") #correct_for_password


haveLength = input("Are there 6 or more characters? (Yes or No): ") #asking_series_of_yes_or_no_questions

if haveLength == "Yes":
    haveLength == True
    counter += 1 #add_to_counter

upCase = input("Are there at least one or more upcase letters? (Yes or No): ")
if upCase == "Yes":
	upCase = True
	counter += 1  #add_to_counter

lowCase = input("Are there at least one or more lowcase letters? (Yes or No): ")
if lowCase == "Yes":
	lowCase = True
	counter += 1  #add_to_counter

haveNum = input("Are there at least one or more numerical digits? (Yes or No): ")
if haveNum == "Yes":
	haveNum = True


if counter >= 3:  #total_add_up_to_counter_to_meet_3_characteristics
    print("This is a suitable password!, Welcome")

else:
    print("Please make sure you have met the password criteria!")