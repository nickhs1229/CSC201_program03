#Project 5
def match_gact(): #Define the program
    inp6 = input("Enter a string of DNA: ") #Define the first input
    inp7 = input("Enter a string of DNA: ") #Define the second input
    if "G" in inp6 and "A" in inp6 and "C" in inp6 and "T" in inp6 and "G" in inp7 and "A" in inp7 and "C" in inp7 and "T" in inp7: #If both inputs contain the appropriate characters
        print([a == b for (a, b) in zip(inp6, inp7)].count(True), "Matches") #Check both strings for matching characters and then print the number of matches
    else: #If both inputs contain any other characters
        print("Invalid DNA sequence.") #Print an error message
match_gact() #Execute the program

#Project 6
def long_gact(): #Define the program
    inp8 = input("Enter a string of DNA: ") #Define the first input
    inp9 = input("Enter a string of DNA: ") #Define the second input
    if "G" in inp8 and "A" in inp8 and "C" in inp8 and "T" in inp8 and "G" in inp9 and "A" in inp9 and "C" in inp9 and "T" in inp9: #If both inputs contain the appropriate characters
        answer = "" #Define the answer
        len1, len2 = len(inp8), len(inp9) #Define the lengths of both inputs
        for i in range(len1): #Define the range of the first length
            match = "" #Define the match
            for j in range(len2): #Define the range of the second length
                if (i + j < len1 and inp8[i + j] == inp9[j]): #If the range and respective lengths are of particular sizes
                    match += inp9[j] #Adjust the match for the length of the second input
            else: #For all other sizes and lengths of the variables
                if (len(match) > len(answer)): answer = match #If the length of the match is greater than the length of the answer then set answer equal to match
                match = "" #Redefine the match
        print(answer) #Print the answer
    else: #If both inputs contain any other characters
        print("Invalid DNA sequence.") #Print an error message
long_gact() #Execute the program

#Project 7
def database_gact(): #Define the program
    myList = ("GCTCAAGCCTAGCTACTAGCAGTT", "ACTCAAGCATAGCTCCATGCGTTCA", "AGCTAAGCTTAGCTCCATGCG") #Define the gene database
    inp10 = input("Enter a string of DNA: ") #Define the first input
    if "G" in inp10 and "A" in inp10 and "C" in inp10 and "T" in inp10: #If the input contains the appropriate characters
        for s in myList: #For each variable in the database
            print([a == b for (a, b) in zip(inp10, s)].count(True), "Matches") #Print the number of matches between the input and each variable in the database
        answer = "" #Define the answer
        len1, len2 = len(inp10), len(s) #Define the lengths of the input and the database
        for i in range(len1): #Define the range of the first length
            match = "" #Define the match
            for j in range(len2): #Define the range of the second length
                if (i + j < len1 and inp10[i + j] == s[j]): #If the range and respective lengths are of particular sizes
                    match += s[j] #Adjust the match for the length of the database
            else: #For all other sizes and lengths of the variables
                if (len(match) > len(answer)): answer = match #If the length of the match is greater than the length of the answer then set answer equal to match
                match = "" #Redefine the match
        print(answer) #Print the answer
    else: #If the input contains any other characters
        print("Invalid DNA sequence.") #Print an error message
database_gact() #Execute the program
