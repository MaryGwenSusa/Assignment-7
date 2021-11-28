import string
title = "**ALPHA INPUT COUNTER (Words, Vowels, Consonants)**"
print("*" * len(title)) # created a header design
print(title)
print("*" * len(title))

toBeCounted = input("\033[42mInput:\033[00m\033[36m ")
if toBeCounted == None or toBeCounted == "": # input validation-- to make sure there is an input
    raise Exception("\033[41mThe input is empty.\033[00m")

wordCount = sum([w.strip(string.punctuation).isalpha() for w in toBeCounted.split()])
# string.punctuation = (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)
"""The punctuations/special characters/digits in toBeCounted string input will be stripped and confirmed to be alphabets.
All stripped w's will then be split into a list in a loop which will be summed up
"""

vowel = consonant = 0 # initializations (for creating variables with changing values)
