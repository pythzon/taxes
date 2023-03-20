'''
MAINE INCOME TAXES
https://www.maine.gov/revenue/tax-return-forms/individual-income-tax-2022
https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/ind_tax_rate_sched_2022.pdf

For Single Individuals and Married Persons Filing Separate Returns 
If the taxable income is:           The tax is:  
Less than $23,000                   5.8% of Maine taxable income
$23,000 but less than $54,450       $1,334 plus 6.75% of excess over $23,000
$54,450 or more                     $3,457 plus 7.15% of excess over $54,450
    
Unmarried or Legally Separated Individuals who Qualify as Heads of Household
If the taxable income is:           The tax is:  
Less than $34,500                   5.8% of Maine taxable income
$34,500 but less than $81,700       $2,001 plus 6.75% of excess over $34,500
$81,700 or more                     $5,187 plus 7.15% of excess over $81,700       

Married Individuals and Surviving Spouses Filing Joint Returns
If the taxable income is:           The tax is:  
Less than $46,000                   5.8% of Maine taxable income  
$46,000 but less than $108,900      $2,668 plus 6.75% of excess over $46,000
$108,900 or more                    $6,914 plus 7.15% of excess over $108,900 

DEDUCTIONS/EXEMPTIONS
TODO I AM NOT READING THE LINE 17 AND 18 TABLES CORRECTLY OR MAINE IS RUN BY DEGENERATES
https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/22_1040me_book_gen_instruc_revisedFeb23.pdf (P. 4)
STANDARD DEDUCTION MATCHES FEDERAL
Exemptions -> $4,450 per individual/spouse, dependent, and individual/spouse over 65
'''

class Maine:
    if maritalStatus == 'Married Filing Seprately':
        maritalStatus = 'Single'
        
    taxes = -stateCredits

    if stateDeductions == 0:
        thresholds = {'Married Filing Jointly': [171700, 150000], 'Single': [85850, 75000], 'Head of Household': [128750, 112500]}
        # No phaseout
        if agi < thresholds[maritalStatus][0]:
            stateDeductions = federalDeductions + (2 + dependents + numOver65) * 4450
        else:
            agi - thresholds[maritalStatus][1]
    agi -= stateDeductions

    if maritalStatus == 'Married Filing Jointly':
        if agi > 108900:
            stateBracket = .0715
            margin = agi - 108900
            taxes += 6914 + margin * stateBracket
        elif agi > 46000:
            stateBracket = .0675
            margin = agi - 46000
            taxes += 2668 + margin * stateBracket
        else:
            stateBracket = .058
            taxes += agi * stateBracket

    elif maritalStatus == 'Head of Household':
        if agi > 81700:
            stateBracket = .0715
            margin = agi - 81700
            taxes += 5187 + margin * stateBracket
        elif agi > 34500:
            stateBracket = .0675
            margin = agi - 34500
            taxes += 2001 + margin * stateBracket
        else:
            stateBracket = .058
            taxes += agi * stateBracket
    else: # Single or Married Filing Separately
        if agi > 54450:
            stateBracket = .0715
            margin = agi - 54450
            taxes += 3457 + margin * stateBracket
        elif agi > 23000:
            stateBracket = .0675
            margin = agi - 23000
            taxes += 1334 + margin * stateBracket
        else:
            stateBracket = .058
            taxes += agi * stateBracket
