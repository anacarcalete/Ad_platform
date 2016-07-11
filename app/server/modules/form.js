var MongoDB 	= require('mongodb').Db;
var Server 		= require('mongodb').Server;
var moment 		= require('moment');

var dbPort 		= 27017;
var dbHost 		= 'localhost';
var dbName 		= 'form-data';



var db = new MongoDB(dbName, new Server(dbHost, dbPort, {auto_reconnect: true}), {w: 1});
	db.open(function(e, d){
	if (e) {
		console.log(e);
	}	else{
		console.log('connected to database :: ' + dbName);
	}
});

var form = db.collection('form');

var img = db.collection('img');
exports.addUsersAd = function(newData, callback)
{
	console.log(newData)
	form.insert(newData, {safe: true}, callback)

}

exports.addImgAd = function(newData, callback)
{
	
}