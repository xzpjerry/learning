"use strict"
var Pack = require('../static/js/JPack.js');
var C = require('../static/js/const.js');


var Map = require('./map.js');
var User = require('./user.js');
var Item = require('./item.js');
var Client = require('./client.js');

var map1 = require('./maps/lesson1.js');
var map2 = require('./maps/lesson2.js');


function userCollide(a, b, game) {
	//不碰撞情况
	if (a.dead || b.dead) {return}
	if((a.x-b.x)*(a.x-b.x) + (a.y-b.y)*(a.y-b.y) > game.props.userWidth*game.props.userWidth) {return;}

	//带电情况
	if (a.carry == Pack.items.power.id && b.carry != Pack.items.power.id) {
		b.killed('power', a);
		b.vx = (b.x - a.x)/2;
		if (b.carry == Pack.items.bomb.id) {
			a.carry = b.carry;
			a.carryCount = b.carryCount;
			b.carry = '';
		}
		return;
	} else if (a.carry != Pack.items.power.id && b.carry == Pack.items.power.id) {
		a.killed('power', b);
		a.vx = (a.x - b.x)/2;
		if (a.carry == Pack.items.bomb.id) {
			b.carry = a.carry;
			b.carryCount = a.carryCount;
			a.carry = '';
		}
		return;
	} else if (a.carry == Pack.items.power.id && b.carry == Pack.items.power.id) {
		a.carry = '';
		b.carry = '';
	}
	//排除刚刚碰撞
	if (a.ignore[b.id] > 0 || b.ignore[a.id] > 0) {return}
	
	if (b.carry == Pack.items.bomb.id && a.carry != Pack.items.bomb.id) {
		a.carry = b.carry;
		a.carryCount = b.carryCount;
		b.carry = '';
	} else if (a.carry == Pack.items.bomb.id && b.carry != Pack.items.bomb.id) {
		b.carry = a.carry;
		b.carryCount = a.carryCount;
		a.carry = '';
	}
	//正常情况
	if (a.onFloor && b.onFloor) {
		if (a.crawl && !b.crawl) {
			b.vy = 5;
			b.danger = true;
		} else if (!a.crawl && b.crawl) {
			a.vy = 5;
			a.danger = true;
		} else {
			if (a.crawl && b.crawl) {
				a.crawl = false;
				b.crawl = false;
			}
			var tmp = a.vx;
			a.vx = b.vx;
			b.vx = tmp;
			
			a.vy = 2.5;
			b.vy = 2.5;
		}
	} else if (a.onFloor && !b.onFloor) {
		if (a.crawl) {
			a.vx = b.vx / 2;
			b.vx = -b.vx / 2;
			a.vy = 2.5;
			b.vy = 2.5;
		} else {
			a.vx = b.vx;
			b.vx /= 2;
			a.vy = 2.5;
			a.danger = true;
		}
	} else if (!a.onFloor && b.onFloor) {
		if (b.crawl) {
			b.vx = a.vx / 2;
			a.vx = -a.vx / 2;
			b.vy = 2.5;
			a.vy = 2.5;
		} else {
			b.vx = a.vx;
			a.vx /= 2;
			b.vy = 2.5;
			b.danger = true;
		}
	} else {
		var tmp = a.vx;
		a.vx = b.vx;
		b.vx = tmp;
		a.danger = true;
		b.danger = true;
	}
	//自然抗拒
	if (a.x < b.x) {
		if (!a.crawl) {
			a.vx -= 1;
		}
		if (!b.crawl) {
			b.vx += 1;
		}
	} else {
		if (!a.crawl) {
			a.vx += 1;
		}
		if (!b.crawl) {
			b.vx -= 1;
		}
	}
	//阻止近期碰撞
	a.ignore[b.id] = 40;
	b.ignore[a.id] = 40;
	a.fireing = false;
	b.fireing = false;
	a.mining = false;
	b.mining = false;
	a.onPilla = false;
	b.onPilla = false;
	a.lastTouch = b.id;
	b.lastTouch = a.id;
}

function eatItem (a, b, game) {
	if (a.dead || b.dead) {return}
	if (a.carry == Pack.items.bomb.id) {return}
	if((a.x-b.x)*(a.x-b.x) + (a.y+game.props.userHeight/2-b.y)*(a.y+game.props.userHeight/2-b.y) >
			(game.props.userWidth+C.IS)*(game.props.userWidth+C.IS)/4) {
		return;
	}
	b.touchUser(a);
}

var Game = function (adminCode, maxUser, type, remove) {
	this.adminCode = adminCode;
	this.users = [];
	this.clients = [];
	this.items = [];
	this.bodies = [];
	this.mines = [];
	this.entitys = [];
	this.tick = 0;
	this.remove = remove;
	this.props = {
		userHeight: 40,
		userWidth: 40,
		itemSize: 15,
		tw: 28,
		th: 15,
		maxUser: maxUser,
	}
	if (type == "lesson1") {
		this.props.th = map1.h;
		this.props.tw = map1.w;
	} else if (type == "lesson2") {
		this.props.th = map2.h;
		this.props.tw = map2.w;
	}
	this.props.w = this.props.tw * C.TW;
	this.props.h = this.props.th * C.TH;
	
	if (type == "lesson1") {
		this.map = new Map(this, map1);
	} else if (type == "lesson2") {
		this.map = new Map(this, map2);
	} else {
		this.map = new Map(this);
	}
	this.runningTimer = setInterval(() => {
		this.update();
	}, 17);
}
Game.prototype.createNPC = function (data) {
	var u = new User(this, data);
	u.npc = true;
	this.users.push(u);
	return u;
}
//增加玩家
Game.prototype.createUser = function (client) {
	var u = new User(this, client);
	var place = this.map.born();
	u.x = place.x;
	u.y = place.y + C.TH/2;
	this.users.push(u);
	return u;
}
//获得玩家（或者尸体）
Game.prototype.getUser = function (uid) {
	for (let user of this.users) {
		if (user.id == uid) {
			return user;
		}
	}
	for (let user of this.bodies) {
		if (user.id == uid) {
			return user;
		}
	}
}
//获得链接
Game.prototype.getClient = function (cid) {
	for (let client of this.clients) {
		if (client.id == cid) {
			return client;
		}
	}
}
Game.prototype.createItem = function (type) {
	var item = new Item(this, type);
	this.items.push(item);
	return item;
}
//发生爆炸
Game.prototype.explode = function (x, y, byUser, power) {
	for (let user of this.users) {
		var ux = user.x;
		var uy = user.y + this.props.userHeight;
		var dist = (ux - x)*(ux - x) + (uy - y)*(uy - y);
		if (dist < power*power) {
			user.killed('bomb', byUser);
		}
		if (dist < 2.25*power*power) {
			var r = Math.atan2(uy - y, ux - x);
			var force = 450 * power / (dist + 2500);
			user.vx += force * Math.cos(r);
			user.vy += force * Math.sin(r);
			user.danger = true;
		} 
	};
	this.announce('explode', {x: x, y: y, power: power});
}

//发生枪击
Game.prototype.checkShot = function (u) {
	var game = this;
	var x = u.x;
	var y = u.y + game.props.userHeight*2/3;
	var f = u.faceing;

	for (let user of this.users) {
		var uh = game.props.userHeight;
		if (user.crawl) {
			uh /= 2;
		}
		if (f < 0 && x > user.x && user.y <= y && user.y + uh >= y) {
			user.killed('gun', u);
			user.vx = 6 * f;
		}

		if (f > 0 && x < user.x && user.y <= y && user.y + uh >= y) {
			user.killed('gun', u);
			user.vx = 6 * f;
		}
	}
}

Game.prototype.addMine = function (user) {
	var x = user.x + user.faceing * 40;
	if (this.map.onFloor(x, user.y)) {
		this.mines.push({
			x: x,
			y: user.y,
			creater: user,	
		});
		return true;
	}
	return false;
}
Game.prototype.checkMine = function (user) {
	for (var i = this.mines.length - 1; i >= 0; i--) {
		var mine = this.mines[i];
		if (Math.abs(user.x - mine.x) < 10 && Math.abs(user.y - mine.y) < 5) {
			user.killed('mine', mine.creater);
			mine.dead = true;
			return true;
		}
	}
	return false;
}
//链接
Game.prototype.addClient = function (socket) {
	this.clients.push(new Client(socket, this));
}
//链接关闭
Game.prototype.removeClient = function (socket) {
	for (var i = 0; i < this.clients.length; i++) {
		if (this.clients[i].socket == socket) {
			var client = this.clients[i];
			client.leaveTime = new Date().getTime();
			console.log('User <' + client.name + '> '
				 + ' ['+client.joinTime+':'+client.leaveTime+':'+Math.floor((client.joinTime-client.leaveTime)/60)+']'
				 + ' ['+client.kill+','+client.death+','+client.highestKill+']');
			this.clients.splice(i, 1);
			return;
		}
	}
}
//分发事件
Game.prototype.announce = function (type, data) {
	for (let client of this.clients) {
		client.socket.emit(type, data);
	}
}

Game.prototype.win = function (user) {
	this.announce('win', user.id);
	setTimeout(() => {
		clearInterval(this.runningTimer);
		this.remove && this.remove(this);
	}, 1000);
}

//游戏主流程
Game.prototype.update = function () {
	this.tick++;
	this.map.update();
	//物品更新
	for(let item of this.items) {
		item.update();
	}
	//实体更新
	for(let entity of this.entitys) {
		entity.update();
	}
	//碰撞检测
	for (var i = 0; i < this.users.length; i++) {
		for (var j = i + 1; j < this.users.length; j++) {
			userCollide(this.users[i], this.users[j], this);
		}
		for (var j = 0; j < this.items.length; j++) {
			eatItem(this.users[i], this.items[j], this);
		}
	}
	//user更新
	for(let user of this.users) {
		user.update();
	};
	//分发状态
	this.sendTick();
	//清理死亡的人物/物品
	this.clean();
}
Game.prototype.clean = function () {
	for(var i = this.items.length - 1; i >= 0; i--) {
		var item = this.items[i];
		if (!item.dead) {
		} else {
			this.items.splice(i, 1);
		}
	}
	for(var i = this.mines.length - 1; i >= 0; i--) {
		var mine = this.mines[i];
		if (!mine.dead) {
		} else {
			this.mines.splice(i, 1);
		}
	}
	for(var i = this.entitys.length - 1; i >= 0; i--) {
		var entity = this.entitys[i];
		if (!entity.dead) {
		} else {
			this.entitys.splice(i, 1);
		}
	}
	for(var i = this.users.length - 1; i >= 0; i--) {
		var user = this.users[i];
		if (!user.dead) {
		} else {
			this.users.splice(i, 1);
			this.bodies.push(user);
			if (this.bodies.length > 100) {
				this.bodies = this.bodies.slice(0, 50);
			}
		}
	}
}
Game.prototype.sendTick = function () {
	var itemdata = [];
	for (let item of this.items) {
		itemdata.push(item.getData());
	}
	var userdata = [];
	for (let user of this.users) {
		userdata.push(user.getData());
	}
	var clientsdata = [];
	for (let client of this.clients) {
		clientsdata.push(client.getData());
	}
	var entitydata = [];
	for (let entity of this.entitys) {
		entitydata.push(Pack.entityPack.encode(entity));
	}
	for (let client of this.clients) {
		var p1 = client.p1 && client.p1.id;
		var p2 = client.p2 && client.p2.id;
		var onStruct = client.p1 && client.p1.onStruct;
		var minedata = [];
		for (let mine of this.mines) {
			if ((mine.creater.id == p1 && !p2) || mine.dead) {
				minedata.push(Pack.minePack.encode(mine));
			}
		};
		if (client.admin) {
			if (this.tick % 60 == 0) {
				client.socket.emit('tick', {
					users: userdata,
					items: itemdata,
					mines: minedata,
					clients: clientsdata
				});
			}
		} else {
			client.socket.emit('tick', {
				users: userdata,
				items: itemdata,
				mines: minedata,
				entitys: entitydata,
				p1: p1,
				onStruct: onStruct,
				p2: p2
			});
		}
	}
}
module.exports = Game;