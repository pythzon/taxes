'''
MISSISSIPPI INCOME TAXES
https://www.dor.ms.gov/individual/tax-rates

0% on the first $5,000 of taxable income.​                                                                                                                                                                                                                                                                                                      
4% on the next $5,000 of taxable income.                                                                                                                                                                                                                                                                                                                            
5% on the remaining taxable income in excess of $10,000.

EXEMPTIONS (SAME LINK)
Married Filing Joint or Combined*​	 	$12,000	 
Married Spouse Deceased	 	           $12,000	 
Married Filing Separate     	       $6,000 
Head of Family	 	                   $8,000
Single	 	                           $6,000	 
Dependent                       	   $1,500	 
Taxpayer or Spouse over 65	 	       $1,500	 

DEDUCTIONS (SAME LINK)
Married Filing Joint or Combined    $ 4,600	 
Married Spouse Deceased	 	        $ 4,60​0	 
Married Filing Separate	 	        $ 2,300
Head of Family	 	                $ 3,400	 
Single	 	                        $ 2,300
'''

class Mississippi:
    if stateDeductions == 0:
        # COMBINED DEDUCTIONS AND EXEMPTIONS
        stateDeductions = (dependents * 1500)
        if maritalStatus == 'Married':
            stateDeductions += 16600
        elif maritalStatus == 'Head of Household':
            stateDeductions += 11400
        elif maritalStatus in ['Single', 'Married Filing Separately']:
            stateDeductions += 8300
    agi -= stateDeductions

    taxes = -stateCredits

    if agi > 10000:
        stateBracket = .05
        margin = agi - 10000
        taxes += 230 + margin * stateBracket
    
    elif agi > 5000:
        stateBracket = .04
        margin = agi - 5000
        taxes += margin * stateBracket