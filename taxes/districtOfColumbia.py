'''
DISTRICT OF COLUMBIA INCOME TAXES
https://otr.cfo.dc.gov/page/dc-individual-and-fiduciary-income-tax-rates
Tax Rates: The tax rates for tax years beginning after 12/31/2021 are:

If the taxable income is:	The tax is:
Not over $10,000	4% of the taxable income.
Over $10,000 but not over $40,000	$400, plus 6% of the excess over $10,000.
Over $40,000 but not over $60,000	$2,200, plus 6.5% of the excess over $40,000.
Over $60,000 but not over $250,000	$3,500, plus 8.5% of the excess over $60,000.
Over $250,000 but not over $500,000	$19,650, plus 9.25% of the excess over $250,000.
Over $500,000 but not over $1,000,000	$42,775, plus 9.75% of the excess above $500,000.
Over $1,000,000	$91,525, plus 10.75% of the excess above $1,000,000.

DEDUCTIONS
https://otr.cfo.dc.gov/page/individual-income-tax-filing-faqs

RECIRPOCAL AGREEMENTS
https://otr.cfo.dc.gov/page/individual-income-special-circumstances-faqs
Only D.C. residents pay D.C. taxes
'''

class DistrictOfColumbia:
    if resState != 'District of Columbia':
        workState = resState    

    if stateDeductions == 0:
        stateDeductions = federalDeductions
    agi -= stateDeductions

    taxes = -stateCredits

    if agi > 1000000:
        stateBracket = .0895
        margin = agi - 1000000
        taxes += 85025 + margin * stateBracket
    elif agi > 350000:
        stateBracket = .0875
        margin = agi - 350000
        taxes += 28150 + margin * stateBracket
    elif agi > 60000:
        stateBracket = .085
        margin = agi - 60000
        taxes += 3500 + margin * stateBracket
    elif agi > 40000:
        stateBracket = .065
        margin = agi - 40000
        taxes += 2200 + margin * stateBracket
    elif agi > 10000:
        stateBracket = .06
        margin = agi - 10000
        taxes += 400 + margin * stateBracket
    else:
        stateBracket = .04
        taxes += agi * stateBracket
