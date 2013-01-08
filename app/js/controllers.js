'use strict';

/* Controllers */

function GameCtrl($scope, $location) {
  alert($location.search.token);
  channel = new goog.appengine.Channel($location.search.token);
  socket = channel.open();
  socket.onopen = console.log;
  socket.onmessage = console.log;
  socket.onerror = console.log;
  socket.onclose = console.log;
}
GameCtrl.$inject = [];

function JudgeCtrl($scope, $location) {
  alert("Judging");
}
JudgeCtrl.$inject = [];
