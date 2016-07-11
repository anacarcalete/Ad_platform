var http = require("http"),
    url = require("url"),
    path = require("path"),
    fs = require("fs")
    port = process.argv[2] || 3000;

var http = require('http');
var express = require('express');
var session = require('express-session');
var bodyParser = require('body-parser');
var errorHandler = require('errorhandler');
var cookieParser = require('cookie-parser');
var MongoStore = require('connect-mongo')(session);
var app = express();

app.set('views', __dirname + '/app/server/views');
app.set('view engine', 'jade');
app.use(cookieParser());
app.use(session({
  secret: 'faeb4453e5d14fe6f6d04637f78077c76c73d1b4',
  proxy: true,
  resave: true,
  saveUninitialized: true,
  store: new MongoStore({ host: 'localhost', port: 27017, db: 'node-login'})
  })
);
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(require('stylus').middleware({ src: __dirname + '/app/public' }));
app.use(express.static(__dirname + '/app/public'));

require('./app/server/routes')(app);

if (app.get('env') == 'development') app.use(errorHandler());

 
// http.createServer(function(request, response) {

//   var uri = url.parse(request.url).pathname
//     , filename = path.join(process.cwd(), uri);

//   var contentTypesByExtension = {
//     '.html': "text/html",
//     '.css':  "text/css",
//     '.js':   "text/javascript"
//   };

//   fs.exists(filename, function(exists) {
//     if(!exists) {
//       response.writeHead(404, {"Content-Type": "text/plain"});
//       response.write("404 Not Found\n");
//       response.end();
//       return;
//     }

//     if (fs.statSync(filename).isDirectory()) filename += '/index.html';

//     fs.readFile(filename, "binary", function(err, file) {
//       if(err) {        
//         response.writeHead(500, {"Content-Type": "text/plain"});
//         response.write(err + "\n");
//         response.end();
//         return;
//       }

//       var headers = {};
//       var contentType = contentTypesByExtension[path.extname(filename)];
//       if (contentType) headers["Content-Type"] = contentType;
//       response.writeHead(200, headers);
//       response.write(file, "binary");
//       response.end();
//     });
//   });
// }).listen(parseInt(port, 10));

http.createServer(app).listen(parseInt(port, 10)), function(){
   
};

console.log("Static file server running at\n  => http://localhost:" + port + "/\nCTRL + C to shutdown");
