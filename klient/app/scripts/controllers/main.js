'use strict';

/**
 * @ngdoc function
 * @name klientApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the klientApp
 */
angular.module('klientApp')
  .controller('MainCtrl', function ($scope) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
  });
