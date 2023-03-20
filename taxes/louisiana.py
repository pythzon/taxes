'''
LOUISIANA INCOME TAX RATES
https://revenue.louisiana.gov/individualincometax

MARRIED FILING JOINTLY OR QUALIFYING SURVIVING SPOUSE
TAX BRACKET         RATE
$0 - $25,000        1.85%
$25,001 - $100,000   3.50%
$100,001+            4.25%

SINGLE, HEAD OF HOUESEHOLD, MARRIED FILING SEPERATELY
TAX BRACKET         RATE
$0 - $12,500        1.85%
$12,501 - $50,000   3.50%
$50,001+            4.25%

DEDUCTIONS
CREDIT OF $1,000 FOR EACH DEPENDENT OR EACH TAXPAYER/SPOUSE AGE 65 OR OLDER

STANDARD DEDUCTION
https://www.revenue.louisiana.gov/taxforms/6935(11_02)F.pdf
MARRIED FILING JOINTLY OR QUALIFYING SURVIVING SPOUSE - $9,000
SINGLE, HEAD OF HOUSEHOLD, MARRIED FILING SEPERATELY - $4,500
'''

class Louisiana:
    taxes = -stateCredits
    
    if maritalStatus == 'Married Filing Jointly':
        if stateDeductions == 0:
            stateDeductions = 9000 + (dependents + numOver65) * 1000
        agi -= stateDeductions

        if agi > 100000:
            stateBracket = .0425
            margin = agi - 100000
            taxes += 3087.5 + margin * stateBracket
        elif agi > 25000:
            stateBracket = .035
            margin = agi - 25000
            taxes += 462.5 + margin * stateBracket
        else:
            stateBracket = .0185
            taxes += agi * stateBracket
    else:
        if stateDeductions == 0:
            stateDeductions = 4500 + (dependents + numOver65) * 1000
        agi -= stateDeductions

        if agi > 50000:
            stateBracket = .0425
            margin = agi - 50000
            taxes += 1543.75 + margin * stateBracket
        elif agi > 12500:
            stateBracket = .035
            margin = agi - 12500
            taxes += 231.25 + margin * stateBracket
        else:
            stateBracket = .0185
            taxes += agi * stateBracket
