'''
OREGON INCOME TAXES
https://www.oregon.gov/dor/programs/individuals/Pages/PIT.aspx

-FULL YEAR RESIDENTS
https://www.oregon.gov/dor/programs/individuals/Documents/Full%20year%20resident,%20Form%20OR-40%20filers.pdf

-PART YEAR RESIDENTS
https://www.oregon.gov/dor/programs/individuals/Documents/Part-year%20and%20nonresident,%20Form%20OR-40-P%20and%20OR-40-N%20filers.pdf.pdf

2022 Tax rate charts Chart S:
For persons filing single or married filing separately— 
If your taxable income is not over $3,750 .......................................................................................your tax is 4.75% of taxable income
If your taxable income is over $3,750 but not over $9,450 .............................your tax is $178 plus 6.75% of excess over $3,750
If your taxable income is over $9,450 but not over $125,000 ........................your tax is $563 plus 8.75% of excess over $9,450
If your taxable income is over $125,000 ........................................................your tax is $10,674 plus 9.9% of excess over $125,000
    
Chart J: For persons filing jointly, head of household, or qualifying surviving spouse with dependent child—
If your taxable income is not over $7,500 .......................................................................................your tax is 4.75% of taxable income
If your taxable income is over $7,500 but not over $18,900 ...........................your tax is $356 plus 6.75% of excess over $7,500
If your taxable income is over $18,900 but not over $250,000 ................your tax is $1,126 plus 8.75% of excess over $18,900
If your taxable income is over $250,000....................................................... your tax is $21,347 plus 9.9% of excess over $250,000

STANDARD DEDUCTIONS
https://www.oregon.gov/dor/forms/FormsPubs/form-or-40_101-040_2022.pdf (P. 3)
Married filing jointly or qualifying widow(er): $4,840
Single or married filing seperately : $2,420
Head of household: $3,895

DEPENDENT AND AGE OVER 65 CREDITS
https://www.oregon.gov/dor/forms/FormsPubs/form-or-40_101-040_2022.pdf (P. 4)
$219 per dependent, if income is below $100,00 ($200,000 for married filing jointly)
'''
class Oregon:
    if maritalStatus in ['Married Filing Jointly', 'Head of Household']:
        if stateDeductions == 0:
            if maritalStatus == 'Married Filing Jointly':
                stateDeductions = 4840
            else:
                stateDeductions = 3895
        agi -= stateDeductions

        if stateCredits == 0 and agi < 200000:
                stateCredits = (219 * (2 + numOver65) + (dependents * 219))
        taxes = -stateCredits

        if agi > 250000:
            stateBracket = .099
            margin = agi - 250000
            taxes += 21361 + margin * stateBracket
        elif agi > 18400:
            stateBracket = .0875
            margin = agi - 18400
            taxes += 1096 + margin * stateBracket
        elif agi > 7300:
            stateBracket = .0675
            margin = agi - 7300
            taxes += 346.75 + margin * stateBracket
        else:
            stateBracket = .0475
            taxes += agi * stateBracket
    
    else: # Single or Married Filing Separately
        if stateDeductions == 0:
            stateDeductions = 2420
        agi -= stateDeductions

        if stateCredits == 0 and agi < 100000:
            stateCredits = (219 * (1 + numOver65) + (dependents * 219))
        taxes = -stateCredits

        if agi > 125000:
            stateBracket = .099
            margin = agi - 125000
            taxes += 10680.5 + margin * stateBracket
        elif agi > 9200:
            stateBracket = .0875
            margin = agi - 9200
            taxes += 548 + margin * stateBracket
        elif agi > 3650:
            stateBracket = .0675
            margin = agi - 3650
            taxes += 173.375 + margin * stateBracket
        else:
            stateBracket = .0475
            taxes += agi * stateBracket