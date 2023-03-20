'''
UTAH INCOME TAXES
https://incometax.utah.gov/paying/tax-rates
https://tax.utah.gov/forms/current/tc-40.pdf
4.85% of AGI

DEDUCTIONS
https://tax.utah.gov/forms/current/tc-40.pdf (Box 17)
Federal deductions apply prior to the following phaseout thresholds
6% of Federal deductions applies as a tax credit, not refundable
Single or Married Filing Separately: $15,548
Married Filing Jointly or Qualifying Widow(er): $31,096
Head of Household: $23,322
1.3% of AGI over the thresholds is added back to AGI

DEPENDENT DEDUCTION
https://tax.utah.gov/forms/current/tc-40.pdf (Box 2, 11)
$1,802 per dependent
'''

class Utah:
    stateBracket = .0485
    taxes = agi * stateBracket

    # Calculate credits for user
    if stateCredits != 0 and stateDeductions != 0:
        thresholds = {'Married Filing Jointly': 31096, 'Single': 15548, 'Head of Household': 23322}
        if stateDeductions == 0:
            stateDeductions = federalDeductions + 1802 * dependents
        
        # No Phaseout
        if agi < thresholds[maritalStatus]:
            taxes -= stateDeductions * .06
        
        # Phased out
        elif (agi - 31096) * .013 < stateDeductions *.06:
            taxes -= stateDeductions *.06 + (agi - 31096) * .013 
        # Otherwise, no deductions

        if taxes < 0:
            taxes = 0
            stateBracket = 0

    # User inputted credits in this case
    else:
        taxes -= stateCredits