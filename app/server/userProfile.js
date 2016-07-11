var http = require('http');
var url = 'http://146.169.46.99:3000/dmoz/finduser/ska';

http.get(url, function(res) {
    var body = '';

    res.on('data', function(chunk) {
        body += chunk;
    });

    res.on('end', function() {
        var response = JSON.parse(body)
        console.log("Got response: ", response);
    });
}).on('error', function(e) {
      console.log("Got error: ", e);
});