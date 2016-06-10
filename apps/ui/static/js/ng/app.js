var cashmanApp = angular.module('cashmanApp', ['infinite-scroll', 'ngAnimate', 'ngTouch','ui.filters', 'AxelSoft','angularLazyImg', 'ngSanitize', 'LocalStorageModule']);

//'ui.filters', 'AxelSoft' - Used for autocomplete selectbox

cashmanApp.service('LoadingInterceptor', ['$q', '$rootScope', '$log',
function ($q, $rootScope, $log) {
    'use strict';

    var xhrCreations = 0;
    var xhrResolutions = 0;

    function isLoading() {
        return xhrResolutions < xhrCreations;
    }

    function updateStatus() {
        $rootScope.loading = isLoading();
        if($rootScope.loading){
            $("#spinner").show();
        }
        else{
            $("#spinner").hide();
        }
    }

    return {
        request: function (config) {
            xhrCreations++;
            updateStatus();
            return config;
        },
        requestError: function (rejection) {
            xhrResolutions++;
            updateStatus();
            //$log.error('Request error:', rejection);
            return $q.reject(rejection);
        },
        response: function (response) {
            xhrResolutions++;
            updateStatus();
            return response;
        },
        responseError: function (rejection) {
            xhrResolutions++;
            updateStatus();
            //$log.error('Response error:', rejection);
            return $q.reject(rejection);
        }
    };
}]);

cashmanApp.config(['$httpProvider', function($httpProvider) {
    $httpProvider.interceptors.push('LoadingInterceptor');
}]);


//image lazyload configuration
cashmanApp.config(['lazyImgConfigProvider', function (lazyImgConfigProvider) {
    lazyImgConfigProvider.setOptions({
        offset: 1000, // how early you want to load image (default = 100)
        onSuccess: function (image) {},
    });
}]);

//this is the directive will be used when you want to do something after ng-repet rendering is completed.
/*
USAGE:
            1. Define the directive(below)

            2. inside controller:
			        $scope.$on('ngRepeatFinished', function (ngRepeatFinishedEvent) {
			            //your code to execute when rendering completed
			        });

            3. In your HTML code:( on-finish-render="ngRepeatFinished")
                     <li class="list-group-item" ng-repeat="certComment in certComments" on-finish-render="ngRepeatFinished">

*/
cashmanApp.directive('onFinishRender', function ($timeout) {
        return {
            restrict: 'A',
            link: function (scope, element, attr) {
                if (scope.$last === true) {
                    $timeout(function () {
                        scope.$emit('ngRepeatFinished');
                    });
                }
            }
        }
});

// Click to navigate
// e.g. <div link-click="/user-certificate-detail/?sku={{certificate.sku}}">
cashmanApp.directive('linkClick', [function() {
    return {
        link: function(scope, element, attrs) {
            element.on('click', function() {
                scope.$apply(function() {
                    //$location.path(attrs.clickLink);//to append after
                    window.location.href = attrs.linkClick;
                });
            });
        }
    }
}]);


 cashmanApp.directive('onlyNumber', function () {
    return {
      restrict: 'EA',
        require: 'ngModel',
        link: function (scope, element, attrs, ngModel) {
           scope.$watch(attrs.ngModel, function(newValue, oldValue) {
              var spiltArray = String(newValue).split("");

              if(attrs.allowNegative == "false") {
                if(spiltArray[0] == '-') {
                  newValue = newValue.replace("-", "");
                  ngModel.$setViewValue(newValue);
                  ngModel.$render();
                }
              }

              if(attrs.allowDecimal == "false") {
                  newValue = parseInt(newValue);
                  ngModel.$setViewValue(newValue);
                  ngModel.$render();
              }

              if(attrs.allowDecimal != "false") {
                if(attrs.decimalUpto) {
                   var n = String(newValue).split(".");
                   if(n[1]) {
                      var n2 = n[1].slice(0, attrs.decimalUpto);
                      newValue = [n[0], n2].join(".");
                      ngModel.$setViewValue(newValue);
                      ngModel.$render();
                   }
                }
              }


              if (spiltArray.length === 0) return;
              if (spiltArray.length === 1 && (spiltArray[0] == '-' || spiltArray[0] === '.' )) return;
              if (spiltArray.length === 2 && newValue === '-.') return;

                /*Check it is number or not.*/
                if (isNaN(newValue)) {
                    ngModel.$setViewValue(oldValue || '');
                    ngModel.$render();
                }
            });
        }
    };
});

/*
* Angular directive for jQuery lazy load plugin used in project
* Plugin : http://www.appelsiini.net/projects/lazyload
* */
cashmanApp.directive('lazySrc', [
  function() {
    'use strict';

    return {
      restrict: 'A',
      scope: {
        lazySrc: '@',
        effect: '@',
        event: '@',
        threshold: '@',
      },
      compile: function(element, attrs) {

        return {
          pre: function preLink(scope, iElement, iAttrs, controller) {
            iElement.attr('data-original', scope.lazySrc);
            //iElement.attr('style', 'background-image:url(\'' + scope.imgLazyBg + '\')');
          },
          post: function link(scope, element, attrs) {
            element.lazyload({
              effect: scope.effect || "fadeIn",
              event: scope.event,
              threshold:  scope.threshold || 200,
              container: $(".content-area")
            });

            if (scope.event) {
              scope.$on(scope.event, function(data) {
                element.trigger(scope.event);
              });
            }
          }
        };
      }
    };
  }
]);


/*
* Capitalize first letter of the textbox
* Example Usage :  <input type="text" ng-model="name" capitalize-first>
* */
cashmanApp.directive('capitalizeFirst', function($parse) {
   return {
     require: 'ngModel',
     link: function(scope, element, attrs, modelCtrl) {
        var capitalize = function(inputValue) {
           if (inputValue === undefined) { inputValue = ''; }
           var capitalized = inputValue.charAt(0).toUpperCase() +
                             inputValue.substring(1);
           if(capitalized !== inputValue) {
              modelCtrl.$setViewValue(capitalized);
              modelCtrl.$render();
            }
            return capitalized;
         }
         modelCtrl.$parsers.push(capitalize);
         capitalize($parse(attrs.ngModel)(scope)); // capitalize initial value
     }
   };
});

cashmanApp.config(function (localStorageServiceProvider) {
  localStorageServiceProvider
    .setPrefix('cashman')
    .setStorageType('sessionStorage')
    .setNotify(true, true)
});
