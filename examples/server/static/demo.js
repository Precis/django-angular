
(function(angular, undefined) {
'use strict';

angular.module('djangular-demo', ['ngResource', 'ng.django.forms']).
config(function($httpProvider) {
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
}).
factory('SimpleModel', function ($resource) {
    return $resource('/crud/simplemodel', {'pk': '@pk'}, {});
}).
controller('SimpleFormCtrl', function($scope, djangoForm, SimpleModel) {
    $scope.subscribe_data = new SimpleModel();
    $scope.submit_result = undefined;
    $scope.submit = function() {
        $scope.subscribe_data.$save(
            function(out_data) {
                // Success.
                $scope.submit_result = 'Submit succeeded!';
            },
            function(out_data) {
                // Failure.
                $scope.submit_result = 'Submit failed - server responded: ' + out_data.data.message;
                djangoForm.setErrors($scope.simple_form, out_data.data.detail);
            }
        );
    }
});

})(window.angular);
