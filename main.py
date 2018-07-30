import webapp2


# First game page
class MainPage(webapp2.RequestHandler):
    def get(self):
        #stuff

# Second game page
class MainPage(webapp2.RequestHandler):
    def get(self):
        #stuff

# Third game page
class MainPage(webapp2.RequestHandler):
    def get(self):
        #stuff

# FOurth game page
class MainPage(webapp2.RequestHandler):
    def get(self):
        #stuff

# Intitialize webpages:
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/section2', SecondPage),
    ('/section3', ThirdPage),
    ('/section4', FourthPage),
], debug=True)
