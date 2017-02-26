//
//  Brain.swift
//  Calculator
//
//  Created by zippo on 1/3/17.
//  Copyright © 2017 zippo. All rights reserved.
//

import Foundation


class Brain{
    
    private var accumlator/*: Double*/ = 0.0
    
    func setnum(num: Double) {
        accumlator = num
    }
    
    private var opeartions : Dictionary<String, Operation> = [
        "π" : Operation.Constant(M_PI),
        "e" : Operation.Constant(M_E),
        "√" : Operation.UnaryOperation(sqrt),
        "±" : Operation.UnaryOperation({ -$0 }),
        "×" : Operation.BinaryOperation({$0 * $1 }),
        "=" : Operation.Equals,
        "cos" : Operation.UnaryOperation(cos),
        "sin" : Operation.UnaryOperation(sin),
        "+" : Operation.BinaryOperation({$0 + $1}),
        "-" : Operation.BinaryOperation({$0 - $1}),
        "÷" : Operation.BinaryOperation({$0/$1}),
        "." : Operation.BinaryOperation({$0 + $1/10})
    ]
    
    private enum Operation {
        case Constant(Double)
        case UnaryOperation((Double) -> Double )
        case BinaryOperation((Double,Double) -> Double )
        case Equals
    }
    
    func setOperation(symbol: String) {
        if let operation = opeartions[symbol] {
            switch operation{
            case .Constant(let temp):
                accumlator = temp
            case .BinaryOperation(let f):
                excutePending()
                pending = pendingBinaryOperationInfo(function: f, firstOperand: accumlator)
            case .Equals :
                excutePending()
            case .UnaryOperation(let f):
                accumlator = f(accumlator)
            }
        }
    }
    
   
    
    private func excutePending (){
        if pending != nil{
            accumlator = pending!.function(pending!.firstOperand, accumlator)
            pending = nil
        }
    }
    
    private var pending: pendingBinaryOperationInfo?
    
    struct pendingBinaryOperationInfo {
        var function: (Double, Double) -> Double
        var firstOperand: Double
    }
    
    var result: Double{
        get{
            return accumlator
        }
    }
}
