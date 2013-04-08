import json
import logging
import webapp2

from models import Player, Game

from google.appengine.api import channel
from google.appengine.api import users
from google.appengine.ext import db


class PlayMoveHandler(webapp2.RequestHandler):
  '''Handles move updates from players.

  Types of moves include:
  PlayCards
  FlipCards
  SelectWinner

  Each move will trigger a channel update for all players in the game.
  '''

  def post(self):
    game_name = self.request.get('game_name')
    game_key = db.Key.from_path('Game', game_name)
    game = db.get(game_key)
    user = users.get_current_user()
    logging.info('Player {0} playing move for game: {1}'.format(game, user.nickname()))

    move_type = self.request.get('move_type')
    selected_cards = self.request.get('selected_cards')

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

    for player in players:
      channel.send_message("{0}:{1}".format(game_name, player.user.user_id()),
        json.dumps(gamestate))


app = webapp2.WSGIApplication([
  ('/playmove', PlayMoveHandler)
], debug=True)
