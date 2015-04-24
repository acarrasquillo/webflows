var app = angular.module('QueryForm', []);

app.controller('FormCtrl', function($scope,$http){
	
	// regexp for the ipv4 adresses
	$scope.ipv4pattern = /^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/;

	// fields logic options
	$scope.logicOptions = ['none','and','or'];

	// relations for numerical fields
	$scope.relationOptions= ['equal to','greater than','less than'];

	// records to save fields data
	$scope.ipValues = {
		srcaddr : null,
		dstaddr: null,
		logic: $scope.logicOptions[0]
	};
	$scope.portValues = {
		srcport : null,
		dstport: null,
		logic: $scope.logicOptions[0]
	};
	$scope.nexthopValue = {
		value: null
	};
	$scope.outputValue = {
		value: null,
		relational_op: $scope.relationOptions[0]
	};
	$scope.inputValue = {
		value: null,
		relational_op: $scope.relationOptions[0]
	};
	$scope.dPktsValue = {
		value: null,
		relational_op: $scope.relationOptions[0]
	};
	$scope.dOctetsValue = {
		value: null,
		relational_op: $scope.relationOptions[0]
	};
	$scope.firstValue = {
		value: null,
		relational_op: $scope.relationOptions[0]
	};
	$scope.lastValue = {
		value: null,
		relational_op: $scope.relationOptions[0]
	};
	$scope.lastValue = {
		value: null,
		relational_op: $scope.relationOptions[0]
	};
	$scope.tcpFlagsValue = {
		value: null,
	};
	$scope.protValue = {
		value: null
	};
	// record to display forms for the fields
	$scope.showField = {
		'srcaddr': true,
		'dstaddr': true,
		'ipLogic': true,
		'srcport': true,
		'dstport': true,
		'portLogic': true,
		'nexthop': true,
		'output': true,
		'input': true,
		'dPkts': true,
		'dOctets': true,
		'first': true,
		'last': true,
		'tcp_flags': true,
		'prot': true
	};
	// $scope.showField = {
	// 	srcaddr: false,
	// 	dstaddr: false,
	// 	ipLogic: false,
	// 	srcport: false,
	// 	dstport: false,
	// 	portLogic: false,
	// 	nexhop: false,
	// 	output: false,
	// 	input: false,
	// 	dPkts: false,
	// 	dOctets: false,
	// 	first: false,
	// 	last: false,
	// 	tcp_flags: false,
	// 	prot: false
	// };


	// build json function
	$scope.FieldstoJSON = function() {
		$scope.jsonData = {};
		for (var key in $scope.showField){
			// only selected fields are added to the jsonData
			if  ($scope.showField[key]){
				// add the fields to the json object
				switch (key){

					case "srcaddr" || "dstaddr":{
						$scope.jsonData['ipValue'] = $scope.ipValues;
						break; 
					};
					case "srcport" || "dstport":{
						$scope.jsonData['portValue'] = $scope.portValues;
						break;
					};
					case "nexthop":{
						$scope.jsonData['nexthopValue'] = $scope.nexthopValue;
						break;
					};
					case "output":{
						$scope.jsonData['outputValue'] = $scope.outputValue;
						break;
					};
					case "input":{
						$scope.jsonData['inputValue'] = $scope.inputValue;
						break;
					};
					case "dPkts":{
						$scope.jsonData['dPktsValue'] = $scope.dPktsValue;
						break;
					};
					case "dOctets":{
						$scope.jsonData['dOctetsValue'] = $scope.dOctetsValue;
						break;
					};
					case "first":{
						$scope.jsonData['firstValue'] = $scope.firstValue;
						break;
					};
					case "last":{
						$scope.jsonData['lastValue'] = $scope.lastValue;
						break;
					};
					case "tcp_flags":{
						$scope.jsonData['tcpFlagsValue'] = $scope.tcpFlagsValue;
						break;
					};
					case "prot":{
						$scope.jsonData['protValue'] = $scope.protValue;
						break;
					};
					default:{
						break;
					};

				};

			};
		};
		return JSON.stringify($scope.jsonData);
	};

	// ajaxcall
	$scope.postQueryData = function(){
		var jsondata = $scope.FieldstoJSON();

		// Simple POST request example (passing data) :
		$http({
        url: '../cgi-bin/execute.cgi',
        method: "POST",
        data: jsondata,
        headers: {'Content-Type': 'application/json'}
      	}).success(function (data, status, headers, config) {
            console.log(status + ' ' + headers);
            console.log(data);
            //$scope.response_status= status + ' ' + headers;
            //$scope.response=data; // assign  $scope.persons here as promise is resolved here 
        }).error(function (data, status, headers, config) {
            //$scope.response=data;
            //$scope.response_status= status + ' ' + headers;
        });
	};
});