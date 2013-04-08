'use strict';

/* Services */


angular.module('game.services', [])
  .factory('Cards', function($q, $http) {
    var cards = {'black_cards':[], 'white_cards':[]};
    var Cards = {};
    Cards.cards = function() { return cards; };
    $http.get('/card.json')
      .success(function(results, status, headers, config) {
        cards.black_cards = results.black_cards;
        cards.white_cards = results.white_cards;
      })
      .error(function(data, status, headers, config) {
        console.error(data);
      });
    return Cards;
  });

