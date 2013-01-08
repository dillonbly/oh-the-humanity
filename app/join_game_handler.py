import json
import logging
import webapp2
from models import Player, Game

from google.appengine.api import channel
from google.appengine.api import users
from google.appengine.ext import db


class JoinGameHandler(webapp2.RequestHandler):
  '''Handles requests to join an active game. Adds the player to the list of players.'''

  def post(self):
    user = users.get_current_user()
    if not user:
      self.redirect(users.create_login_url("/"))
      return

    game_name = self.request.get('game_name')
    if not game_name:
      self.response.write('No game name specified')
      return

    game_key = db.Key.from_path('Game', game_name)
    game = db.get(game_key)

    if not game:
      game = Game(key_name=game_name)
      game.put()

    logging.info('Game: {0}'.format(game))

    player = Player(user=user, parent=game)
    player.put()

    token = channel.create_channel("{0}:{1}".format(game_name, user.user_id()))

    logging.info("/game#?gamename={0}&token={1}".format(game.key().id_or_name(), token))
    self.redirect("/game#?gamename={0}&token={1}".format(game.key().id_or_name(), token))


app = webapp2.WSGIApplication([
  ('/joingame', JoinGameHandler)
], debug=True)

