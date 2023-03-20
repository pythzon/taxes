'''
HAWAII INCOME TAXES
https://tax.hawaii.gov/forms/d_18table-on/ (Page Last Updated: December 19, 2022)
https://files.hawaii.gov/tax/forms/2018/18table-on.pdf (P. 14)

SINGLE TAXPAYERS AND MARRIED FILING SEPARATE RETURNS
If taxable income is:                   Your tax is:
Not over $2,400                         1.40% of taxable income
Over $2,400 but not over $4,800         $34 plus 3.20% over $2,400
Over $4,800 but not over $9,600         $110 plus 5.50% over $4,800
Over $9,600 but not over $14,400        $374 plus 6.40% over $9,600
Over $14,400 but not over $19,200       $682 plus 6.80% over $14,400
Over $19,200 but not over $24,000       $1,030 plus 7.20% over $19,200
Over $24,000 but not over $36,000       $1,354 plus 7.60% over $24,000
Over $36,000 but not over $48,000       $2,266 plus 7.90% over $36,000
Over $48,000 but not over $150,000      $3,214 plus 8.25% over $48,000
Over $150,000 but not over $175,000     $11,629 plus 9.00% over $150,000
Over $175,000 but not over $200,000     $13,879 plus 10.00% over $175,000
Over $200,000                           $16,379 plus 11.00% over $200,000 

MARRIED TAXPAYERS FILING JOINT RETURNS AND CERTAIN WIDOWS AND WIDOWERS
If taxable income is:                   Your tax is:
Not over $4,800                         1.40% of taxable income
Over $4,800 but not over $9,600         $67 plus 3.20% over $4,800
Over $9,600 but not over $19,200        $221 plus 5.50% over $9,600
Over $19,200 but not over $28,800       $749 plus 6.40% over $19,200
Over $28,800 but not over $38,400       $1,363 plus 6.80% over $28,800
Over $38,400 but not over $48,000       $2,016 plus 7.20% over $38,400
Over $48,000 but not over $72,000       $2,707 plus 7.60% over $48,000
Over $72,000 but not over $96,000       $4,531 plus 7.90% over $72,000
Over $96,000 but not over $300,000      $6,427 plus 8.25% over $96,000
Over $300,000 but not over $350,000     $23,257 plus 9.00% over $300,000
Over $350,000 but not over $400,000     $27,757 plus 10.00% over $350,000
Over $400,000                           $32,757 plus 11.00% over $400,000
    
UNMARRIED HEADS OF HOUSEHOLD
If taxable income is:                   Your tax is:
Not over $3,600                         1.40% of taxable income
Over $3,600 but not over $7,200         $50 plus 3.20% over $3,600
Over $7,200 but not over $14,400        $166 plus 5.50% over $7,200
Over $14,400 but not over $21,600       $562 plus 6.40% over $14,400
Over $21,600 but not over $28,800       $1,022 plus 6.80% over $21,600
Over $28,800 but not over $36,000       $1,512 plus 7.20% over $28,800
Over $36,000 but not over $54,000       $2,030 plus 7.60% over $36,000
Over $54,000 but not over $72,000       $3,398 plus 7.90% over $54,000
Over $72,000 but not over $225,000      $4,820 plus 8.25% over $72,000
Over $225,000 but not over $262,500     $17,443 plus 9.00% over $225,000
Over $262,500 but not over $300,000     $20,818 plus 10.00% over $262,500
Over $300,000                           $24,568 plus 11.00% over $300,000

DEDUCTIONS AND EXEMPTIONS
https://files.hawaii.gov/tax/news/pubs/22outline.pdf
STANDARD DEDUCTION:
MARRIED FILING JOINTLY OR SURVIVING SPOUSE WITH DEPENDENT CHILD: $4,400
SINGLE OR MARRIED FILING SEPARATELY: $2,200
HEAD OF HOUSEHOLD: $3,212

https://files.hawaii.gov/tax/news/pubs/FastTaxRefGuide_2017.pdf
PERSONAL EXEMPTION: $1,144 PER PERSON
Age 65 or older: $1,250 per married person, $1,550 per non-married person

HAWAII CAPITAL GAINS TAXES
Fluid situation, but it's currenlty 7.25% for now. The following testimony discusses a proposal to increase it to 9%

https://www.grassrootinstitute.org/2023/02/hb337-increasing-tax-on-capital-gains-a-bad-risk/
Current Rate: 7.25%
Proposed Rate: 9%
'''
class Hawaii:
    taxes = capitalGains * .0725
    taxes -= stateCredits

    if maritalStatus == "Married":
        if stateDeductions == 0:
            stateDeductions = 4400 + (2 + dependents) * 1144 + numOver65 * 1250
        if agi > 400000:
            stateBracket = .11
            margin = agi - 400000
            taxes += 32757.2 + margin * stateBracket
        elif agi > 350000:
            stateBracket = .1
            margin = agi - 350000
            taxes += 27757.2 + margin * stateBracket
        elif agi > 300000:
            stateBracket = .09
            margin = agi - 300000
            taxes += 23257.2 + margin * stateBracket
        elif agi > 96000:
            stateBracket = .0825
            margin = agi - 96000
            taxes += 6427.2 + margin * stateBracket
        elif agi > 72000:
            stateBracket = .079
            margin = agi - 72000
            taxes += 4531.2 + margin * stateBracket
        elif agi > 48000:
            stateBracket = .076
            margin = agi - 48000
            taxes += 2707.2 + margin * stateBracket
        elif agi > 38400:
            stateBracket = .072
            margin = agi - 38400
            taxes += 2016 + margin * stateBracket
        elif agi > 28800:
            stateBracket = .068
            margin = agi - 28800
            taxes += 1363.2 + margin * stateBracket
        elif agi > 19200:
            stateBracket = .064
            margin = agi - 19200
            taxes += 748.8 + margin * stateBracket
        elif agi > 9600:
            stateBracket = .055
            margin = agi - 9600
            taxes += 220.8 + margin * stateBracket
        elif agi > 4800:
            stateBracket = .032
            margin = agi - 4800
            taxes += 67.2 + margin * stateBracket
        else:
            stateBracket = .014
            taxes += agi * stateBracket
    
    elif maritalStatus == "Head of Household":
        if stateDeductions == 0:
            stateDeductions = 3212 + (1 + dependents) * 1144 + numOver65 * 1550
        agi -= stateDeductions

        if agi > 300000:
            stateBracket = .11
            margin = agi - 300000
            taxes += 24568+ margin * stateBracket
        elif agi > 262500:
            stateBracket = .1
            margin = agi - 262500
            taxes += 20818 + margin * stateBracket
        elif agi > 225000:
            stateBracket = .09
            margin = agi - 225000
            taxes += 17443 + margin * stateBracket
        elif agi > 72000:
            stateBracket = .0825
            margin = agi - 72000
            taxes += 4820 + margin * stateBracket
        elif agi > 54000:
            stateBracket = .079
            margin = agi - 54000
            taxes += 3398 + margin * stateBracket
        elif agi > 36000:
            stateBracket = .076
            margin = agi - 36000
            taxes += 2030 + margin * stateBracket
        elif agi > 28800:
            stateBracket = .072
            margin = agi - 28800
            taxes += 1512 + margin * stateBracket
        elif agi > 21600:
            stateBracket = .068
            margin = agi - 21600
            taxes += 1022 + margin * stateBracket
        elif agi > 14400:
            stateBracket = .064
            margin = agi - 14400
            taxes += 562 + margin * stateBracket
        elif agi > 7200:
            stateBracket = .055
            margin = agi - 7200
            taxes += 166 + margin * stateBracket
        elif agi > 3600:
            stateBracket = .032
            margin = agi - 3600
            taxes += 50 + margin * stateBracket
        else:
            stateBracket = .014
            taxes += agi * stateBracket

    else: # Single and Married Filing Separately
        if stateDeductions == 0:
            stateDeductions = 2200 + (1 + dependents) * 1144 + numOver65 * 1550
        agi -= stateDeductions

        if agi > 200000:
            stateBracket = .11
            margin = agi - 200000
            taxes += 16378.6 + margin * stateBracket
        elif agi > 175000:
            stateBracket = .1
            margin = agi - 175000
            taxes += 13878.6 + margin * stateBracket
        elif agi > 150000:
            stateBracket = .09
            margin = agi - 150000
            taxes += 11628.6 + margin * stateBracket
        elif agi > 48000:
            stateBracket = .0825
            margin = agi - 48000
            taxes += 3213.6 + margin * stateBracket
        elif agi > 36000:
            stateBracket = .079
            margin = agi - 36000
            taxes += 2265.6 + margin * stateBracket
        elif agi > 24000:
            stateBracket = .076
            margin = agi - 24000
            taxes += 1353.6 + margin * stateBracket
        elif agi > 19200:
            stateBracket = .072
            margin = agi - 19200
            taxes += 1008 + margin * stateBracket
        elif agi > 14400:
            stateBracket = .068
            margin = agi - 14400
            taxes += 681.6 + margin * stateBracket
        elif agi > 9600:
            stateBracket = .064
            margin = agi - 9600
            taxes += 374.4 + margin * stateBracket
        elif agi > 4800:
            stateBracket = .055
            margin = agi - 4800
            taxes += 110.4 + margin * stateBracket
        elif agi > 2400:
            stateBracket = .032
            margin = agi - 2400
            taxes += 33.6 + margin * stateBracket
        else:
            stateBracket = .014
            taxes += agi * stateBracket