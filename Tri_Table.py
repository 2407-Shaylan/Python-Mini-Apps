num = int(input("Enter the number of rows needed: \n"))            #user_input
for i in range (1, num + 1):                                       #for_loop_rows
    for y in range (1 , i + 1):                                    #for_loop_columns
        print(i * y , end="  ")                                    #prints_out_rows_and_columns_like_multiplication_table
    print()                                                        #prints_on_a_new_line