# This is the flower box and it should be at the beginning of each assignment
# You must add comments to your code
# Program name : Wk8_Jacob_Sulecki.py
# Student Name : Jacob Sulecki
# Course : ENTD220
# Instructor : David Gunderman
# Date : 29 January 2023
# Description : This code will utilize classes & functions/methods in order to calculate user inputted numbers with addition, subtraction, multiplication, and division or all at once
# Copy Wrong : this iteration of the calculator uses a menu in order to pick what type of calculation the user wants
#whether that be a single calculation, using the Scalc() function or allInOne() function that prints all operands and their calculations
#It utilizes classes to call the correct methods to calculate whatever the user selects on the menu and also has the option to write outputs to a text file or read from a file.

from Wk8_Jacob_Sulecki_Mylib import * #This imports all the function in that file as a module to be used in this main file. 


#Main program

print('********************* CALCULATOR *********************')
print() #spacer

Menu() #calling to print menu to user
option = int(input('Please make a selection: '))
#-------------------------------------------------------------------------------------------------------------
while option !=  0:

    if option == 1:
        num1 = int(input('Enter in your first number: '))
        num2 = int(input('Enter in your second number: '))
        obj = basicMath(num1, num2)
        print(str(num1) + ' + ' + str(num2) + ' = ' + str(obj.funcAdd()))

    elif option == 2:
        num1 = int(input('Enter in your first number: '))
        num2 = int(input('Enter in your second number: '))
        obj = basicMath(num1, num2)
        print(str(num1) + ' - ' + str(num2) + ' = ' + str(obj.funcSub()))

    elif option == 3:
        num1 = int(input('Enter in your first number: '))
        num2 = int(input('Enter in your second number: '))
        obj = basicMath(num1, num2)
        print(str(num1) + ' * ' + str(num2) + ' = ' + str(obj.funcMultiply()))

    elif option == 4:
        num1 = int(input('Enter in your first number: '))
        num2 = int(input('Enter in your second number: '))
        obj = basicMath(num1, num2)
        print(str(num1) + ' / ' + str(num2) + ' = ' + str(obj.funcDivide()))

    elif option == 5:
        stringThing = input('Enter your calculation like this: num1,num2,operator (ex: 15,50,*):')
        print(scalc(stringThing))

    elif option == 6:
        num1 = int(input('Enter in your first number: '))
        num2 = int(input('Enter in your second number: '))
        print(allInOne(num1, num2))

    elif option == 7:
        num1 = int(input('Enter in your first number: '))
        num2 = int(input('Enter in your second number: '))
        objF = wrfile(num1, num2)
        objF.writeFile()

    elif option == 8:
        num1 = int(input('Enter in your first number: '))
        num2 = int(input('Enter in your second number: '))
        objF = wrfile(num1, num2)
        objF.readFile()


    else:
        print('Invalid Option. Please try again')
#-------------------------------------------------------------------------------------------------------------

    print()#Using as a spacer
    Menu()#calling menu again so we dont get stuck in a forever loop
    option = int(input('Please make a selection: \n'))


print('********************************************************')
print('Thank you for using my calculator! Goodbye.')
print('********************************************************')