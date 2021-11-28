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
toBeCounted = toBeCounted.lower()
"""Convert input to lower case to lessen the if conditions read by the program
"""
for v in toBeCounted: # 97 = lowercase a; 101 = lowercase e; 105 = lowercase i; 111 = lowercase o; 117 = lowercase u; 122 = lowercase z
    if(ord(v) == 97 or ord(v) == 101 or ord(v) == 105
       or ord(v) == 111 or ord(v) == 117):
        vowel+=1
    elif(ord(v) >= 97 and ord(v) <= 122):
        consonant+=1
"""Utilization of American Standard Code for Information Interchange table to represent certain alphabets and minimize the program
"""
print("\033[00m\033[45mOutput:\033[00m")
print("\033[43mWord(s):\033[00m\033[93m", wordCount)
print("\033[00m\033[44mVowel(s):\033[00m\033[34m",vowel)
print("\033[00m\033[42mConsonant(s):\033[00m\033[92m",consonant)