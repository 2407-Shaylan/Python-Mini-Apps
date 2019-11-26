string = input("Please enter a sentence: \n")                                          #user_input
character = input("What character/s of the sentence would you like removed?: \n")      #user_input
string1 = string                                                                       #creating_and_building_a_variable
for x in character:                                                                    #for_loop
    if x in character:                                                                 #if_statement_for_characters
        string1 = string1.replace(x, "")                                               #replace_chosen_character_from_user_input

print(string1)                                                                         #prints_string_with_removed_characters