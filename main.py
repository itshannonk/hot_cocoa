# AI or You main python file
# import libraries
import webapp2
import jinja2
import os
import json

# Create Jinja environment templates
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# FUNCTIONS
# convert text into json# JSON maker function
def makeJSON(string):
    js_value = json.dumps(string)
    js_value = (json.dumps(string)
    .replace(u'<', u'\\u003c')
    .replace(u'>', u'\\u003e')
    .replace(u'&', u'\\u0026')
    .replace(u"'", u'\\u0027'))
    return string

# First game page
class StartGame(webapp2.RequestHandler):
    def get(self):
        # Link Handler to webpage
        MainPageTemp = JINJA_ENVIRONMENT.get_template('templates/startgame.html')
        sentence = makeJSON('it\'s shannon')

        # Render page using template
        self.response.write(MainPageTemp.render(sentence=sentence))

    def post(self):
        MainPageTemp = JINJA_ENVIRONMENT.get_template('templates/startgame.html')

        username = self.request.get('username')

        the_variable_dict = {'playerName': username}

        self.response.write(MainPageTemp.render(the_variable_dict))

# Introduction Page
class Introduction(webapp2.RequestHandler):
    def get(self):
        Template = JINJA_ENVIRONMENT.get_template('templates/introduction.html')
        self.response.write(Template.render())

# Second game page
class Entrance(webapp2.RequestHandler):
    def get(self):
        # Link Handeler to webpage
        SecPageTemp = JINJA_ENVIRONMENT.get_template('templates/entrance.html')

        # Render page using template
    def post(self):
        SecPageTemp = JINJA_ENVIRONMENT.get_template('templates/entrance.html')

        self.response.write(SecPageTemp.render())

# Third game page
class Watson(webapp2.RequestHandler):
    def get(self):
        # Link Handler to webpage
        ThirdPageTemp = JINJA_ENVIRONMENT.get_template('templates/watson.html')

        # Render page using template
        self.response.write(ThirdPageTemp.render())

class Searching(webapp2.RequestHandler):
    def get(self):
        # Link Handler to webpage
        FourthPageTemp = JINJA_ENVIRONMENT.get_template('templates/searching.html')

        # Render page using template
        self.response.write(FourthPageTemp.render())

class Confront(webapp2.RequestHandler):
    def get(self):
        # Link Handler to webpage
        FifthPageTemp = JINJA_ENVIRONMENT.get_template('templates/confront.html')

        # Render page using template
        self.response.write(FifthPageTemp.render())

class Gameover(webapp2.RequestHandler):
    def get(self):
        # Link Handler to webpage
        GameoverTemp = JINJA_ENVIRONMENT.get_template('templates/gameover.html')
        self.response.write(GameoverTemp.render())
        # Render page using template
    def post(self):
        GameoverTemp = JINJA_ENVIRONMENT.get_template('templates/gameover.html')

        self.response.write(GameoverTemp.render())

class Win(webapp2.RequestHandler):
    def get(self):
        # Link Handler to webpage
        WinTemp = JINJA_ENVIRONMENT.get_template('templates/winpage.html')
        self.response.write(WinTemp.render())
        # Render page using template
    def post(self):
        WinTemp = JINJA_ENVIRONMENT.get_template('templates/winpage.html')

        self.response.write(WinTemp.render())

# Intitialize webpages:
app = webapp2.WSGIApplication([
    ('/', StartGame),
    ('/introduction', Introduction),
    ('/entrance', Entrance),
    ('/confront', Confront),
    ('/gameover', Gameover),
    ('/winpage', Win),
], debug=True)
