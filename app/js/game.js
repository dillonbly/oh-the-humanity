'use strict';


// Declare app level module which depends on filters, and services
angular.module('game', ['game.filters', 'game.services', 'game.directives']).
  config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/game', {templateUrl: 'html/game.html', controller: GameController});
    $routeProvider.when('/hand', {templateUrl: 'partials/hand.html', controller: HandController});
    $routeProvider.when('/judge', {templateUrl: 'partials/judge.html', controller: JudgeController});
    $routeProvider.otherwise({redirectTo: '/'});
  }]);
