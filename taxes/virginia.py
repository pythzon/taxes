'''
VIRGINIA INCOME TAXES (2023)
https://www.tax.virginia.gov/sites/default/files/vatax-pdf/2022-760-instructions.pdf (P. 35)
If your AGI is:
Over      But not over       Tax is:
$0        $3,00              2% of AGI
$3,000    $5,000             $60 plus 3% of the amount over $3,000
$5,000    $17,000            $120 plus 5% of the amount over $17,000
$17,000                      $720 plus 5.75% of the amount over $17,000

DEDUCTIONS
STANDARD DEDUCTION
https://www.tax.virginia.gov/sites/default/files/vatax-pdf/2022-760-instructions.pdf (P.1)
Increase in Standard Deduction: New legislation enacted during the 2022 General Assembly session increases the
$16,000 for married filers filing jointly, $8,000 otherwise

DEPENDENT DEDUCTION
https://www.tax.virginia.gov/sites/default/files/vatax-pdf/2022-760-instructions.pdf (P.10)
$930 per dependent

AGE 65 OR OLDER DEDUCTION
https://www.tax.virginia.gov/sites/default/files/vatax-pdf/2022-760-instructions.pdf (P.10)
$800 per spouse age 65 or older

RECIRPOCAL AGREEMENTS
https://www.tax.virginia.gov/reciprocity
District of Columbia, Kentucky, Maryland, Pennsylvania, and West Virginia
'''

class Virginia:
    if resState in ['District of Columbia', 'Kentucky', 'Maryland', 'Pennsylvania', 'West Virginia']:
        workState = resState
    
    if stateDeductions == 0:
        if maritalStatus == 'Married Filng Jointly':
            stateDeductions = 16000
        else: # All other filers
            stateDeductions = 8000
        stateDeductions += dependents * 930
        stateDeductions += numOver65 * 800
    agi -= stateDeductions

    taxes = -stateCredits

    if agi > 17000:
        stateBracket = .0575
        margin = agi - 17000
        taxes += 720 + margin * stateBracket
    elif agi > 5000:
        stateBracket = .05
        margin = agi - 5000
        taxes += 120 + margin * stateBracket
    elif agi > 3000:
        stateBracket = .03
        margin = agi - 3000
        taxes += 60 + margin * stateBracket
    else:
        stateBracket = .02
        taxes += agi * stateBracket