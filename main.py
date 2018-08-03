# AI or You main python file
# import libraries
import webapp2
import jinja2
import os

# Create Jinja environment templates
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# First game page
class StartGame(webapp2.RequestHandler):
    def get(self):
        # Link Handler to webpage
        MainPageTemp = JINJA_ENVIRONMENT.get_template('templates/startgame.html')

        # Render page using template
        self.response.write(MainPageTemp.render())

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
class Confront(webapp2.RequestHandler):
    def get(self):
        # Link Handler to webpage
        ThirdPageTemp = JINJA_ENVIRONMENT.get_template('templates/confront.html')

        # Render page using template
        self.response.write(ThirdPageTemp.render())

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

class Credits(webapp2.RequestHandler):
    def get(self):
        # Link Handler to webpage
        FinalTemp = JINJA_ENVIRONMENT.get_template('templates/credits.html')
        self.response.write(FinalTemp.render())
        # Render page using template
    def post(self):
        FinalTemp = JINJA_ENVIRONMENT.get_template('templates/credits.html')

        self.response.write(FinalTemp.render())

# Intitialize webpages:
app = webapp2.WSGIApplication([
    ('/', StartGame),
    ('/introduction', Introduction),
    ('/entrance', Entrance),
    ('/confront', Confront),
    ('/gameover', Gameover),
    ('/winpage', Win),
    ('/credits', Credits),
], debug=True)
