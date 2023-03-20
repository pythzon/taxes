'''
ARIZONA INCOME TAXES (2022)
https://azdor.gov/forms/individual/form-140-x-y-tables 

Single or Married Filing Separate
Taxable Income
Is over         But not over    Tax Rate
$0              $28,653         2.55%
$28,653                         2.98% + $731

Married Filing Joint or Head of Household
Taxable Income
Is over         But not over    Tax Rate
$0              $57,305         2.55%
$57,305                         2.98% + $1,461

DEDUCTIONS AND EXEMPTIONS
Federal deductions apply

DEPENDENT CREDIT
$100 per dependent
Married Filing Joint: $400,000 Threshold
Otherwise: $200,000 Threshold
If AGI - Threshold is greater than $19,000, you cannot claim the deduction
However, if AGI - Threshold > 0, the following formula applies:
[20 - Ceiling{((AGI - $19,000) / $1,000)}] / 20 * dependent credit

Table V. P. 22
If AGI - Threshold > 0 ->
$ 1-1,000      .95   $10,001-11,000   .45
$ 1,001-2,000  .90   $11,001-12,000   .40
$ 2,001-3,000  .85   $12,001-13,000   .35
$ 3,001-4,000  .80   $13,001-14,000   .30
$ 4,001-5,000  .75   $14,001-15,000   .25
$ 5,001-6,000  .70   $15,001-16,000   .20
$ 6,001-7,000  .65   $16,001-17,000   .15
$ 7,001-8,000  .60   $17,001-18,000   .10
$ 8,001-9,000  .55   $18,001-19,000   .05
$ 9,001-10,000 .50   $19,001+         .00

RECIRPOCAL AGREEMENTS
https://azdor.gov/businesses-arizona/withholding-tax/withholding-exceptions
California, Indiana, Oregon, and Virginia
'''
class Arizona:
    import math
    if resState in ['California', 'Indiana', 'Oregon', 'Virginia']:
        workState = resState
    
    # Ask for state deductions only in the solely state calculator prompt
    if stateDeductions == 0:
        stateDeductions = federalDeductions
    agi -= stateDeductions
    
    if dependents and (stateCredits == 0):
        stateCredits = 100 * dependents
        marriedThreshold = 400000
        otherThreshold = 200000

        if (maritalStatus == 'Married Filing Jointly' and agi > marriedThreshold) or (maritalStatus != 'Married Filing Jointly' and agi > otherThreshold):
            # Fully phased out
            if agi - marriedThreshold > 19000:
                stateCredits = 0
            else:
                stateCredits *= (20 - math.ceil((agi - marriedThreshold) / 1000)) / 20
    taxes -= stateCredits

    if maritalStatus in ['Married Filing Jointly', 'Head of Household']:
        if agi > 250000:
            stateBracket = .08
            margin = agi - 250000
            taxes += 10052.76 + margin * stateBracket
        elif agi > 163632:
            stateBracket = .045
            margin = agi - 163632
            taxes += 6166.2 + margin * stateBracket
        elif agi > 54544:
            stateBracket = .0417
            margin = agi - 54544
            taxes += 1617.23 + margin * stateBracket
        elif agi > 27272:
            stateBracket = .0334
            margin = agi - 27272
            taxes += 706.345 + margin * stateBracket
        else:
            stateBracket = 0.0259
            taxes += agi * stateBracket
    # Single or Married Filing Separate
    else:
        if agi > 500000:
            stateBracket = .08
            margin = agi - 500000
            taxes += 20105.52 + margin * stateBracket
        elif agi > 327263:
            stateBracket = .045
            margin = agi - 327263
            taxes += 12332.357 + margin * stateBracket
        elif agi > 109088:
            stateBracket = .0417
            margin = agi - 109088
            taxes += 3234.46 + margin * stateBracket
        elif agi > 54544:
            stateBracket = .0334
            margin = agi - 54544
            taxes += 1412.69 + margin * stateBracket
        else:
            stateBracket = 0.0259
            taxes += agi * stateBracket