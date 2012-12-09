from google.appengine.ext import db
from google.appengine.ext.db import polymodel


class Card(polymodel.PolyModel):
  '''A drawn card.'''

  text = db.StringProperty(required=True)


class BlackCard(Card):
  '''Question card'''
  pass


class WhiteCard(Card):
  '''Answer card'''
  pass


class Game(db.Model):
  '''Represents an active Oh The Humanity game.'''

  player_turn = db.IntegerProperty(default=0)


class Player(db.Model):
  '''Represents an active Oh The Humanity game.'''

  user = db.UserProperty()
  cards = db.ListProperty(long)
  played_cards = db.ListProperty(long)
  score = db.IntegerProperty(default=0)

