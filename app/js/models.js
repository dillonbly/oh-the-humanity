'use strict';

var oth = oth || {};

/**
 * @param {string} title
 * @param {number=} opt_id
 * @param {string=} opt_description
 * @constructor
 */
oth.BlackCard = function(title, opt_id, opt_description) {
  this.title = title;
  this.blanks = title.split('_').length - 1;
  this.id = opt_id;
  this.description = opt_description;
};
/**
 * @param {string} title
 * @param {number=} opt_id
 * @param {string=} opt_description
 * @constructor
 */
oth.WhiteCard = function(title, opt_id, opt_description) {
  this.title = title;
  this.id = opt_id;
  this.description = opt_description;
};

/**
 * @param {oth.BlackCard} blackCard
 * @param {...oth.WhiteCard} var_args
 * @constructor
 */
oth.Play = function(blackCard, var_args) {
  this.blackCard = blackCard;
  this.cards = angular.copy(Array.prototype.slice.call(arguments, 0));
  this.cards.shift();
  if(this.blackCard.blanks > this.cards.length) {
    throw 'Mismatch: Cards required for play. Expected ' +
          this.blackCard.blanks + ', received ' + this.cards.length;
  }
};
oth.Play.prototype.render = function() {
  var result = this.blackCard.title;
  angular.forEach(this.cards, function(card) {
    result = result.replace(
        '_', '<span class="oth-replacement">' + card.title + '</span>');
  });
  return result;
};
