"use strict"
var url = require('url');
var express = require('express');
var app = express();
var server = require('http').Server(app);
var WebSocketServer = require('ws').Server
var wss = new WebSocketServer({server: server});
var Room = require('./game/room.js');

var opts = {};
for (var key of process.argv.splice(2)) {
	var keys = key.split('=');
	opts[keys[0]] = keys[1];
}

server.listen(opts.port || 8030, function () {
	console.log('Listening on ' + server.address().port);
});

app.use('/static', express.static('static'));

//游戏地址
app.get('/', function (req, res) {
	res.sendFile(__dirname + '/static/index.html');
});
//游戏地址
app.get('/rooms', function (req, res) {
	res.sendFile(__dirname + '/static/rooms.html');
});
//管理地址
app.get('/admin', function (req, res) {
	res.sendFile(__dirname + '/static/admin.html');
});


//游戏地址
app.get('/createRoom', function (req, res) {
	var type = req.query.type;
	var room = Room.createRoom(type);
	res.writeHead(200, { 'Content-Type': 'text/plain' });
	res.end(room.id+"");
});

//获取房间列表
app.get('/roomsData', function (req, res) {
	res.writeHead(200, { 'Content-Type': 'text/plain' });
	res.end(JSON.stringify(Room.getRoomData()));
});

var adminCode = opts.code || 'admin';
for (var i = 0; i < (opts.room || 1); i++) {
	Room.createRoom("大乱斗", true);
}

wss.on('connection', function (ws) {
	var location = url.parse(ws.upgradeReq.url, true);
	var roomID = location.query.roomID || 1;
	var room = Room.findRoom(roomID);
	if (!room) {
		ws.close();
		return;
	}
	var socket = {
		emit: function (name, data) {
			try {
				var c = name + "$" + JSON.stringify(data);
				ws.send(c);
			} catch (e) {
				console.log(e);
			}
		},
		on: function (name, callback) {
			this.listeners[name] = callback;
		},
		ip: ws.upgradeReq.connection.remoteAddress,
		listeners: {}
	}
	room.game.addClient(socket);

	ws.on('message', function (message) {
		var $s = message.indexOf('$');
		if ($s == -1) {
			var name = message;
			var data = {};
		} else {
			var name = message.substring(0, $s);
			var data = JSON.parse(message.substring($s + 1));
		}
		socket.listeners[name] && socket.listeners[name](data);
	});

	ws.on('close', function () {
		room.game.removeClient(socket);
		socket = null;
		ws = null;
		room = null;
	});
});

