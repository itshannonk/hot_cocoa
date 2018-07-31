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

<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
class
>>>>>>> 48eec8e13206e03003c1f92b98419d748aafa929

dict_names = {'playerName': save_player_name,

<<<<<<< HEAD
>>>>>>> fde7ae323752633f6149aa554c7451440e7ec91b
=======
            }
=======


>>>>>>> master
>>>>>>> 48eec8e13206e03003c1f92b98419d748aafa929
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


# Second game page
class Entrance(webapp2.RequestHandler):
    def get(self):
        # Link Handeler to webpage
        SecPageTemp = JINJA_ENVIRONMENT.get_template('templates/entrance.html')

        # Render page using template
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

class Confront(webapp2.RequestHandler):
    def get(self):
        # Link Handler to webpage
        FifthPageTemp = JINJA_ENVIRONMENT.get_template('templates/game5.html')

        # Render page using template
        self.response.write(FifthPageTemp.render())

# Intitialize webpages:
app = webapp2.WSGIApplication([
    ('/startgame', StartGame),
    ('/entrance', Entrance),
    ('/watson', Watson),
    ('/searching', Searching),
    ('/confront', Confront),
], debug=True)
