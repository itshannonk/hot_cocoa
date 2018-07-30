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

        dicti = {'number': 0}
        for i in range(5):
            dicti['number'] = i
            # Render page using template
            self.response.write(MainPageTemp.render(dicti))

# Second game page
class SecondPage(webapp2.RequestHandler):
    def get(self):
        # Link Handeler to webpage
        SecPageTemp = JINJA_ENVIRONMENT.get_template('templates/game2.html')

        # Render page using template
        self.response.write(SecPageTemp.render())

# Third game page
class ThirdPage(webapp2.RequestHandler):
    def get(self):
        # Link Handler to webpage
        ThirdPageTemp = JINJA_ENVIRONMENT.get_template('templates/game3.html')

        # Render page using template
        self.response.write(ThirdPageTemp.render())




# Intitialize webpages:
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/section2', SecondPage),
    ('/section3', ThirdPage),
], debug=True)
