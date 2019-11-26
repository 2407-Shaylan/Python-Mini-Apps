num = int(input("Enter a number: \n"))                           #user_input
  
if num > 1:                                                      #if_statement_if_num_was_greater_than_one
   for i in range(2,num):                                        #range_starting_from_2_because_1_divided_into_anything_is_the_same
       if (num % i) == 0:                                        #modulus_equal_to_0
           print(num,"is not a prime number")                    #the_output_given                                  
           break 
   else:  
       print(num,"is a prime number")                            #else_if_an_input_is_a_prime_number_it_will_print_what_is_in_the_parenthesis
         
else:  
       print(num,"is a prime number")                            #else_if_an_input_is_a_prime_number_it_will_print_what_is_in_the_parenthesis                           

