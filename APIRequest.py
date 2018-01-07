
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
        return next(response.results).text

    def fetchWikipedia(self, input):
        # show result
        return wikipedia.summary(input)

    def getResponse(self, query):
        try:
            # wolframalpha
            return self.fetchWolfram(query)

        except:
            # wikipedia
            return self.fetchWikipedia(query)




#apiRequest = APIRequest()
#answer = apiRequest.getResponse()

#print(answer)
#os.system("say the answer is  " + answer)


