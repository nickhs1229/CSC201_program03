#Nicholas Hitchens-Spellman

#Project 1
def mirror_gact(): #Define the program
    inp1 = input("Enter a string of DNA: ") #Define the input
    print(inp1.replace("G", "X").replace("C", "G").replace("X", "C").replace("T", "Y").replace("A", "T").replace("Y", "A")) #Mirror all input "GACT" and print the result
mirror_gact() #Execute the program

#Project 2
def reverse_gact(): #Define the program
    inp2 = input("Enter a string of DNA: ") #Define the input
    print(inp2[::-1]) #Reverse the direction of the input
reverse_gact() #Execute the program

#Project 3
def verify_gact(): #Define the program
    inp3 = input("Enter a string of DNA: ") #Define the input
    if "G" in inp3 and "A" in inp3 and "C" in inp3 and "T" in inp3: #If the input contains the appropriate characters
        print("Valid") #Print "Valid"
    else: #If the input contains any other characters
        print("Invalid") #Print "Invalid"
verify_gact() #Execute the program

#Project 4
def compare_gact(): #Define the program
    inp4 = input("Enter a string of DNA: ") #Define the first input
    inp5 = input("Enter a string of DNA: ") #Define the second input
    inp4m = inp4.replace("G", "X").replace("C", "G").replace("X", "C").replace("T", "Y").replace("A", "T").replace("Y", "A") #Define the mirrored first input
    inp5m = inp5.replace("G", "X").replace("C", "G").replace("X", "C").replace("T", "Y").replace("A", "T").replace("Y", "A") #Define the mirrored second input
    inp4r = inp4[::-1] #Define the reversed first input
    inp5r = inp5[::-1] #Define the reversed second input
    if "G" in inp4 and "A" in inp4 and "C" in inp4 and "T" in inp4 and "G" in inp5 and "A" in inp5 and "C" in inp5 and "T" in inp5: #If both inputs contain the appropriate characters
        if inp4 == inp5 and inp4m == inp5m and inp4r == inp5r: #If all variables equal their input counterparts
            print("Both DNA fragments match: ") #Print a confirmation that the inputs match
        elif inp4 != inp5 or inp4m != inp5m or inp4r != inp5r: #If all variables do not match
            print("Both DNA fragments do not match: ") #Print a confirmation that the inputs do not match
    else: #If both inputs contain any other characters
        print("Invalid DNA sequence or inequal DNA lengths.") #Print an error message
compare_gact() #Execute the program
