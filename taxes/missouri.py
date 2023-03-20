'''
MISSOURI INCOME TAXES 2022
https://dor.mo.gov/taxation/individual/tax-types/income/year-changes/
If the Missouri taxable income is   The tax is
$0 to $111	                        $0
At least $112 but not over $1,121	1.5% of the Missouri taxable income
Over $1,121 but not over $2,242	    $17 plus 2.0% of excess over $1,121
Over $2,242 but not over $3,363	    $39 plus 2.5% of excess over $2,242
Over $3,363 but not over $4,484	    $67 plus 3.0% of excess over $3,363
Over $4,484 but not over $5,605	    $101 plus 3.5% of excess over $4,484
Over $5,605 but not over $6,726	    $140 plus 4.0% of excess over $5,605
Over $6,726 but not over $7,847	    $185 plus 4.5% of excess over $6,726
Over $7,847 but not over $8,968	    $235 plus 5.0% of excess over $7,847
Over $8,968	                        $291 plus 5.3% of excess over $8,968

STANDARD DEDUCTIONS ARE THE SAME AS FEDERAL (SAME LINK)    

LOCAL INCOME TAXES
https://www.kcmo.gov/city-hall/departments/finance/earnings-tax
KCMO 1%

https://www.stlouis-mo.gov/government/departments/collector/earnings-tax/individual-earnings-tax-info.cfm
St. Louis 1%
'''

class Missouri:
    if stateDeductions == 0:
        stateDeductions = federalDeductions
    agi -= stateDeductions

    taxes = -stateCredits
    
    if agi > 8968:
        stateBracket = .053
        margin = agi - 8584
        taxes += 291 + margin * stateBracket
    elif agi > 7847:
        stateBracket = .05
        margin = agi - 7847
        taxes += 235 + margin * stateBracket
    elif agi > 6726:
        stateBracket = .045
        margin = agi - 6726
        taxes += 185 + margin * stateBracket
    elif agi > 5605:
        stateBracket = .04
        margin = agi - 5605
        taxes += 140 + margin * stateBracket
    elif agi > 4484:
        stateBracket = .035
        margin = agi - 4484
        taxes += 101 + margin * stateBracket
    elif agi > 3363:
        stateBracket = .03
        margin = agi - 3363
        taxes += 67 + margin * stateBracket
    elif agi > 2242:
        stateBracket = .025
        margin = agi - 2242
        taxes += 39 + margin * stateBracket
    elif agi > 1121:
        stateBracket = .02
        margin = agi - 1121
        taxes += 17 + margin * stateBracket
    elif agi > 112:
        stateBracket = .015
        margin = agi - 112
        taxes += margin * stateBracket
    
    if county in ['Kansas City', 'St. Louis']:
        localBracket = .01
        taxes += agi * localBracket
        stateBracket += localBracket
