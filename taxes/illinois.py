'''
ILLINOIS INCOME TAXES
https://tax.illinois.gov/research/taxrates/income.html#IndividualIncome
4.95% on all income

DEDUCTIONS
https://tax.illinois.gov/content/dam/soi/en/web/tax/forms/incometax/documents/currentyear/individual/il-1040-instr.pdf (P.8)
$2,425 Per Exemption (Individuals and Dependents)
Maximum income of $500,000 for joint filers and $250,000 for all other filers

RECIPROCAL AGREEMENTS
https://tax.illinois.gov/questionsandanswers/12.html
https://tax.illinois.gov/content/dam/soi/en/web/tax/forms/incometax/documents/currentyear/individual/il-1040-instr.pdf
(P.3) Iowa, Kentucky, Michigan, or Wisconsin
'''

def illinois():
    if resState in ['Iowa', 'Kentucky', 'Michigan', 'Wisconsin']:
        workState = resState

    if stateDeductions == 0:
        # Cannot claim personal exemption if AGI above 500k
        if maritalStatus == 'Married Filing Jointly' and agi < 500000:
            stateDeductions = 4850 + (dependents * 2425)
        
        # Cannot claim personal exemption if AGI above 250k for other filers
        elif agi < 250000:
            stateDeductions = 2425 + (dependents * 2425)
    agi -= stateDeductions

    taxes = -stateCredits

    stateBracket = .0495
    taxes += agi * stateBracket
