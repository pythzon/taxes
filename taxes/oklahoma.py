'''
OKLAHOMA INCOME TAXES
https://oklahoma.gov/content/dam/ok/en/tax/documents/resources/publications/businesses/withholding-tables/WHTables-2022.pdf
Single or Married Filing Seperately
If the amount of wages is:
Over        but less than   The amount of income tax to withhold is:
$0          $6,350          $0
$6,350      $7,350          $0 + 0.25% of the excess over $6,350
$7,350      $8,850          $2.50 + 0.75% of the excess over $7,350
$8,850      $10,100         $13.75 + 1.75% of the excess over $8,850
$10,100     $11,250         $35.63 + 2.75% of the excess over $10,100
$11,250     $13,550         $67.25 + 3.75% of the excess over $11,250
$13,550                     $153.50 + 4.75% of the excess over $13,550 

Married Filing Jointly, Head of Household, and Qualifying Widower
If the amount of wages is:
Over        but less than   The amount of income tax to withhold is:
$0          $12,700         $0   
$12,700     $14,700         $0 + 0.25% of the excess over $12,700
$14,700     $17,700         $5.00 + 0.75% of the excess over $14,700
$17,700     $20,200         $27.50 + 1.75% of the excess over $17,700
$20,200     $22,500         $71.25 + 2.75% of the excess over $20,200
$22,500     $24,900         $134.50 + 3.75% of the excess over $22,500
$24,900                     $224.50 + 4.75% of the excess over $24,900

DEDUCTIONS
https://oklahoma.gov/content/dam/ok/en/tax/documents/forms/individuals/current/511-NR-Pkt.pdf
Oklahoma allows $1,000 for each exemption claimed at the top of page 1 of Form 511-NR.
This includes dependents, each spuse, and another exemption for each spouse above the age of 65.

STANDARD DEDUCTIONS (P. 13) (Built into tax rates)
Single or Married Filing Separately: $6,350
Married Filing Jointly or Qualifying Widow(er): $12,700
Head of Household: $9,350
'''

class Oklahoma:
    taxes = -stateCredits

    if maritalStatus == 'Married Filing Jointly':
        if stateDeductions == 0:
            stateDeductions = 12700 + (2 + dependents + numOver65) * 1000
        agi -= stateDeductions

        if agi > 24900:
            stateBracket = .0475
            margin = agi - 24900
            taxes += 224.5 + margin * stateBracket
        elif agi > 22500:
            stateBracket = .0375
            margin = agi - 22500
            taxes += 134.5 + margin * stateBracket
        elif agi > 20200:
            stateBracket = .0275
            margin = agi - 20200
            taxes += 71.25 + margin * stateBracket
        elif agi > 17700:
            stateBracket = .0175
            margin = agi - 17700
            taxes += 27.5 + margin * stateBracket
        elif agi > 14700:
            stateBracket = .0075
            margin = agi - 14700
            taxes += 5 + margin * stateBracket
        elif agi > 12700:
            stateBracket = .0025
            margin = agi - 12700
            taxes += margin * stateBracket
    else:
        if stateDeductions == 0:
            stateDeductions = (1 + dependents + numOver65) * 1000
            if maritalStatus in ['Single', 'Married Filing Separately']:
                stateDeductions += 6350
            # Head of Household
            else:
                stateDeductions += 9350
        agi -= stateDeductions

        if agi > 13550:
            stateBracket = .0475
            margin = agi - 13550
            taxes += 153.5 + margin * stateBracket
        elif agi > 11250:
            stateBracket = .0375
            margin = agi - 11250
            taxes += 67.25 + margin * stateBracket
        elif agi > 10100:
            stateBracket = .0275
            margin = agi - 10100
            taxes += 35.63 + margin * stateBracket
        elif agi > 8850:
            stateBracket = .0175
            margin = agi - 8850
            taxes += 13.75 + margin * stateBracket
        elif agi > 7350:
            stateBracket = .0075
            margin = agi - 7350
            taxes += 2.5 + margin * stateBracket
        elif agi > 6350:
            stateBracket = .0025
            margin = agi - 6350
            taxes += margin * stateBracket
    