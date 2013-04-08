from google.appengine.ext import db
from google.appengine.ext.db import polymodel


class Game(db.Model):
  '''Represents an active Oh The Humanity game.'''

  player_turn = db.IntegerProperty(default = 0)


class Player(db.Model):
  '''Represents an active Oh The Humanity game.'''

  user = db.UserProperty()
  cards = db.ListProperty(long)
  played_cards = db.ListProperty(long)
  score = db.IntegerProperty(default = 0)


def load_cards(path):
  id_ctr = 0
  cards = []
  with open(path, 'r') as f:
    for line in f:
      cards.append(Card(id_ctr, line.rstrip()))
      id_ctr += 1
  return cards


class Card:
  '''Card read in from a file at runtime, rather than a DB'''

  def __init__(self, id, text):
    self.id = id
    self.text = text

  def num_answers(self):
    '''Returns the number of answers spots for a black question card.

    This is equal to the number of underscores in the question text.
    '''
    return self.text.count("_")

  def __str__(self):
    return '%s: %s' % (self.id, self.text)

  def __repr__(self):
    return self.__str__()

  def dict(self):
    '''Aids JSON serialization'''
    return {
      "id": self.id,
      "text": self.text,
      "num_answers": self.num_answers()
    }


class BlackCards:
  '''Question Card'''
  cards = []

  @staticmethod
  def get():
    '''Load all black cards'''
    if not BlackCards.cards:
      BlackCards.cards = load_cards("data/black")
    return BlackCards.cards


class WhiteCards:
  '''Answer Card'''
  cards = []

  @staticmethod
  def get():
    '''Get all white cards'''
    if not WhiteCards.cards:
      WhiteCards.cards = load_cards("data/white")
    return WhiteCards.cards

