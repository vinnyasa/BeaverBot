# Description: Wolfram Integration
# Author: Beaver Pack
# Jan 4, 2017

import wolframalpha

def  fetchWolfram():
    # promp user for a question
    input = raw_input("How can I help? ")

    # request to api
    client = wolframalpha.Client("W7R5JE-T5TL7U6P8V")  # hide this.

    response = client.query(input)

    # show answer
    print next(response.results).text

fetchWolfram()