# AI or You main python file
import webapp2
import jinja2
import os

variable = True
# Create Jinja environment templates
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# First game page
    def get(self):
        # Link Handler to webpage
<<<<<<< HEAD
        MainPageTemp = JINJA_ENVIRONMENT.get_template('templates/game1.html')
        variable = False
        self.response.write(MainPageTemp.render())

# Second game page
class Entrance(webapp2.RequestHandler):
    def get(self):
        # Link Handeler to webpage

        # Render page using template
        self.response.write(SecPageTemp.render())

# Third game page
class Watson(webapp2.RequestHandler):
    def get(self):
        # Link Handler to webpage

        # Render page using template
        self.response.write(ThirdPageTemp.render())

class Searching(webapp2.RequestHandler):
    def get(self):
        # Link Handler to webpage

        # Render page using template
        self.response.write(FourthPageTemp.render())

class Confront(webapp2.RequestHandler):
    def get(self):
        # Link Handler to webpage

        # Render page using template
        self.response.write(FifthPageTemp.render())

# Intitialize webpages:
app = webapp2.WSGIApplication([
    ('/entrance', Entrance),
    ('/watson', Watson),
    ('/searching', Searching),
    ('/confront', Confront),
], debug=True)
