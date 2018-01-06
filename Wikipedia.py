# Description: Wikipedia Integration
# Author: Beaver Pack
# Jan 5, 2017


import wikipedia

def fetchWikipedia():
    # promp user
    input = raw_input("What can we learn about today? ")

    # show result
    print wikipedia.summary(input)


#fetchWikipedia()