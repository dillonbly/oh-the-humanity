'use strict';

/* Controllers */

function GameController($scope, $location, Cards) {
  var channel = new goog.appengine.Channel($location.search().token);
  var socket = channel.open();
  $scope.cards = Cards.cards();
  socket.onopen = function() { console.log('Channel opened'); }
  socket.onmessage = function(m) { console.log('Message: ' + m ); };
  socket.onerror = function(err) { console.log('Error: ' + err ); };
  socket.onclose = function() { console.log('Channel closed'); };
}


function JudgeController($scope, $location) {
  alert("Judging");
}


function HandController() {
  alert("Hand");
}
