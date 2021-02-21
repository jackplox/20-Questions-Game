# -*- coding: utf-8 -*-

####################################################################################################################
# Variables:
#..f........................This is the file with the questions.
#..content..................List of lines
#..uIn......................User input
#..idx......................List index of specified line to print
#..amtQ.....................Amount of times the loop will iterate
#..c........................Count of questions asked
#..filename.................Name of the file. Hardcoded as 'questions.txt', please ensure your file is named this.
#..i........................Incremental value for iteration
#####################################################################################################################


filename = "questions.txt"

#Read file, make list content with each index a seperate line
with open(filename) as f:
    content = f.read().splitlines()
#
#   AmtQ starts at -1 to offset the answers    
amtQ = -1
i = 0
   
## Amount of questions - Add one each line
while i <= len(content)/2+1:
    i = i * 2 + 1
    amtQ += 1

c = 0
idx = 0


print("\t\tWelcome to 20 Questions\n\tBy Jack Johnson\n\nPlease have your .txt file in the same directory as the 20qgame.py file.\n\nHere's your first question...\n")

while c != amtQ:
    
    uIn = input(content[idx])
    
    if uIn == 'y' or uIn == 'Y':
        idx = (idx * 2) + 1
        
        # Question successfully replied to
        c += 1
        
    elif uIn == 'n' or uIn == 'N':
        idx = (idx * 2) + 2
        
        # Question successfully replied to
        c += 1
    elif uIn == 'x' or uIn == 'X':
        break
        
    else:
        print("Error.... Please input either:\n\t'y' or 'Y' for yes\n\t'n' or 'N' for no.\n\t'x' or 'X' to exit the program.\n\n")
    
    # Check if amount of Qs successfully replied to matches the amount of Qs to be asked
    if c == amtQ:
        print("Your answer is... \n\n", content[idx], " !\n\nDid I get it right or what?")

f.close()