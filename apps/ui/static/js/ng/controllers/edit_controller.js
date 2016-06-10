/**
 * Created by hardik on 27-11-2015.
 */

var editPage = angular.module("editPage", ['cashmanApp']);

editPage.controller("editPageController",

    function ($scope, $http, localStorageService) {
        // Check if cookie exists or redirect to home page otherwise
        $scope.venue_id = localStorageService.cookie.get('venue_id');
        $scope.image_set_id = localStorageService.cookie.get('image_set_id');

        if ($scope.venue_id == null || $scope.image_set_id == null){
            localStorageService.cookie.clearAll();
            window.location.href = '/'
        }

        $scope.selectedPhotos = localStorageService.cookie.get('selected_photos');
        if ($scope.selectedPhotos == null){
            $scope.selectedPhotos = [];
        }

        // Load photos list with thumb URLS
        $scope.url = '/api/games/images/?image_set=' + $scope.image_set_id;
        var url = $scope.url;
        $http.get(url).success(function (data) {
            $scope.photos = data;
        });


        //Function to take user to home page selecting team (Venue)
        $scope.changeTeam = function() {
            localStorageService.cookie.clearAll();
            window.location.href = '/'
        }


        /*
        Function to create list of selected photos
         */
        $scope.select_photo = function(photo){
            var idx = $scope.selectedPhotos.indexOf(photo)
            if(idx != -1){
                $scope.selectedPhotos.splice(idx,1);
            }else {
                $scope.selectedPhotos.push(photo);
            }
            localStorageService.cookie.set('selected_photos', $scope.selectedPhotos);
            console.log($scope.selectedPhotos);
        };

        // Proceed to editing photos and then checkout
        $scope.edit_photos = function(){
            console.log("Hello");
            window.location.href = '/cashman/product';
        };


    }
);
