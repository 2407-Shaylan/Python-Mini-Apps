dna = input("Enter the DNA sequence in which you want to translate: \n") #user_input
def translate(codon): #defining_a_function_with_parameters
    if codon in ("ATA","ATC", "ATT"): #if_user enters these codes
        return "I"
    if codon in ("CTA","CTC","CTG","CTT","TAA","TTG"): #if_user enters these codes
        return "L" #this_amino_acid_will_be_returned
    if codon in ( "GTA","GTC","GTG","GTT"): #if_user enters these codes
        return "V" #this_amino_acid_will_be_returned
    if codon in ("TTC","TTT"): #if_user enters these codes
        return "F" #this_amino_acid_will_be_returned
    if codon == "ATG": #if_user enters this code
        return "M" #this_amino_acid_will_be_returned
    else:
        return "X"
amino_acids = "" #creating_a_variable

for i in range(0,len(dna), 3):
    amino_acids+=translate(dna[i : i + 3])
print(f"The amino acid/(s) of the given DNA sequence is/are {amino_acids}")

#compulsory task 2


x = open("DNA.txt","r")                    #opening_a_text_file
occurence = x.read()                       #reading_file
occurence = occurence.replace("\r", "")
x.close()                                  #closing_file

dna_upper = occurence.upper()              #capitialising_all_letters_in_text
    
new_file1 = open("normalDNA.txt", "w")     #creating_a_new_file
new_file1.write(dna_upper)                 #all_characters_to_capital_from_DNA.txt

new_file1.close()                          #closing_file_after_completion

replace_T = occurence.replace("a","T")     #replacing_small_a_to_capital_T

new_file2 = open("mutatedDNA.txt", "w")    #writing_a_new_file
new_file2.write(replace_T)                 #writing_this_variable_to_the_text_file

new_file2.close()                          #closing_the_file

def txtTranslate():                        #defining_a_function
    translate(dna_upper)                   #translating
    translate(replace_T)                   #translating

txtTranslate()                             #calling_a_function