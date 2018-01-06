
# Description: Wolfram Integration
# Author: Beaver Pack
# Jan 5, 2017

import wikipedia
import wolframalpha

class APIRequest:

    def fetchWolfram(self):
        # promp user for a question

        input = raw_input("How can I help? ")
        # request to api
        client = wolframalpha.Client("W7R5JE-T5TL7U6P8V")  # hide this.

        response = client.query(input)

        # show answer
        print next(response.results).text

    def fetchWikipedia(self):
        # promp user
        input = raw_input("What can we learn about today? ")

        # show result
        print wikipedia.summary(input)

    def getResponse(self):

        try:
            # wolframalpha
            self.fetchWolfram()
        except:
            # wikipedia
            self.fetchWikipedia()

apiRequest = APIRequest()
apiRequest.getResponse()
