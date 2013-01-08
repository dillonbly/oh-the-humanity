'use strict';

/* Controllers */

function GameController($scope, $location) {
  var channel = new goog.appengine.Channel($location.search().token);
  var socket = channel.open();
  socket.onopen = function() { console.log('Channel opened'); }
  socket.onmessage = function(m) { console.log('Message: ' + m ); };
  socket.onerror = function(err) { console.log('Error: ' + err ); };
  socket.onclose = function() { console.log('Channel closed'); };
}
GameController.$inject = ["$scope", "$location"];


function JudgeController($scope, $location) {
  alert("Judging");
}
JudgeController.$inject = ["$scope", "$location"];


function HandController() {
  alert("Hand");
}
HandController.$inject = [];
