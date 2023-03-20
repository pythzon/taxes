'''
VERMONT INCOME TAXES (2022)
Which one is the best approximation for 2023?
https://tax.vermont.gov/sites/tax/files/documents/GB-1210-2023.pdf (Only Single and Married Filing Jointly?)
https://tax.vermont.gov/sites/tax/files/documents/Income%20Booklet-2022.pdf (P. 45) For Comparison
Married Filing Jointly
If Wages are:
over         but not over   Tax is:
$0           $10,538        $0
$10,538      $86,388        3.35% of amount over $10,538
$86,388      $193,938       $2,540.98 + 6.60% of amount over $86,388
$193,938     $289,988       $9,639.28 + 7.60% of amount over $193,938
$289,988                    $16,939.08 + 8.75% of amount over 289,988

Other Filers
If Wages are:
over         but not over   Tax is:
$0           $3,500         $0
$3,500       $48,900        3.35% of amount over $3,500
$48,900      $113,550       $1,520.90 + 6.60% of amount over $48,900
$113,550     $233,050       $5,787.80 + 7.60% of amount over $113,550
$233,050                    $14,869.80 + 8.75% of amount over #233,050

Special Clause
https://tax.vermont.gov/sites/tax/files/documents/Income%20Booklet-2022.pdf (P. 45) For Comparison (P. 11, Line 8)
If AGI is more than $150,000, the filer must pay a minimum of 3%

DEDUCTIONS AND EXEMPTIONS (2022)
https://tax.vermont.gov/sites/tax/files/documents/Income%20Booklet-2022.pdf (P. 10)
STANDARD DEDUCTION
Single or Married Filing Separately: $6,800
Married Filing Jointly $13,050
Head of Household: $9,800

$4,500 per individual/spouse, dependent
$1,050 per individual/spouse over 65

CREDITS (2022)
https://tax.vermont.gov/individuals/personal-income-tax/tax-credits
Dependent based:
    "72% of the federal Child and Dependent Care Tax Credit"
    "Fully refundable"
EIC based:
    "38% of the federal Earned Income Tax Credit"

VERMONT CAPITAL GAINS TAXES 
https://tax.vermont.gov/individuals/personal-income-tax/taxable-income
40% of long capital gains of assets held for more than 3 years up to $350,000 in deductions
'''

class Vermont:
    if capitalGains > 875000:
        agi -= 350000
    else:
        agi -= capitalGains * .4

    taxes = -stateCredits

    if stateDeductions == 0:
        if maritalStatus == 'Married Filing Jointly':
            stateDeductions = 13050 + (2 + dependents) * 4500 + numOver65 * 1050
        elif maritalStatus == 'Head of Household':
            stateDeductions = 9800 + (1 + dependents) * 4500 + numOver65 * 1050
        else: # Single or Married Filing Separately
            stateDeductions = 6800 + (1 + dependents) * 4500 + numOver65 * 1050
        
    agi -= stateDeductions

    if maritalStatus == 'Married Filing Jointly':
        if agi > 289988:
            stateBracket = .0875
            margin = agi - 289988
            taxes += 16939.08 + margin * stateBracket
        elif agi > 193938:
            stateBracket = .076
            margin = agi - 193938
            taxes += 9639.08 + margin * stateBracket
        elif agi > 86388:
            stateBracket = .066
            margin = agi - 86388
            taxes += 2540.98 + margin * stateBracket
        else:
            stateBracket = .0335
            taxes += agi * stateBracket
    
    else: # All other filing statuses
        if agi > 204000:
            stateBracket = .0875
            margin = agi - 204000
            taxes += 13214.625 + margin * stateBracket
        elif agi > 97800:
            stateBracket = .076
            margin = agi - 97800
            taxes += 5143.425 + margin * stateBracket
        elif agi > 40350:
            stateBracket = .066
            margin = agi - 40350
            taxes += 1351.725 + margin * stateBracket
        else:
            stateBracket = .0335
            taxes += agi * stateBracket
    if eic:
        taxes -= eic * .38

    # Special clause from line 8 of tax form
    if agi > 15000 and  taxes < .03 * agi:
        taxes = .03 * agi