# AI or You main python file
import webapp2
import jinja2
import os

# Create Jinja environment templates
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# First game page
class MainPage(webapp2.RequestHandler):
    def get(self):
        # Link Handler to webpage
        MainPageTemp = JINJA_ENVIRONMENT.get_template('templates/game1.html')

        self.response.write(MainPageTemp.render())

# Second game page
class Entrance(webapp2.RequestHandler):
    def get(self):
        # Link Handeler to webpage
        SecPageTemp = JINJA_ENVIRONMENT.get_template('templates/game2.html')

        # Render page using template
        self.response.write(SecPageTemp.render())

# Third game page
class Watson(webapp2.RequestHandler):
    def get(self):
        # Link Handler to webpage
        ThirdPageTemp = JINJA_ENVIRONMENT.get_template('templates/game3.html')

        # Render page using template
        self.response.write(ThirdPageTemp.render())

class Searching(webapp2.RequestHandler):
    def get(self):
        # Link Handler to webpage
        FourthPageTemp = JINJA_ENVIRONMENT.get_template('templates/game4.html')

        # Render page using template
        self.response.write(FourthPageTemp.render())

class Searching(webapp2.RequestHandler):
    def get(self):
        # Link Handler to webpage
        FifthPageTemp = JINJA_ENVIRONMENT.get_template('templates/game5.html')

        # Render page using template
        self.response.write(FifthPageTemp.render())

# Intitialize webpages:
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/entrance', Entrance),
    ('/watson', Watson),
    ('/searching', Searching),
    ('/confront', Confront),
], debug=True)
