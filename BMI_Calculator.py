weight = int(input("What is your weight?: \n")) #user_input_in_kilograms
height = float(input("What is your height?: \n")) #user_input_in_meters
BMI = (weight) / ((height)*(height)) #formula_to_calculate_BMI
BMI = round(BMI,2) #using_this_as_new_BMI_round_off_to_2_places

print(BMI) #using_formula_to_print_BMI
if (BMI >= 30):
    print("You are quite obese!") #equal_or_higher
elif (BMI >= 25):
    print("You are overweight!") #equal_or_higher
elif (BMI >= 18.5):
    print("You are normal!") #equal_or_higher
else:
    print("You are underweight!") #if_user_BMI_is_less_than_18.5