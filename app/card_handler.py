import json
import webapp2
from models import BlackCards, WhiteCards

class CardHandler(webapp2.RequestHandler):
  '''Available white and black cards for clients.'''

  def get(self):
    cards = {
      "white_cards": list(card.dict() for card in WhiteCards.get()),
      "black_cards": list(card.dict() for card in BlackCards.get())
    }
    self.response.content_type = "application/x-javascript";
    self.response.write(json.dumps(cards))


app = webapp2.WSGIApplication([
  ('/card.json', CardHandler)
], debug=True)

