'''
NEBRASKA INCOME TAXES 2023
https://revenue.nebraska.gov/sites/revenue.nebraska.gov/files/doc/2023_Circular_EN_8-429r2023_Whole_Book_11.pdf

Single or Head of Household
If the taxable income is:           
Over:       But not over:      The tax is:
$3,060      $5,990             $0 plus 2.26% of the amount over $3,060
$5,990      $19,470            $66.22 plus 3.22% of the amount over $5,990
$19,470     $28,210            $500.28 plus 4.91% of the amount over $19,470
$28,210     $35,820            $929.41 plus 6.20% of the amount over $28,210
$35,820     $67,270            $1,401.23 plus 6.39% of the amount over $35,820
$67,270                        $3,410.89  plus 6.75% of the amonut over $67,270

Married Filing Jointly or Qualifying Widow(er)
If the taxable income is:           
Over:       But not over:      The tax is:
$7,530      $11,610            $0 plus 2.26% of the amount over $7,530
$11,610     $28,910            $92.21 plus 3.22% of the amount over $11,610
$28,910     $44,980            $649.27 plus 4.91% of the amount over $28,910
$44,980     $55,810            $1,438.31 plus 6.20% of the amount over $44,980
$55,810     $74,010            $2,109.77 plus 6.39% of the amount over $55,810
$74,010                        $3,272.75  plus 6.75% of the amonut over $67,270

STANDARD DEDUCTION
https://revenue.nebraska.gov/sites/revenue.nebraska.gov/files/doc/2022_Ne_Individual_Income_Tax_Booklet_8-307-2022_final_6.pdf (P.9)
If you or your spourse are over 65:  Neither      One         Both
Single                               $7,350       $9,050      
Married Filing Jointly               $14,700      $18,100     $21,500
Married Filing Separately            $7,350       $8,750      $10,150
Head of Household                    $10,750      $12,450     

CREDITS
https://revenue.nebraska.gov/sites/revenue.nebraska.gov/files/doc/2022_Ne_Individual_Income_Tax_Booklet_8-307-2022_final_6.pdf (p.23-24)
$146 per filer and dependent (max 3 depednets)
'''

class Nebraska: 
    if stateCredits == 0:
        if dependends > 3:
            dependends = 3
        stateCredits = dependents * 146
        if maritalStatus == 'Married Filing Jointly':
            stateCredits = 292
        else:
            stateCredits = 146
    taxes = -stateCredits
        
    if maritalStatus == 'Married Filing Jointly':
        if stateDeductions == 0:
            stateDeductions = 14700
        agi -= stateDeductions

        if agi > 74010:
            stateBracket = .0675
            margin = agi - 74010
            taxes += 3272.75 + margin * stateBracket
        elif agi > 55810:
            stateBracket = .0639
            margin = agi - 55810
            taxes += 2109.77 + margin * stateBracket
        elif agi > 44980:
            stateBracket = .062
            margin = agi - 44980
            taxes += 1438.31 + margin * stateBracket
        elif agi > 28910:
            stateBracket = .0491
            margin = agi - 28910
            taxes += 549.41 + margin * stateBracket
        elif agi > 11610:
            stateBracket = .0322
            margin = agi - 11610
            taxes += 92.21 + margin * stateBracket
        elif agi > 7530:
            stateBracket = .0226
            margin = agi - 7530
            taxes += margin * stateBracket
    else:
        if stateDeductions == 0:
            if maritalStatus == 'Head of Household':
                stateDeductions = 10750
            # Single or Married Filing Separately
            else:
                stateDeductions = 7350
        agi -= stateDeductions

        if agi > 67720:
            stateBracket = .0675
            margin = agi - 67720
            taxes += 3410.89 + margin * stateBracket
        elif agi > 35820:
            stateBracket = .0639
            margin = agi - 35820
            taxes += 1401.23 + margin * stateBracket
        elif agi > 28210:
            stateBracket = .062
            margin = agi - 28210
            taxes += 929.41 + margin * stateBracket
        elif agi > 19470:
            stateBracket = .0491
            margin = agi - 19470
            taxes += 500.28 + margin * stateBracket
        elif agi > 5990:
            stateBracket = .0322
            margin = agi - 5990
            taxes += 66.22 + margin * stateBracket
        elif agi > 3060:
            stateBracket = .0226
            margin = agi - 3060
            taxes += margin * stateBracket