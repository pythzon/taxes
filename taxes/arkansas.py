'''
ARKANSAS INCOME TAXES (2022)
https://www.arkansasedc.com/why-arkansas/business-climate/tax-structure/personal-income-tax

PERSONAL INCOME TAX RATES FOR TAX YEAR BEGINNING JANUARY 1, 2022
Income Tax Rate for Individuals with Net Income of Less Than or Equal to $84,500	 
$0      - $4,999	0.0%
$5,000  - $9,999	2.0%
$10,000 - $14,299	3.0%
$14,300 - $23,599	3.4%
$23,600 - $84,500	4.9%

Income Tax Rate for Individuals with a Net Income Greater Than $84,500	 
$0      - $4,300	2.0%
$4,301  - $8,500	4.0%
$8,501+

STANDARD DEDUCTION
https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/2022_AR1000F_and_AR1000NR_Instructions.pdf (P.14)
Married Filing Jointly: $4,540
All Other Filers: $2,270

CREDITS
https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/2022_AR1000F_FullYearResidentIndividualIncomeTaxReturn.pdf (Line 7a.)
https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/2022_AR1000F_and_AR1000NR_Instructions.pdf (P.12) 
$29 per individual/spouse, dependent, and bonus for each spouse over 65

CAPITAL GAINS TAXES
https://www.arkansasedc.com/why-arkansas/business-climate/tax-structure/capital-gains-tax-reduction
50% of net capital gains are deducted, as is any net capital gain in excess of $10M
'''
class Arkansas:
    if shortCapitalGains + longCapitalGains > 10000000:
        capitalGains = 5000000
        capitalGains += shortCapitalGains + longCapitalGains - 10000000 
        agi -= capitalGains
    else:
        capitalGains = shortCapitalGains + longCapitalGains
        agi -= capitalGains* .5
        
    if stateDeductions == 0:
        if maritalStatus == 'Married':
            stateDeductions = 4540
        else:
            stateDeductions = 2270       
    agi -= stateDeductions

    if stateCredits == 0:
        if maritalStatus == 'Married':
            # $58 credit for married couples
            stateCredits = 58
        else:
            # $29 credit for individuals
            stateCredits = 29
        # $29 credit per dependent and each spouse over 65
        stateCredits = 29 * (dependents + numOver65)
    taxes = -stateCredits
    
    if agi > 84500:
        stateBracket = .049
        margin = agi - 84500
        # $254 = $4,300 * 2% + $4,200 * 4%
        taxes += 254 + (agi - 8500) * stateBracket
    elif agi > 23600:
        stateBracket = .049
        margin = agi - 23600
        taxes += 545.2 + margin * stateBracket
    elif agi > 14300:
        stateBracket = .034
        margin = agi - 14300
        taxes += 229 + margin * stateBracket
    elif agi > 10000:
        stateBracket = .03
        margin = agi - 10000
        taxes += 100 + margin * stateBracket
    elif agi > 5000:
        stateBracket = .02
        taxes += (agi - 5000) * stateBracket
    else:
        stateBracket = 0