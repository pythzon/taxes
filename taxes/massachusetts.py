'''
MASSACHUSETTS INCOME TAX 
https://www.mass.gov/service-details/massachusetts-tax-rates
5%

CAPITAL GAINS TAX (SAME LINK)
LONG TERM - 12%
SHORT TERM - 5%

STATE DEDUCTIONS 
https://www.mass.gov/service-details/view-massachusetts-personal-income-tax-exemptions
$1000 deduction per dependent

STANDARD DEDUCTION
SINGLE OR MARRIED FILING SEPARATELY - $4,400
MARRIED FILING JOINTLY OR QUALIFYING WIDOW - $8,800
HEAD OF HOUSEHOLD - $6,800

CREDITS
https://www.mass.gov/service-details/view-child-and-dependent-related-credits
$240 credit per dependent, max 2

CAPITAL GAINS TAXES
https://www.mass.gov/service-details/massachusetts-tax-rates
LONG-TERM -> 5%
SHORT-TERM -> 12%    
'''

class Massachusetts:
    agi += longCapitalGains
    taxes = shortCapitalGains * .12
    
    if stateDeductions == 0:
        stateDeductions = 1000 * dependents
        if maritalStatus == 'Married Filing Jointly':
            stateDeductions += 8800
        elif maritalStatus == 'Head of household':
            stateDeductions += 6800
        else: # Single or Married filing separately
            stateDeductions += 4400
    agi -= stateDeductions

    if stateCredits == 0:
        if dependents > 2:
            dependents = 2
        stateCredits = dependents * 240
    taxes = -stateCredits

    stateBracket = .05
    taxes += agi * stateBracket