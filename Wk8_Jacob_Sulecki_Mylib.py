#----------------------------------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------------------------------#

#This menu function will be called to set up the options for the user depending on what kind of calculation they want
#Selections will be stored in a variable to then call the correct function
def Menu():
    print('[1] ADD two numbers')
    print('[2] SUBTRACT two numbers')
    print('[3] MULTIPLY two numbers')
    print('[4] DIVIDE two numbers')    
    print('[5] SCALC')
    print('[6] ALL IN ONE')
    print('[7] Write to File')
    print('[8] Read from File')
    print('[0] EXIT the program')

#----------------------------------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------------------------------#

class basicMath(): #making a class here makes the most sense as the functions/methods inside are the building blocks for the entire program
     
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    #All functions below are more or less the same, they take in the user entered numbers and do the corresponding arithmetic 
    def funcAdd(self):
        return self.num1 + self.num2

    def funcSub(self):
        return self.num1 - self.num2

    def funcMultiply(self):
        return self.num1 * self.num2

    #This divide function is different simply because you will get an error if dividing by 0, 
    # so I put logic in that will allow the program to keep running even if the user chooses to divide by 0
    def funcDivide(self): 
        try: #instead of using an if else logic I tried the exception logic with the built in error recognition 
            return self.num1 / self.num2
        except ZeroDivisionError: #Function will return the division unless user chooses 0 for second number; you can't divide by 0 so this exception will allow the program to continue 
            return 'You cannot divide by 0'

#----------------------------------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------------------------------#


#this function allows the entry of the string "stringThing", and uses the split function to split the entry up into different 
#variables and depending on which operator the user selects, this function will return the corelating arithmetic method  
def scalc(stringThing):

    a = stringThing.split(',')

    num1 = int(a[0])
    num2 =  int(a[1])
    operand = a[2]
    obj = basicMath(num1, num2)

    if operand == '+':
        return obj.funcAdd()

    elif operand == '-':
        return obj.funcSub()

    elif operand == '*':
        return obj.funcMultiply()

    elif operand == '/':
        return obj.funcDivide()

    else:
        return('You need to enter your inputs in the correct format: (x,y,*)')

#----------------------------------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------------------------------#


#this allInOne function stores all the different operands and prints all outputs to the user
#Using the dictionary we can pass the methods already created in the basicMath class thus keeping the error logic for division and such
def allInOne(num1, num2):

    obj = basicMath(num1,num2)
    
    allOutput = {
        'add' : obj.funcAdd(),
        'sub' : obj.funcSub(),
        'mul' : obj.funcMultiply(),
        'div' : obj.funcDivide()
    }

    return str(num1) + ' + ' + str(num2) + ' = ' + str(allOutput['add']) + '\n' + str(num1) + ' - ' + str(num2) + ' = ' + str(allOutput['sub']) + '\n' + str(num1) + ' * ' + str(num2) + ' = ' + str(allOutput['mul']) + '\n' + str(num1) + ' / ' + str(num2) + ' = ' + str(allOutput['div']) + '\n'


#----------------------------------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------------------------------#

class wrfile():

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def writeFile(self):
        f = open('calcOutput.txt', 'a') 
        print('Outputs written to "calcOutput.txt"')
        return f.write(allInOne(self.num1, self.num2))

    def readFile(self):
        f = open('calcOutput.txt', 'r')
        return print(f.read())
       