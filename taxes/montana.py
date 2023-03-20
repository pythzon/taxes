'''
MONTANA INCOME TAXES
https://mtrevenue.gov/wp-content/uploads/dlm_uploads/2023/02/Form_2_2022-1.pdf (P. 8)
If your Montana taxable income is:
More than         But not more than      Your tax is:
$0                 $3,300                1%
$3,300             $5,800                2% - $33
$5,800             $8,900                3% - $91
$8,900             $12,000               4% - $180
$12,000            $15,400               5% - $300
$15,400            $19,800               6% - $454
$19,800                                  6.75% - $603

RECIRPOCAL AGREEMENTS
https://mtrevenue.gov/wp-content/uploads/2022/12/montana-employees-withholding-allowance-and-exemption-certificate-form-mw-4.pdf
North Dakota

STANDARD DEDUCTION
https://mtrevenue.gov/wp-content/uploads/dlm_uploads/2023/02/Form_2_2022-1.pdf (P. 7)

Married Filing Jointly or Head of Household
$4,520 if your Montana taxable income is $22,600 or less
20% of your Montana taxable income if your Montana taxable income is more than $22,600 but not more than $50,900
$10,180 if your Montana taxable income is more than $50,900

Single or Married Filing Separately
$2,260 if your Montana taxable income is $22,600 or less
20% of your Montana taxable income if your Montana taxable income is more than $22,600 but not more than $50,900
$10,180 if your Montana taxable income is more than $50,900

EXEMPTIONS
https://mtrevenue.gov/wp-content/uploads/dlm_uploads/2023/02/Form_2_2022-1.pdf (P. 1)
$2,710 for each dependent or individual or spouse over the age 65


CAPITAL GAINS TAXES
https://mtrevenue.gov/2021/11/29/simplification-of-montana-income-taxation/?utm_source=rss&utm_medium=rss&utm_campaign=simplification-of-montana-income-taxation
30% of long term gains are deducted, but all gains are treated as ordinary income

EIC
https://mtrevenue.gov/wp-content/uploads/dlm_uploads/2023/02/Form_2_2022-1.pdf (P. 1)
3% of federal EIC
'''

# !Federal deduction only applies if itemizing !margin with deductions *sigh*
class Montana:
    agi += shortCapitalGains + (longCapitalGains * .7)
    
    if resState == 'North Dakota':
            workState = resState

    if stateDeductions == 0:
        if maritalStatus in ['Married', 'Head of Household']:
            if agi > 50900:
                stateDeductions = 10180
            elif agi > 22600:
                stateDeductions = agi * .2
            else:
                stateDeductions = 4520
        # Single, Married Filing Separately, or Qualifying Widow(er)
        else:
            if agi > 25450:
                stateDeductions = 5090
            elif agi > 11300:
                stateDeductions = agi * .2
            else:
                stateDeductions = 2260
        if dependents > 3:
            dependents = 3
        stateDeductions += (dependents+ numOver65) * 2710
    agi -= stateDeductions

    taxes = -stateCredits

    if agi > 19800:
        stateBracket = .0675
        margin = agi - 19800
        taxes += agi * stateBracket - 603
    elif agi > 15400:
        stateBracket = .06
        margin = agi - 15400
        taxes += agi* stateBracket - 454
    elif agi > 12000:
        stateBracket = .05
        margin = agi - 12000
        taxes += 300 + margin * stateBracket
    elif agi > 8900:
        stateBracket = .04
        margin = agi - 8900
        taxes += 180 + margin * stateBracket
    elif agi > 5800:
        stateBracket = .03
        margin = agi - 5800
        taxes += 91 + margin * stateBracket
    elif agi > 3300:
        stateBracket = .02
        margin = agi - 3300
        taxes += 33 + margin * stateBracket
    else:
        stateBracket = .01
        taxes += agi * stateBracket