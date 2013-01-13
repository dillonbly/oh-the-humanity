'use strict';


// Declare app level module which depends on filters, and services
angular.module(
  'game',
  ['game.filters', 'game.services', 'game.directives'],
  function($routeProvider, $locationProvider) {
    $routeProvider.when('/game', {templateUrl: 'partials/game.html', controller: GameController});
    $routeProvider.when('/hand', {templateUrl: 'partials/hand.html', controller: HandController});
    $routeProvider.when('/judge', {templateUrl: 'partials/judge.html', controller: JudgeController});
    $routeProvider.otherwise({redirectTo: '/'});

    // No need for hashtag in URLs.
    $locationProvider.html5Mode(true);
  });
