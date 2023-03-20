'''
GEORGIA INCOME TAXES
https://dor.georgia.gov/tax-tables-georgia-tax-rate-schedule

Single
If Georgia Taxable Income Is
Over        But not over    Amount of Tax Is
$0          $750            1% of taxable income
$750        $2,250          $8.00 Plus 2% of the amount over $750
$2,250      $3,750          $38.00 Plus 3% of the amount over $2,250
$3,750      $5,250          $83.00 Plus 4% of the amount over $3,750
$5,250      $7,000          $143.00 Plus 5% of the amount over $5,250
$7,000                      $230.00 Plus 5.75% of the amount over $7,000

Married Filing Joint or Head of Household
If Georgia Taxable Income Is
Over        But not over    Amount of Tax Is
$0          $1,000          1% of taxable income
$1,000      $3,000          $10.00 Plus 2% of the amount over $1,000
$3,000      $5,000          $50.00 Plus 3% of the amount over $3,000
$5,000      $7,000          $110.00 Plus 4% of the amount over $5,000
$7,000      $10,000         $190.00 Plus 5% of the amount over $7,000
$10,000                     $340.00 Plus 5.75% of the amount over $10,000

Married Filing Separate
If Georgia Taxable Income Is
Over        But not over    Amount of Tax Is
$0          $500            1% of taxable income
$500        $1,500          $5.00 Plus 2% of the amount over $500
$1,500      $2,500          $25.00 Plus 3% of the amount over $1,500
$2,500      $3,500          $55.00 Plus 4% of the amount over $2,500
$3,500      $5,000          $95.00 Plus 5% of the amount over $3,500
$5,000                      $170.00 Plus 5.75% of the amount over $5,000

DEDUCTIONS 
https://apps.dor.ga.gov/FillableForms/PDFViewer/Index?form=2022GA500
STANDARD DEDUCTION (Lines 6c., 14a.)
Married Filing Jointly -> $7,400
Single or Head of Household -> $2,700
Married Filing Separately -> $3,700

DEPENDENT DEDUCTION
$3,000 for each dependent (Lines 7a., 14b.)

AGE 65+
$1,300 per person (Line 11 b.)
'''
class Georgia:
    taxes = -stateCredits

    if maritalStatus == 'Married Filing Jointly':
        if stateDeductions == 0:
            stateDeductions = 7400 + 3000 * dependents + numOver65 * 1300
        agi -= stateDeductions

        if agi > 10000:
            stateBracket = .055
            margin = agi - 10000
            taxes += 340 + margin * stateBracket
        elif agi > 7000:
            stateBracket = .05
            margin = agi - 7000
            taxes += 190 + margin * stateBracket
        elif agi > 5000:
            stateBracket = .04
            margin = agi - 5000
            taxes += 110 + margin * stateBracket
        elif agi > 3000:
            stateBracket = .03
            margin = agi - 3000
            taxes += 50 + margin * stateBracket
        elif agi > 1000:
            stateBracket = .02
            margin = agi - 1000
            taxes += 10 + margin * stateBracket
        else:
            stateBracket = .01
            taxes += agi * stateBracket
    
    else: # All other filing statuses
        if stateDeductions == 0:
            if maritalStatus == 'Married Filing Separately':
                stateDeductions = 3700
            else:
                stateDeductions = 2700
            stateDeductions += dependents * 3000 + numOver65 * 1300
        agi -= stateDeductions

        if agi > 7000:
            stateBracket = .055
            margin = agi - 7000
            taxes += 230 + margin * stateBracket
        elif agi > 5250:
            stateBracket = .05
            margin = agi - 5250
            taxes += 142.5 + margin * stateBracket
        elif agi > 3750:
            stateBracket = .04
            margin = agi - 3750
            taxes += 82.5 + margin * stateBracket
        elif agi > 2250:
            stateBracket = .03
            margin = agi - 2250
            taxes += 37.5 + margin * stateBracket
        elif agi > 750:
            stateBracket = .02
            margin = agi - 750
            taxes += 7.5 + margin * stateBracket
        else:
            stateBracket = .01
            taxes += agi * stateBracket