# Description: Wolfram Integration
# Author: Beaver Pack
# Jan 4, 2017

import wolframalpha

    #promp user for a question
    input = raw_input("How can I help? ")

    #request from api
    client = wolframalpha.Client("W7R5JE-T5TL7U6P8V") #app_id can not be here, we need to hide this.

    response = client.query(input)

    #show answer
    print next(response.results).text


