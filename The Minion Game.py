
# HackerRank Practice
#
# This function takes an input string and prints the 
# name and score of winner.
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.

def minion_game(string):
   kevin = stuart = indx = 0
   vowels = "AEIOU"
   for letter in string:
    indx += 1
    if letter in vowels:
        kevin += len(string) -  indx + 1
    else:
       stuart += len(string) - indx + 1
   if kevin == stuart:
    print("Draw")
   else:
    print("Kevin" if kevin > stuart  else "Stuart", max(kevin, stuart))

s = input()
minion_game(s)