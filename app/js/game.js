'use strict';


// Declare app level module which depends on filters, and services
angular.module('game', ['game.filters', 'game.services', 'game.directives']).
  config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/hand', {templateUrl: 'partials/hand.html', controller: GameCtrl});
    $routeProvider.when('/judge', {templateUrl: 'partials/judge.html', controller: JudgeCtrl});
    $routeProvider.otherwise({redirectTo: '/'});
  }]);
