user = input("Please enter a word or sentence: \n")      #user_input

listing = {}                                             #creating_a_list

for x in user:                                           #for_statement
    if x in listing:                                     #if_statement
            listing[x] += 1                              
    else:
        listing[x] = 1


print(listing)                                          #prints_frequency_of_characters_appearing_in_a_word_or_sentence
 