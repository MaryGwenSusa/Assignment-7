
title = "**ALPHA INPUT COUNTER (Words, Vowels, Consonants)**"
print("*" * len(title)) # created a header design
print(title)
print("*" * len(title))

toBeCounted = input("\033[42mInput:\033[00m\033[36m ")
if toBeCounted == None or toBeCounted == "": # input validation-- to make sure there is an input
    raise Exception("\033[41mThe input is empty.\033[00m")