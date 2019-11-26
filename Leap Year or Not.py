year = int(input("Enter a year: \n")) #user_inputs_a_year
numYear = int(input("How many years would you like to go up to?: \n")) #user_input_how_many_years_would_be_viewed_for_a_leap_year_or_not
end = year + numYear #building_a_variable

for i in range (year, end): #for_loop_to_differentiate_leap_years


    if(i%4==0 and i%100 !=0 or i%400==0): #differentiation
        print(f"{i} is a leap year!!") #if_year_is_leap_it_will_be_stated
    else:
        print(f"{i} is not a leap year!!") #else_statement_if_year_is_not_leap


