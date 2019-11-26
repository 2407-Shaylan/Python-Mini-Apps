sentence = input("Please enter a sentence: \n")       #user_input
space = " ".join(sentence.split(" "))                 #creating_and_building_a_variable
for i in range(0, len(space)):                        #for_statement_starting_in_range_0_to_length_of_space
    if i % 2 == 0:                                    #if_i_modulus_2_=_0...
        print(space[i].upper(), end= "")              #this_will_be_printed
    else:
        print(space[i].lower(), end= "")              #the_programme_will_print_this