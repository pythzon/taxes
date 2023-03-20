'''
RHODE ISLAND INCOME TAXES
https://tax.ri.gov/sites/g/files/xkgbur541/files/2022-12/2023%20RI-1040ES_w.pdf (P. 1)
Amount of wages is:
Over      But not over       Tax is:
$0        $73,450            3.75%
$73,450   $166,950           $2,754.38 plus 4.75% of the amount over $73,450
$166,950                     $7,195.63 plus 5.99% of the amount over $166,950

STANDARD DEDUCTION AND EXEMPTIONS
https://tax.ri.gov/sites/g/files/xkgbur541/files/2022-12/2023%20RI-1040ES_w.pdf (P. 2)
$0 if AGI is more than $260,550

If AGI is less than $233,750:
Married Filing Jointly: $20,000
Head of Household: $15,050
Married Filing Separately: $10,025
Single: $10,000
$4,700 per dependent

Othwerwise, deductions are 4/5 divided by the ceiling of AGI - $233,750 / $6,700

EIC
https://tax.ri.gov/sites/g/files/xkgbur541/files/2022-12/2022_1040WE_w_0.pdf
15% of the federal EIC
'''

class RhodeIsland:
    import math

    taxes = -stateCredits
    
    if stateDeductions == 0:
        if agi < 260550:
            if maritalStatus == 'Married':
                stateDeductions = 20000
            elif maritalStatus == 'Head of Household':
                stateDeductions = 15050
            elif maritalStatus == 'Married Filing Separately':
                stateDeductions = 10025
            else:
                stateDeductions = 10000
            stateDeductions += (dependents * 4700)
            if agi < 233750:
                agi -= stateDeductions
            else:
                agi -= stateDeductions * .8 / math.ceil((agi - 233750) / 6700)
    agi -= stateDeductions

    if eic:
        taxes -= eic * .15
        
    if agi > 166950:
        stateBracket = .0599
        margin = agi - 166950
        taxes += 7195.63 + margin * stateBracket
    elif agi > 73450:
        stateBracket = .0475
        margin = agi - 73450
        taxes += 2754.38 + margin * stateBracket
    else:
        stateBracket = .0375
        taxes += agi * stateBracket