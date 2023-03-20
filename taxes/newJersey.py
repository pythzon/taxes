'''
NEW JERSEY INCOME TAXES
https://www.state.nj.us/treasury/taxation/taxtables.shtml

SINGLE OR MARRIED FILING SEPARATELY
If Taxable Income is:
Over       But not over        Tax is
$0         $20,000             1.4%  
$20,000    $35,000             1.75% - $70
$35,000    $40,000             3.5% - $682.50
$40,000    $75,000             5.525% - $1,492.50
$75,000    $500,000            6.37% - $2,126.25
$500,000   $1,000,000          8.97% - $15,126.25
$1,000,000                     10.75% - $32,926.25
    
Married/CU filing joint, Head of household, OR Qualifying widow(er)/surviving CU partner STEP
SINGLE OR MARRIED FILING SEPARATELY
If Taxable Income is:
Over       But not over        Tax is
$0         $20,000             1.4%  
$20,000    $50,000             1.75% - $70
$50,000    $70,000             2.45% - $420
$70,000    $80,000             3.5% - $1,154.5
$80,000    $150,000            5.525% - $2,775
$150,000   $500,000            6.37% - $4,042.5
$500,000   $1,000,000          8.97% - $17,042.5
$1,000,000                     10.75% - $34,842.5

DEDUCTIONS AND EXEMPTIONS
https://www.state.nj.us/treasury/taxation/njit13.shtml

Regular Exemptions
You can claim a $1,000 exemption for yourself and your spouse/CU partner (if filing a joint return) or your Domestic Partner.

Senior 65+ Exemptions
You can claim a $1,000 exemption if you were 65 or older on the last day of the tax year. If you are filing jointly, your spouse can take a $1,000 exemption if they were 65 or older on the last day of the tax year. You cannot claim this exemption for your domestic partner or dependents.

Dependent Exemptions
You can claim a $1,500 exemption for each child or dependent who qualifies as your dependent for federal tax purposes.

RECIRPOCAL AGREEMENTS
https://www.nj.gov/treasury/taxation/njit25.shtml
Pennsylvania
'''

class NewJersey:
    if resState == 'Pennsylvania':
            workState = resState

    taxes = -stateCredits

    if maritalStatus in ['Single', "Married Filing Separately"]:
        if stateDeductions == 0:
            stateDeductions = 1000 * (1 + numOver65) + dependents * 1500
        agi -= stateDeductions

        if agi > 1000000:
            stateBracket = .01075
            margin = agi - 1000000
            taxes += margin * stateBracket - 34842.5
        elif agi > 500000:
            stateBracket = .0897
            margin = agi - 500000
            taxes += margin * stateBracket - 17042.5
        elif agi > 150000:
            stateBracket = .0637
            margin = agi - 150000
            taxes += margin * stateBracket - 4042.5
        elif agi > 80000:
            stateBracket = .05525
            margin = agi - 80000
            taxes += margin * stateBracket - 2775
        elif agi > 70000:
            stateBracket = .035
            margin = agi - 70000
            taxes += margin * stateBracket - 1154.5
        elif agi > 50000:
            stateBracket = .0245
            margin = agi - 50000
            taxes += margin * stateBracket - 420
        elif agi > 20000:
            stateBracket = .0175
            margin = agi - 20000
            taxes += margin * stateBracket - 70
        else:
            stateBracket = .014
            taxes += agi * stateBracket
    
    else: # Married Filing Jointly or Head of Household
        if stateDeductions == 0:
            stateDeductions = 1000 * (2 + numOver65) + dependents * 1500
        agi -= stateDeductions
        
        if agi > 1000000:
            stateBracket = .01075
            margin = agi - 1000000
            taxes += margin * stateBracket - 32926.25
        elif agi > 500000:
            stateBracket = .0897
            margin = agi - 500000
            taxes += margin * stateBracket - 15126.25
        elif agi > 75000:
            stateBracket = .0637
            margin = agi - 75000
            taxes += margin * stateBracket - 2126.25
        elif agi > 40000:
            stateBracket = .05525
            margin = agi - 40000
            taxes += margin * stateBracket - 1492.5
        elif agi > 35000:
            stateBracket = .035
            margin = agi - 35000
            taxes += margin * stateBracket - 682.5
        elif agi > 20000:
            stateBracket = .0175
            margin = agi - 20000
            taxes += margin * stateBracket - 70
        else:
            stateBracket = .014
            taxes += agi * stateBracket