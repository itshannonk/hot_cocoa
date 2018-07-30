# AI or You main python file
import webapp2
import jinja2

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
], debug=True)
