'''
NORTH CAROLINA INCOME TAXES (2023)
https://www.ncdor.gov/taxes-forms/tax-rate-schedules

2022 -> 4.99%
2023 -> 4.75%
2024 -> 4.6%
2025 -> 4.5%
2026 -> 4.25%
2027+ -> 4%

STATE DEDUCTIONS (2022)
https://www.ncdor.gov/taxes-forms/individual-income-tax/north-carolina-standard-deduction-or-north-carolina-itemized-deductions
f your filing status is:	                                    Your standard deduction is:
Single	                                                        $12,750
Married Filing Jointly/Qualifying Widow(er)/Surviving Spouse	$25,500
Married Filing Separately	 
    Spouse does not claim itemized deductions                   $12,750
    Spouse claims itemized deductions                           $0
Head of Household	                                            $19,125
'''

class NorthCarolina:
    if stateDeductions == 0:
        if maritalStatus == 'Married Filing Jointly':
            stateDeductions = 25500
        elif maritalStatus == 'Head of Household':
            stateDeductions = 19125
        # SINGLE OR MARRIED FILING SEPARATELY
        else:
            stateDeductions = 12750
    agi -= stateDeductions

    taxes = -stateCredits

    stateBracket = .0475
    taxes += agi * stateBracket