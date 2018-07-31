from google.appengine.ext import ndb

class Player(ndb.Model):
    save_player_name = ndb.StringProperty(required=True)

    
