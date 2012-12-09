import json
import webapp2

class GameStateHandler(webapp2.RequestHandler):
  '''Handles requests for a player to download the current game state.'''

  def get(self):
    game_name = self.request.get('game_name')

    game = db.GqlQuery("SELECT * FROM Games WHERE name = :1", game_name).get()

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
