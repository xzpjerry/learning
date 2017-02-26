//: Playground - noun: a place where people can play

import UIKit

var str = "Hello, playground"

class Wechataccount {
    
    var name: String?
    var balance: Double
    init(name: String){
        self.name = name
        self.balance = 0.0
    }
    init(name:String, balance: Double){
        self.balance = balance
        self.name = name
    }
    func check_balance(){
        print("\(name) has \(balance)")
    }
    func deposit(amount: Double){
        balance = balance + amount
    }
    func withdraw(amount: Double){
        balance = balance - amount
    }
    
}
var xzp = Wechataccount(name:"ZhipengX", balance:100)
xzp.check_balance()
xzp.deposit(amount: 60)
xzp.check_balance()
0x1.0p0
