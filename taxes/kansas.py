'''
KANSAS INCOME TAXES
https://www.ksrevenue.gov/taxrates.html
Tax year 2018 and all tax years thereafter
Tax Rates, Resident, married, joint
    taxable income not over $30,000: 3.1 % (K.S.A. 79-32,110)
    taxable income over $30,000 but not over $60,000: $930 plus 5.25 % of excess over $30,000 (K.S.A. 79-32,110)
    taxable income over $60,000: $2,505 plus 5.7 % of excess over $60,000 (K.S.A. 79-32,110)
Tax Rates, Resident, others
    taxable income not over $15,000: 3.1 % (79-32,110)
    taxable income over $15,000 but not over $30,000: $465 plus 5.25 % of excess over $15,000 (K.S.A. 79-32,110)
    taxable income over $30,000: $1252.50 plus 5.7 % of excess over $30,000 (K.S.A. 79-32,110)

Privilege Tax?:
Banks total net income: 2.25% plus 2.125% surtax on taxable income over $25,000 4.375% K.S.A. (79-1107)
Trusts and S&Ls total net income: 2.25% plus 2.25% surtax on taxable income over $25,000 4.50% (K.S.A. 79-1108)

DEDUCTIONS
https://www.ksrevenue.gov/incomebook22.html#0
Standard Deduction (Line 4)
Single: $3,500
Married Filing Jointly: $8,000
Married Filing Separately: $4,000
Head of Household: $6,000

Age 65 or older: $850 if single or head of household, $700 per spouse if married filing jointly or separately (Line 4)
Exemptions: $2,250 per indvidual/spouse or dependent (Line 5)
'''
    
class Kansas:
    if stateDeductions == 0:
        if maritalStatus == 'Married Filing Jointly':
            stateDeductions = 8000 + (2 + dependents * 2250) + numOver65 * 700
        elif maritalStatus == 'Married Filing Separately':
            stateDeductions = 4000 + (1 + dependents * 2250) + numOver65 * 700
        elif maritalStatus == 'Head of Household':
            stateDeductions = 6000 + (1 + dependents * 2250) + numOver65 * 850
        else: # Single
            stateDeductions = 3500 + (1 + dependents * 2250) + numOver65 * 850
    agi -= stateDeductions

    taxes = -stateCredits

    if agi > 30000:
        stateBracket = .057
        margin = agi - 30000
        taxes += 16.76 + margin * stateBracket
    elif agi > 15000:
        stateBracket = .0525
        margin = agi - 15000
        taxes += 5.53 + margin * stateBracket
    else:
        stateBracket = .031
        taxes += agi * stateBracket