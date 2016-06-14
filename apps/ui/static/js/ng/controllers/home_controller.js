/**
 * Created by hardik on 27-11-2015.
 */

var homePage = angular.module("homePage", ['cashmanApp']);

homePage.controller("HomePageController",

    function ($scope, $http, localStorageService) {
        $scope.teams = [];
        $scope.url = '/api/games/teams/';
        $scope.venue_selected = false;
        $scope.team_box_selected = false;
        $scope.overlay = false;
        $scope.gallery_box_selected = false;
        $scope.theme_class = 'gaints-theme';
        $scope.theme_mapping = {
            'BOS': 'redsox-theme',
            'CHC': 'ccubs-theme',
            'BAL': 'orioles-theme',
            'TBR': 'rays-theme',
            'KAN': 'kcroyals-theme',
            'SFG': 'gaints-theme',
            'LAA': 'angels-theme'
        }


        /*
        // To get dynamic list of Teams which are to be selected.
        var url = $scope.url;
        $http.get(url).success(function (data) {
            $scope.teams = data;
        });
        */

        // Find more memories
        $scope.find_memories = function(){
            if ($scope.venue_selected){
                $scope.theme_class = $scope.theme_mapping[$scope.venue_id];
                $scope.gallery_box_selected = true;
            }
            else {
                $scope.team_box_selected = true;
            }
            $scope.overlay = true;
        };


        // Event on venue selection
        $scope.getDetails = function(venue_id){
            $scope.venue_id = venue_id
            localStorageService.cookie.set('venue_id',venue_id);
            $scope.theme_class = $scope.theme_mapping[venue_id];
            $scope.team_box_selected = false;
            $scope.gallery_box_selected = true;

            // Load game list to select game menu
            $scope.get_games(venue_id);
        };

        // Get games according to selected Venue
        $scope.get_games = function(venue_id){
            $scope.venue_id = venue_id;
            var game_url = '/api/games/games/?venue=' + $scope.venue_id;
            $http.get(game_url).success(function (data) {
                $scope.games = data;
            });
        }


        // Close boxes
        $scope.close_box = function(){
            $scope.gallery_box_selected = false;
            $scope.team_box_selected = false;
            $scope.overlay = false;
        }

        // Switch Team
        $scope.switch_team = function(){
            $scope.gallery_box_selected = false;
            localStorageService.cookie.clearAll();
            $scope.team_box_selected = true;
        }

        // Function to take user to home page selecting team (Venue)
        $scope.goToHome = function() {
            localStorageService.cookie.clearAll();
        }



        // Function to set cookie for selected game and to get gallery list for same game
        $scope.selectGame = function() {
            url = '/api/games/galleries/?game=' + $scope.selected_game.id;
            $http.get(url).success(function (data) {
                $scope.galleries = data;
            });
            localStorageService.cookie.set('game_id', $scope.selected_game.id);
            localStorageService.cookie.set('game', $scope.selected_game.gdate);
        }


        // Function to save cookies for selected gallery and redirect to photos' listing page.
        $scope.findPhotos = function(){
            localStorageService.cookie.set('image_set_id', $scope.selected_gallery.ImageSetID);
            localStorageService.cookie.set('barcode', $scope.selected_gallery.Barcode);
            window.location.href = '/cashman/photos'
        }


        // Check if cookie exists or redirect to home page otherwise
        $scope.venue_id = localStorageService.cookie.get('venue_id')
        if ($scope.venue_id == null){
            localStorageService.cookie.clearAll()
        }
        else{
            $scope.venue_selected = true;
            $scope.theme_class = $scope.theme_mapping[$scope.venue_id];
            $scope.get_games($scope.venue_id);
        }

    }
);