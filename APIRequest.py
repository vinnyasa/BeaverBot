
# Description: Wolfram Integration
# Author: Beaver Pack
# Jan 5, 2017

import wikipedia
import wolframalpha

class APIRequest:

    def fetchWolfram(self, input):
        # request to api
        client = wolframalpha.Client("W7R5JE-T5TL7U6P8V")  # hide this.

        response = client.query(input)

        # show answer
        print next(response.results).text

    def fetchWikipedia(self, input):
        # show result
        print wikipedia.summary(input)

    def getResponse(self):
        while True:
            input = raw_input("How can I help? ")

            try:
                # wolframalpha
                self.fetchWolfram(input)
            except ValueError:
                # wikipedia
                self.fetchWikipedia(input)

apiRequest = APIRequest()
apiRequest.getResponse()
