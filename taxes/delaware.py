''' 
DELAWARE INCOME TAXES (2022)
https://revenue.delaware.gov/software-developer/tax-rate-changes/

Taxable income range	        Base	    Rate
At least	But less than
$0	        $2,000	            $0	        0%
$2,000	    $5,000	            $0	        2.2%
$5,000	    $10,000	            $66	        3.9%
$10,000	    $20,000	            $261	    4.8%
$20,000	    $25,000	            $741	    5.2%
$25,000	    $60,000	            $1,001	    5.55%
$60,000		                    $2943.50	6.6%

CREDITS AND DEDUCTIONS
https://revenuefiles.delaware.gov/2022/PIT-RES_TY22_2022-01_PaperInteractive.pdf
https://revenuefiles.delaware.gov/2022/PIT-RES_TY22_2022-02_Instructions.pdf

LINE 19 - STANDARD DEDUCTION 
MARRIED - $6,500
OTHERWISE - $3,250

LINE 26A. - PERSONAL CREDITS
NUMBER OF EXEMPTIONS * $110 (Each filer, dependent, and spouse over 60)

LINE 30
CHILD TAX CARE CREDIT - 50% OF FEDERAL CREDIT

LOCAL INCOME TAXES
https://www.newcastlede.gov/DocumentCenter/View/20147/City-of-Wilmington-Wage-Tax-Information-PDF
Wilmington 1.25% Gross Wages

CAPITAL GAINS
https://revenue.delaware.gov/frequently-asked-questions/personal-income-tax-faqs/
Capital gains are taxed as ordinary income.
'''

class Delaware:
    if stateDeductions == 0:
        if maritalStatus == 'Married Filing Jointly':
            stateDeductions = 6500
        else: # All other filers
            stateDeductions = 3250
    agi -= stateDeductions

    if stateCredits == 0:
        if maritalStatus == 'Married Filing Jointly':
            stateCredits = (2 + dependents + numOver65) * 110
        else:
            stateCredits = (1 + dependents + numOver65) * 110
    taxes = -stateCredits

    if agi > 60000:
        stateBracket = .066
        margin = agi - 60000
        taxes = 2943.50 + margin * stateBracket
    elif agi > 25000:
        stateBracket = .0555
        margin = agi - 25000
        taxes = 1001 + margin * stateBracket
    elif agi > 20000:
        stateBracket = .052
        margin = agi - 20000
        taxes = 741 + margin * stateBracket
    elif agi > 10000:
        stateBracket = .048
        margin = agi - 10000
        taxes = 261 + margin * stateBracket
    elif agi > 5000:
        stateBracket = .039
        margin = agi - 5000
        taxes = 66 + margin * stateBracket
    elif agi > 2000:
        stateBracket = .022
        margin = agi - 2000
        taxes = margin * stateBracket
    if county == 'Wilmington':
        # GROSS WAGES, NOT AGI
        taxes += .0125 * salary