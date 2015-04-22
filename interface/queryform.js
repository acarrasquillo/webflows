var app = angular.module('QueryForm', []);

app.controller('FormCtrl', function($scope){
	$scope.ipv4pattern = /^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/
	$scope.logicOptions = ['none','and','or'];
	$scope.result = [];
	$scope.ipValues = {
		srcaddr : null,
		dstaddr : null,
		logic: $scope.logicOptions[0]
	};
	$scope.portValues = {
		srcport : null,
		dstport : null,
		logic: $scope.logicOptions[0]
	};
	$scope.otherValues = {
		nexthop: null,
		output: null,
		input: null,
		dPkts: null,
		dOctets: null,
		first: null,
		last: null,
		tcp_flags: null,
		prot: null
	};
	$scope.showField = {
		srcaddr: false,
		dstaddr: false,
		ipLogic: false,
		srcport: false,
		dstport: false,
		portLogic: false,
		nexhop: false,
		output: false,
		input: false,
		dPkts: false,
		dOctets: false,
		first: false,
		last: false,
		tcp_flags: false,
		prot: false
	}; 
});

app.filter('arrayDiff', function(){
	return function(array,diff){

		var i, item,
		newArray = [],
		exception = Array.prototype.slice.call(arguments,2);

		for (i=0; i < array.length; i++){

			item = array[i];
			if (diff.indexOf(item) < 0 || exception.indexOf(item) >= 0){
				newArray.push(item);
			}
		}

		return newArray;
	};
	
});