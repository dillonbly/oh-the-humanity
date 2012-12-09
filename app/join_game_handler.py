import json
import webapp2
from models import Player, Game

from google.appengine.ext import db
from google.appengine.api import users


class JoinGameHandler(webapp2.RequestHandler):
  '''Handles requests to join an active game. Adds the player to the list of players.'''

  def post(self):
    user = users.get_current_user()
    #if not user:
    #  self.response.write('You must be logged in to join a game')
    #  return

    game_name = self.request.get('game_name')
    if not game_name:
      self.response.write('No game name specified')
      return

    game = db.GqlQuery("SELECT * FROM Games WHERE name = :1", game_name).get()

    if not game:
      self.response.write('Game not found')
      return
 
    # TODO(dillonbly): Detect if the user is joining a second time.
    player = Player(user=user, game=game)
    player.put()

    self.response.redirect('/game.html#gameid=%s'.format(game.id()))
 
app = webapp2.WSGIApplication([
  ('/joingame', JoinGameHandler)
], debug=True)
