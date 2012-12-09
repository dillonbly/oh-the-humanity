#!/usr/bin/env python

import json
import webapp2

from google.appengine.ext import db
from google.appengine.api import users


class CreateGameHandler(webapp2.RequestHandler):
  '''Handles requests to create a new game. Adds the player to the list of players.'''

  def post(self):
    user = users.get_current_user()
    if not user:
      self.response.write('You must be logged in to join a game')
      return

    game_name = self.request.get('game_name')
    if not game_name:
      self.response.write('No game name specified')
      return

    game = db.GqlQuery("SELECT * FROM Games WHERE name = :1", game_name).get()

    if game:
      self.response.write('Game already exists. Cannot create.')
      return

    game = Game(name=game_name)
    game.put()

    player = Player(user=user, game=game)
    player.put()

    self.response.redirect('/game.html#gameid={0}'.format(game.id()))

app = webapp2.WSGIApplication([
  ('/creategame', CreateGameHandler),
], debug=True)
