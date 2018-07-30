import webapp2
import jinja2
import os
import json

# Create Jinja environment templates
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# JSON maker function
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
        sentence = 'is it finally working'

        sentence = makeJSON(sentence)
        # Render page using template
        self.response.write(MainPageTemp.render(sentence=sentence))
        print ('break')
