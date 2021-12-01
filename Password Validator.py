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