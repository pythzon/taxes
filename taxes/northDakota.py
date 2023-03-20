'''
NORTH DAKOTA INCOME TAXES
https://www.tax.nd.gov/forms

https://www.tax.nd.gov/sites/www/files/documents/forms/2022-individual-income-tax-booklet.pdf
Single
If North Dakota Taxable Income Is:
Over        But Not Over    Your Tax Is: 
$ 0         $41,775         1.10% of North Dakota Taxable Income   
$41,775     $101,050        $459.53 + 2.04% of amount over $ 41,775
$101,050    $210,825        $1,668.74 + 2.27% of amount over $101,050
$210,825    $458,350        $4,160.63 + 2.64% of amount over $210,825
$458,350                    $10,695.29 + 2.90% of amount over $458,350

STANDARD DEDUCTION
https://www.tax.nd.gov/sites/www/files/documents/forms/2022-individual-income-tax-booklet.pdf
Same as federal (P. 12)

TAX CREDITS
https://www.tax.nd.gov/tax-exemptions-credits/income-tax-exemptions-credits

RECIRPOCAL AGREEMENTS
https://www.tax.nd.gov/sites/www/files/documents/forms/business/ndwrfillable.pdf
Minnesota and Montana

CAPITAL GAINS TAXES
https://www.tax.nd.gov/news/tax-legislative-changes/significant-changes-law/individual-income-tax-history
40% of the long-term gains are deducted
'''

class NorthDakota:
    agi += shortCapitalGains + (longCapitalGains * .6)
    if resState in ['Minnesota', 'Montana']:
            workState = resState

    if stateDeductions == 0:
            stateDeductions = federalDeductions
    agi -= stateDeductions

    taxes = -stateCredits

    if maritalStatus == 'Married Filing Jointly':    
        if agi > 440600:
            stateBracket = .029
            margin = agi - 440600
            taxes += 9716.225 + margin * stateBracket
        elif agi > 246700:
            stateBracket = .0264
            margin = agi - 246700
            taxes += 4597.335 + margin * stateBracket
        elif agi > 161950:
            stateBracket = .0227
            margin = agi - 161950
            taxes += 2673.51 + margin * stateBracket
        elif agi > 67050:
            stateBracket = .0204
            margin = agi - 67050
            taxes += 737.55 + margin * stateBracket
        else:
            stateBracket = .011
            taxes += agi * stateBracket
    else:
        if agi > 440600:
            stateBracket = .029
            margin = agi - 440600
            taxes += 10281.415 + margin * stateBracket
        elif agi > 202650:
            stateBracket = .0264
            margin = agi - 202650
            taxes += 3999.535 + margin * stateBracket
        elif agi > 97150:
            stateBracket = .0227
            margin = agi - 97150
            taxes += 1604.685 + margin * stateBracket
        elif agi > 40125:
            stateBracket = .0204
            margin = agi - 40125
            taxes += 441.375 + margin * stateBracket
        else:
            stateBracket = .011
            taxes += agi * stateBracket