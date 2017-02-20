import webapp

class urlaleat(webapp.webApp):

    def process(self, parsedRequest):
        import random
        num = random.randint(1,1000000)

        return ("200 OK", "<html><body><h1><a href='" + str(num) + "'>Dame mas</h1></body></html>")

if __name__ == "__main__":
    testWebApp = urlaleat("localhost", 1234)
