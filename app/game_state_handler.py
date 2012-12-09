import json
import logging
import webapp2


class GameStateHandler(webapp2.RequestHandler):
  '''Handles requests for a player to download the current game state.'''

  def get(self):
    game_name = self.request.get('game_name')

    game_key = db.Key.from_path('Game', game_name)
    game = db.get(game_key)
    logging.info('Found game: {0}'.format(game))

    players = []
    current_hand = []
    gamestate = {
      "players": players,
      "current_hand": current_hand,
      "player_turn": 1
    }

    self.response.write(json.dumps(gamestate))


app = webapp2.WSGIApplication([
  ('/gamestate', GameStateHandler)
], debug=True)
