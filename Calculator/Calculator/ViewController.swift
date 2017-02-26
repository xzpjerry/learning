//
//  ViewController.swift
//  Calculator
//
//  Created by zippo on 1/2/17.
//  Copyright © 2017 zippo. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    
    @IBOutlet private weak var display: UILabel!
    
    private var  userIsInTheMiddleofTypeing /*: Bool*/ = false
    
    @IBAction private func touchdigit(_ sender: UIButton) {
        let digit = sender.currentTitle!
        if userIsInTheMiddleofTypeing {
            let textCurrently = display.text!
            display.text = textCurrently + digit
        }else{
            display.text = digit
        }
        userIsInTheMiddleofTypeing = true
    }
    private var resultvalue : Double {
        get{
            return Double(display.text!)!
        }
        set{
            display.text = String(newValue)
        }
    }
    
    private var brain/*: Brain*/ = Brain()
    
    @IBAction private func PerformOperation(_ sender: UIButton) {
        if userIsInTheMiddleofTypeing {
            brain.setnum(num: resultvalue)
            userIsInTheMiddleofTypeing = false
        }
        if let mathmaticalSymbol = sender.currentTitle {
            brain.setOperation(symbol: mathmaticalSymbol)
        }
        resultvalue = brain.result
        
    }
    
}

