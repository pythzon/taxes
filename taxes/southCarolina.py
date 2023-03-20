'''
SOUTH CAROLINA INCOME TAXES (2022)
https://dor.sc.gov/resources-site/lawandpolicy/Advisory%20Opinions/IL22-15.pdf
For the 2022 tax year the new tax brackets, indexed for inflation, and tax computations for each bracket are:
New Tax Brackets for Tax Year 2022      Bracket Amounts for Tax Year 2022       Compute the tax as follows for each bracket amount
Tax Bracket #1                          $0 to $3,199                            0% times the amount (i.e., exempt from tax)
Tax Bracket #2                          $3,200 to $16,039                       3% times the amount minus $96
Tax Bracket #3                          $16,040 and up                          *6.5% times the amount minus $658

DEDUCTIONS (2022)
https://dor.sc.gov/forms-site/Forms/IITPacket_2022.pdf
Standard Deduction is same as federal (P. 13)
Dependent and Age 65+ Deductions are $4,430 per person (P. 3 and 21)

CAPITAL GAINS TAXES
https://www.scstatehouse.gov/code/t12c006.php
44% of net capital gains are deducted (SECTION 12-6-1150)
'''

class SouthCarolina:
    agi += (shortCapitalGains + longCapitalGains) * .56
    
    if stateDeductions == 0:
        stateDeductions = federalDeductions
        stateDeductions += (dependents + numOver65) * 4430
    agi -= stateDeductions

    taxes = -stateCredits
    
    if agi > 15400:
        stateBracket = .07
        margin = agi - 15400
        taxes += 555 + margin * stateBracket
    elif agi > 12310:
        stateBracket = .06
        margin = agi - 12310
        taxes += 369.6 + margin * stateBracket
    elif agi > 9230:
        stateBracket = .05
        margin = agi - 9230
        taxes += 215.6 + margin * stateBracket
    elif agi > 6150:
        stateBracket = .04
        margin = agi - 6150
        taxes += 92.4 + margin * stateBracket
    elif agi > 3070:
        stateBracket = .03
        margin = agi - 3070
        taxes +  margin * stateBracket