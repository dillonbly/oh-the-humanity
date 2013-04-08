import json
import logging
import webapp2
from google.appengine.api import channel
from google.appengine.api import users


class GameStateHandler(webapp2.RequestHandler):
  '''Handles requests for a player to download the current game state.'''

  def get(self):
    game_name = self.request.get('game_name')

    game_key = db.Key.from_path('Game', game_name)
    game = db.get(game_key)
    user = users.get_current_user()
    logging.info('Player {0} connecting to game: {1}'.format(game, user.nickname())

    token = channel.create_channel("{0}:{1}".format(game_name, user.user_id()))

    players = Player.all().ancestor(game).run()
    for player in players:
      if player.user == user:
        this_player = player

    if not this_player:
      raise Exception("Player not found: {0}".format(user.nickname()))

    gamestate = {
      "players": players,
      "current_hand": this_player.cards,
      "player_turn": game.player_turn
    }

    self.response.write(json.dumps(gamestate))


app = webapp2.WSGIApplication([
  ('/gamestate', GameStateHandler)
], debug=True)
