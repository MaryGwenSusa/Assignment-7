def header():
    title = "**Password Validator**"
    print("*" * len(title)) # created a header design
    print(title)
    print("*" * len(title))

def validPassword(inputPassword):
    """\033[4mEvaluate if the input is valid as a password.\033[0m

    These are the conditions need to be met:
    if its greater than \033[3m\033[32m15 characters\033[0m;
    if it has at least \033[3m\033[34mone uppercase letter\033[0m;
    if it has at least \033[3m\033[35mone numeral\033[0m; and
    if it has any of the \033[3m\033[36mspecial characters (!#$%&()*+,-./:;<=>?@[\]^_{|}~)\033[0m.
    """
    specialSymbol = ['$','@','#','!','%','&','(',')','*','+',',','-','.',';','/',':','<','=','>','?','[',']','^','_','{','|','}','~']
    inputValue = True
    if not len(inputPassword):
        print("\033[41mEmpty string was entered!\033[00m")
        exit(0)
    if len(inputPassword) < 15:
        print('The length of password should be \033[4m\033[32mgreater than 15 characters.\033[0m')    
        inputValue = False
    if not any(char.isupper() for char in inputPassword): # determines if there is no letter in uppercase in inputPassword characters
        print('The password should have at least \033[4m\033[33mone uppercase letter.\033[0m')  
        inputValue = False
    if not any(char.isdigit() for char in inputPassword): # determines if there is no digit in inputPassword characters
        print('The password should have at least \033[4m\033[34mone numeral.\033[0m')
        inputValue = False
    if not any(char in specialSymbol for char in inputPassword): # determines if there is no special symbol in inputPassword characters
        print('The password should have at least \033[4m\033[35mone special character (!#$%&()*+,-./:;<=>?@[\]^_{|}~).\033[0m')
        inputValue = False
    elif inputValue:
        print('\033[46mOutput: \033[3mValid\033[00m')

header()      
print(validPassword.__doc__) # this will print the docstring indicated in the defined function
password = input('\033[91mInput:\033[00m ')
validPassword(password)


# another version utilizes string module
import string
def header():
    title = "**Password Validator**"
    print("*" * len(title)) # created a header design
    print(title)
    print("*" * len(title))

def validPassword(inputPassword):
    """\033[4mEvaluate if the input is valid as a password.\033[0m

    These are the conditions need to be met:
    Should contain more than \033[3m\033[32m15 characters\033[0m;
    Should contain at least \033[3m\033[34mone uppercase letter\033[0m;
    Should contain at least \033[3m\033[35mone numeral\033[0m; and
    Should contain any of the \033[3m\033[36mspecial characters (!"#$%&()*+,-./:;<=>?@[\]^_`{|}~)\033[0m.
    """  
    inputValue = True
    if not len(inputPassword):
        print("\033[41mEmpty string was entered!\033[00m")
        exit(0)
    if len(inputPassword) < 15:
        print('The length of password should be \033[4m\033[32mgreater than 15 characters.\033[0m')    
        inputValue = False

    evalCapitalL = evalDigit = evalSpecialCha = 0 # initializations (for creating variables with changing values)
    for cha in inputPassword:
        if cha in string.ascii_uppercase: # evaluates if there is any string uppercase letter (of cha) in inputPassword
            evalCapitalL+=1 # variable value 1 
        if cha in string.digits: # evaluates if there is any string digit (of cha) in inputPassword
            evalDigit+=1 # variable value 1
        if cha in string.punctuation: # evaluates if there is any string punctuation (of cha) in inputPassword
            evalSpecialCha+=1 # variable value 1

    if not evalCapitalL:
        print('The password should have at least \033[4m\033[33mone uppercase letter.\033[0m')  
        inputValue = False
    if not evalDigit:
        print('The password should have at least \033[4m\033[34mone numeral.\033[0m')
        inputValue = False
    if not evalSpecialCha:
        print('The password should have at least \033[4m\033[35mone special character except single quotation (!"#$%&()*+,-./:;<=>?@[\]^_`{|}~).\033[0m')
        inputValue = False
    elif inputValue:
        print('\033[46mOutput: \033[3mValid\033[00m')

header()  
print(validPassword.__doc__) # this will print the docstring indicated in the defined function
password = input('\033[91mInput:\033[00m ')
validPassword(password)


# another version (minimal)
from string import punctuation as p
def header():
    title = "**Password Validator**"
    print("*" * len(title)) # created a header design
    print(title)
    print("*" * len(title))

def passwordEval():
    """\033[4mEvaluate if the input is valid as a password.\033[0m

    These are the conditions need to be met:
    if its greater than \033[3m\033[32m15 characters\033[0m;
    if it has at least \033[3m\033[34mone uppercase letter\033[0m;
    if it has at least \033[3m\033[35mone numeral\033[0m; and
    if it has any of the \033[3m\033[36mspecial characters (!#$%&()*+,-./:;<=>?@[\]^_{|}~)\033[0m.
    """      
    password = input('\033[1m\033[33mInput:\033[0m ')
    initial = [0, 0, 0] # initialization (for creating variables with changing values)
    for cha in password:
        if cha.isupper():
            initial[0] = 123456789
        elif cha in p:
            initial[1] = 123456789
        elif cha.isdigit():
            initial[2] = 123456789
    print('\033[3m\033[31mOutput:\033[0m \033[4mValid\033[0m') if len(password) > 15 and 0 not in initial else print('\033[3m\033[31mOutput:\033[0m \033[4mInvalid\033[0m')

header()
print(passwordEval.__doc__)
passwordEval()