import math
import os

#These are the possible choices for a menu option
menuChoices = ['1', '2', '3']

#Prints the main menu
def printMainMenu():
    print("====================\n1. Permutation\n2. Combination\n3. Quit\n====================\n\nInput your selection: ")

#Takes selection as input and calls whatever function is desired
def runSelection(selection):
     #Checks for the different menu options
    if selection == '1':
        os.system('cls')
        permLoop()
        os.system('pause')
        os.system('cls')

    elif selection == '2':
        os.system('cls')
        combLoop()
        os.system('pause')
        os.system('cls')
        
    elif selection == '3':
        os.system('cls')
        quit()    

#Calculates Premutations
def permLoop():
    #Gets the value for n
    print('Enter a value for \'n\'(total number of items): ')

    try:
        #Attemps to assign n to the integer value from input
        n = int(input())
    except:
        #If its not an integer, it exits the function
        print('Please enter an integer.')
        return 1
  
    #Gets the value for k
    print('Enter a value for \'k\'(number of items in arrangment): ')
    try:
        #Attemps to assign k to the integer value from input
        k = int(input())
    except:
        #If its not an integer, it exits the function
        print('Please enter an integer.')
        return 1

    #Prints the answer
    print('The answer is: ' + str(math.perm(n, k)))

#Calculates Combinations
def combLoop():
    #Gets the value for n
    print('Enter a value for \'n\'(total number of items): ')

    try:
        #Attemps to assign n to the integer value from input
        n = int(input())
    except:
        #If its not an integer, it exits the function
        print('Please enter an integer.')
        return 1
  
    #Gets the value for k
    print('Enter a value for \'k\'(number of items in arrangment): ')
    try:
        #Attemps to assign k to the integer value from input
        k = int(input())
    except:
        #If its not an integer, it exits the function
        print('Please enter an integer.')
        return 1

    #Prints the answer
    print('The answer is: ' + str(math.comb(n, k)))

#This is the main loop
while True:
    #Prints the main menu and waits for a selection
    printMainMenu()
    selection = input()

    #If the selection is not contained within the menu choices, it reprompts
    if selection not in menuChoices:
        os.system('cls')
        print("Please choose one of the choices provided.")

    #Runs the desired function
    runSelection(selection)

   