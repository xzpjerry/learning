#! /usr/bin/env python3
'''
  Estimating federal income tax.  Assignment 1, CIS 210
  
  Authors:  Zhipeng Xie
  
  Credits: 'python.org' document

  Inputer income and num_of_exemption, output tax.
'''
def brain (temp_income, temp_num_of_exempt):
    '''
    (float or int, int) -> float
    
    return estimated tax result (result) based on
    the income and the number of exemption, is the
    brain of est_tax function, which is in charge of
    the computation.
    
    >>> brain(2000,2)
    0
    >>> brain(20000,2)
    380
    >>> brian(0,2)
    0
    '''
    if temp_income <= 10000:
        result = 0
        return result
    else:
        Standard_Deduction = 10000
        One_exemption_amount = 4050
        tax_rate = 0.2
        money_table = temp_income - Standard_Deduction - ( temp_num_of_exempt * One_exemption_amount)
        result = money_table * tax_rate
        return result

def est_tax(income, num_of_exempt):
    '''
    (float or int, int) -> string

    print estimated tax information based on
    income and number of exemption.
    None value is returned, its job is check the arguments
    eligibility and uses the result of brain function.

    >>> est_tax(abc, efg)
    Bad number(s)
    >>> est_tax(30000,0.5)
    Bad number(s)
    >>> est_tax(20000,2)
    Estimated federal income tax for
    reported income: $ 20000.00
    with 2 exemptions,
    using standard deduction $10000 and
    an assumed 20% tax rate is : $380.00    
    '''
    if isinstance(income,(int,float)):
        if isinstance(num_of_exempt,(int)):
            if income >= 0:
                print('''Estimated federal income tax for
reported income: $ %.2f
with %d exemptions,
using standard deduction $10000 and
an assumed 20%% tax rate is : $%.2f''' % (income, num_of_exempt,brain(income,num_of_exempt)))
    else:
        raise TypeError('Bad number(s)')

est_tax(20000,2)