'''
IDAHO INCOME TAXES (2022)
https://tax.idaho.gov/taxes/income-tax/individual-income/individual-income-tax-rate-schedule/
Single
At least	Less than	Tax	Rate
$1	        $1,662	    $0.00	plus 1.0% of the amount over $0
$1,662  	$4,987	    $16.62	plus 3.0% of the amount over $1,662
$4,987	    $8,311	    $116.36	plus 4.5% of the amount over $4,987
$8,311		            $265.96	plus 6.0% of the amount over $8,311
Married
At least	Less than	Tax	Rate
$1	        $3,324	    $0.00	plus 1.0% of the amount over $0
$3,324	    $9,974	    $33.24	plus 3.0% of the amount over $3,324
$9,974	    $16,622	    $232.72	plus 4.5% of the amount over $9,974
$16,622		            $531.92	plus 6.0% of the amount over $16,622

DEDUCTIONS (2022)
https://tax.idaho.gov/wp-content/uploads/forms/EIN00046/EIN00046_03-01-2023.pdf (P.8)
Same as federal
'''
class Idaho:
    if stateDeductions == 0:
        stateDeductions = federalDeductions
    agi -= stateDeductions

    taxes = -stateCredts
    if maritalStatus == 'Married':
        if agi > 23520:
            stateBracket = .06925
            margin = agi - 23520
            taxes += 1058.4 + margin * stateBracket
        elif agi > 15680:
            stateBracket = .06625
            margin = agi - 15680
            taxes += 568.4 + margin * stateBracket
        elif agi > 12544:
            stateBracket = .05625
            margin = agi - 12544
            taxes += 392 + margin * stateBracket
        elif agi > 9408:
            stateBracket = .04625
            margin = agi - 9408
            taxes += 246.96 + margin * stateBracket
        elif agi > 6272:
            stateBracket = .03625
            margin = agi - 6272
            taxes += 133.28 + margin * stateBracket
        elif agi > 3136:
            stateBracket = .03125
            margin = agi - 3136
            taxes += 35.28 + margin * stateBracket
        else:
            stateBracket = .01125
            taxes += agi * stateBracket
    else: # All other filing statuses
        if agi > 11760:
            stateBracket = .06925
            margin += agi - 11760
            taxes = 529.2 + margin * stateBracket
        elif agi > 7840:
            stateBracket = .06625
            margin = agi - 7840
            taxes += 284.2 + margin * stateBracket
        elif agi > 6272:
            stateBracket = .05625
            margin = agi - 6272
            taxes += 196 + margin * stateBracket
        elif agi > 4704:
            stateBracket = .04625
            margin = agi - 4704
            taxes += 123.48 + margin * stateBracket
        elif agi > 3136:
            stateBracket = .03625
            margin = agi - 3136
            taxes += 66.64 + margin * stateBracket
        elif agi > 1568:
            stateBracket = .03125
            margin = agi - 1568
            taxes += 17.64 + margin * stateBracket
        else:
            stateBracket = .01125
            taxes += agi * stateBracket