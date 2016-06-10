/**
 * Created by hardik on 27-11-2015.
 */

var photosPage = angular.module("photosPage", ['cashmanApp']);

photosPage.controller("photosPageController",

    function ($scope, $http, localStorageService) {
        // Check if cookie exists or redirect to home page otherwise
        $scope.venue_id = localStorageService.cookie.get('venue_id');
        $scope.image_set_id = localStorageService.cookie.get('image_set_id');
        $scope.selectedPhotos = localStorageService.cookie.get('selected_photos');
        $scope.selected_game_id = localStorageService.cookie.get('game_id');

        // Get games according to selected Venue
        $scope.get_games = function(venue_id){
            $scope.venue_id = venue_id;
            var game_url = '/api/games/games/?venue=' + $scope.venue_id;
            $http.get(game_url).success(function (data) {
                $scope.games = data;
                len = $scope.games.length;
                for (var i = 0; i < len; i++) {
                    if ($scope.games[i].id == $scope.selected_game_id){
                        //console.log($scope.selected_game_id);
                        //console.log($scope.games[i]);
                        $scope.selected_game = $scope.games[i];
                    }
                }
                if ($scope.selected_game){
                    //console.log("Come here")
                    $scope.selectGame();
                }
            });
        }

        // Function to set cookie for selected game and to get gallery list for same game
        $scope.selectGame = function() {
            url = '/api/games/galleries/?game=' + $scope.selected_game.id;
            $http.get(url).success(function (data) {
                $scope.galleries = data;
                len = $scope.galleries.length;
                for (var i = 0; i < len; i++) {
                    if ($scope.galleries[i].ImageSetID == $scope.image_set_id){
                        //console.log($scope.image_set_id);
                        //console.log($scope.galleries[i]);
                        $scope.selected_gallery = $scope.galleries[i];
                    }
                }
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

        //Function to take user to home page selecting team (Venue)
        $scope.changeTeam = function() {
            localStorageService.cookie.clearAll();
            window.location.href = '/'
        }


        // Function to create list of selected photos
        $scope.select_photo = function(photo){
            var idx = $scope.selectedPhotos.indexOf(photo)
            if(idx != -1){
                $scope.selectedPhotos.splice(idx,1);
            }else {
                $scope.selectedPhotos.push(photo);
            }
            localStorageService.cookie.set('selected_photos', $scope.selectedPhotos);
            console.log($scope.selectedPhotos);
            $scope.photos_length = $scope.selectedPhotos.length;
        };

        // Proceed to editing photos and then checkout
        $scope.edit_photos = function(){
            console.log("Hello");
            window.location.href = '/cashman/product';
        };

        // Load games by calling function get_games
        $scope.get_games($scope.venue_id);

        if ($scope.venue_id == null || $scope.image_set_id == null){
            localStorageService.cookie.clearAll();
            window.location.href = '/'
        }

        if ($scope.selectedPhotos == null){
            $scope.selectedPhotos = [];
        }

        // Load photos list with thumb URLS
        $scope.url = '/api/games/images/?image_set=' + $scope.image_set_id;
        var url = $scope.url;
        $http.get(url).success(function (data) {
            $scope.photos = data;
            refresh_layout();
        });
    }
);

