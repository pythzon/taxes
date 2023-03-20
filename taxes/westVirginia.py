'''
WEST VIRGINIA INCOME TAXES (2023)
https://tax.wv.gov/Individuals/Pages/PersonalIncomeTaxReductionBill.aspx
Single, Head of household, Married filing jointly, or Qualifying widow(er
Less than $10,000               2.36% of the taxable income
At least    But less than 
$10,000     $25,000             $236.00 plus 3.15% of excess over $10,000
$25,000     $40,000             $900.00 plus 3.54% of excess over $25,000
$40,000     $60,000             $1,575.00 plus 4.72% of excess over $40,000
$60,000                         $2,775.00 plus 5.12% of excess over $60,000

Married filing separately
Less than $5,000                2.36% of the taxable income
At least    But less than      
$5,000$     12,500              $118.00 plus 3.15% of excess over $5,000
$12,500     $20,000             $450.00 plus 3.54% of excess over $12,500
$20,000     $30,000             $787.50 plus 4.72% of excess over $20,000
$30,000                         $1,387.50 plus 5.12% of excess over $30,000

DEDUCTIONS
$2,000 per exemption, including each indivudal or spouse, dependent, and individual or spouse over 65

SOCIAL SECURITY BENEFITS (P. 23/Line 32)
0% is taxable for those with income less than $100,000 if married filing jointly or $50,000 otherwise

LOCAL INCOME TAXES
https://www.nfc.usda.gov/Publications/HR_Payroll/Taxes/Bulletins/2011/TAXES-11-35att.html
Since the following are payroll taxes, they only apply if the user is working
Charleston: $4 per pay period
Huntington: $6 per pay period
Parkersburg: $5 per pay period

RECIRPOCAL AGREEMENTS
https://tax.wv.gov/Documents/TSD/tsd438.pdf
Kentucky, Maryland, Ohio, Pennsylvania, and Virginia
'''
class WestVirginia:
    if resState in ['Kentucky', 'Maryland', 'Ohio', 'Pennsylvania', 'Virginia']:
            workState = resState
    if stateDeductions == 0:
        stateDeductions = 2000
        if maritalStatus == 'Married Filing Jointly':
            stateDeductions = 4000
        stateDeductions += (dependents + numOver65) * 2000
    agi -= stateDeductions

    taxes = -stateCredits

    if maritalStatus != 'Married Filing Separately':
        if agi > 60000:
            stateBracket = .0512
            margin = agi - 60000
            taxes = 2775 + margin * stateBracket
        elif agi > 40000:
            stateBracket = .0472
            margin = agi - 1000
            taxes = 1575 + margin * stateBracket
        elif agi > 25000:
            stateBracket = .0354
            margin = agi - 25000
            taxes = 900 + margin * stateBracket
        elif agi > 10000:
            stateBracket = .0315
            margin = agi - 10000
            taxes = 236 + margin * stateBracket
        else:
            stateBracket = .0236
            taxes = agi * stateBracket
    
    # Married filing separately
    else:
        if agi > 60000:
            stateBracket = .0512
            margin = agi - 60000
            taxes = 1387.5+ margin * stateBracket
        elif agi > 40000:
            stateBracket = .0472
            margin = agi - 1000
            taxes = 787.5 + margin * stateBracket
        elif agi > 25000:
            stateBracket = .0354
            margin = agi - 25000
            taxes = 450 + margin * stateBracket
        elif agi > 10000:
            stateBracket = .0315
            margin = agi - 10000
            taxes = 118 + margin * stateBracket
        else:
            stateBracket = .0236
            taxes = agi * stateBracket

    if county == 'Charleston':
        taxes += 4 * payPeriods
    elif county == 'Huntington':
        taxes += 6 * payPeriods
    elif county == 'Parkersburg':
        taxes += 5 * payPeriods
