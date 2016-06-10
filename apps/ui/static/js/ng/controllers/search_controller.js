/**
 * Created by hardik on 27-11-2015.
 */

var searchPage = angular.module("searchPage", ['cashmanApp']);

searchPage.controller("SearchPageController",

    function ($scope, $http, localStorageService) {
        // Check if cookie exists or redirect to home page otherwise
        $scope.team_id = localStorageService.cookie.get('team_id')
        if ($scope.team_id == null){
            localStorageService.cookie.clearAll()
            window.location.href = '/'
        }

        // Load game list to select menu
        $scope.url = '/api/games/games/?team=' + $scope.team_id;
        var url = $scope.url;
        $http.get(url).success(function (data) {
            $scope.games = data;
        });

        /*
        Function to take user to home page selecting team (Venue)
         */
        $scope.goToHome = function() {
            $scope.team_id = localStorageService.cookie.remove('team_id');
            window.location.href = '/'
        }


        /*
        Function to set cookie for selected game and to get gallery list for same game
         */
        $scope.selectGame = function() {
            url = '/api/games/galleries/?game=' + $scope.selected_game.id;
            $http.get(url).success(function (data) {
                $scope.galleries = data;
            });
            localStorageService.cookie.set('game_id', $scope.selected_game.id);
            localStorageService.cookie.set('game', $scope.selected_game.gdate);
        }


        /*
        Function to save cookies for selected gallery and redirect to photos' listing page.
         */
        $scope.findPhotos = function(){
            localStorageService.cookie.set('image_set_id', $scope.selected_gallery.ImageSetID);
            localStorageService.cookie.set('barcode', $scope.selected_gallery.Barcode);
            window.location.href = '/cashman/photos'
        }

    }
);
