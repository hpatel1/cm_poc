

var imagesPage = angular.module("imagesPage", []);

imagesPage.controller("imagesPageController",

    function ($scope, $http) {
        
        // Load photos list with thumb URLS
        $scope.url = '/api/catalog/images/';
        var url = $scope.url;
        $http.get(url).success(function (data) {            
            $scope.photos = data.results;
        });
        // Function to get images.
        $scope.getImages = function(){
            window.location.href = '/cashman/displayAll'
        }

    }
);
