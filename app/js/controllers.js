'use strict';

/* Controllers */

function GameController($scope, $location, $http, Cards) {
  var channel = new goog.appengine.Channel($location.search().token);
  var socket = channel.open();
  $scope.cards = Cards.cards();
  socket.onopen = function() { console.log('Channel opened'); }
  socket.onmessage = function(m) { console.log('Message: ' + m ); };
  socket.onerror = function(err) { console.log('Error: ' + err ); };
  socket.onclose = function() { console.log('Channel closed'); };
  $scope.endTurn = function() {
    $http.post('/playmove?game_name=test&move_type=PlayCards')
        .success(function(response) {
          console.log('Cards played');
        });
  };
}


function JudgeController($scope, $location) {
  alert("Judging");
}


function HandController() {
  alert("Hand");
}
