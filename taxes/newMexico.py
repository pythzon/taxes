'''
NEW MEXICO INCOME TAXES (2022)
https://klvg4oyd4j.execute-api.us-west-2.amazonaws.com/prod/PublicFiles/34821a9573ca43e7b06dfad20f5183fd/fdf3c548-8aba-4b9c-9eb4-bb564c716015/FYI-104.pdf

SINGLE OR MARRIED FILING SEPARATELY
If the amount                                                             
Is over      but not over     Tax is                                   
$6,925       $12,425          1.7% of income over $6,925
$12,425      $17,925          $93.50 + 3.2% of ncome over $12,425
$17,925      $22,925          $269.5 + 4.7% of income over $17,925
$22,925      $216,925         $504.5 + 4.9% if income over $22,925
$216,925                      $10,010.5 + 5.9% of income over 216,925

MARRIED OR HEAD OF HOUSEHOLD
If the amount                                                             
Is over      but not over     Tax is                                   
$13,850      $21,850          1.7% of income over $13,850
$21,850      $29,850          $136 + 3.2% of income over $21,850
$29,850      $37,850          $392 + 4.7% of income over $29,850
$37,850      $328,850         $768 + 4.9% if income over $37,850
$328,850                      $15,027 + 5.9% of income over 216,925

DEDUCTIONS CREDITS TODO Sorry I'm Dumb
https://klvg4oyd4j.execute-api.us-west-2.amazonaws.com/prod/PublicFiles/34821a9573ca43e7b06dfad20f5183fd/0bf943fd-652e-4400-bb1b-cd8397eb5a95/2022pit-adj.pdf (Form)
https://klvg4oyd4j.execute-api.us-west-2.amazonaws.com/prod/PublicFiles/34821a9573ca43e7b06dfad20f5183fd/2f1a6781-9534-4436-b427-1557f9592099/2022pit-adj-ins.pdf (Instructions)

SOCIAL SECURITY IS UNTAXED (Line 24. of PIT)

CAPITAL GAINS TAXES
https://klvg4oyd4j.execute-api.us-west-2.amazonaws.com/prod/PublicFiles/34821a9573ca43e7b06dfad20f5183fd/1afc56af-ea90-4d48-82e5-1f9aeb43255a/PITbook2022.pdf
The first $1,000 of net capital gains are deducted or the greater of 40% of net capital gains are deducted
'''
class NewMexico:
    if shortCapitalGains + longCapitalGains < 1000:
        pass
    # $1000 is deducted in this case
    elif shortCapitalGains + longCapitalGains < 2500:
        agi += shortCapitalGains + longCapitalGains - 1000
    # 40% of the gains are deducted
    elif shortCapitalGains + longCapitalGains > 2500:
        agi += (shortCapitalGains + longCapitalGains) * .6

    
    taxes = -stateCredits
    
    # TODO verify credits and deductions
    # $4000 dependent credit for at most one dependent
    if stateDeductions == 0:
        stateDeductions = federalDeductions
        if dependents:
            stateDeductions += 4000
    agi -= stateDeductions
    

    if maritalStatus == 'Married Filing Jointly':
        if agi > 328850:
            stateBracket = .059
            margin = agi - 315000
            taxes += 15027 + margin * stateBracket
        elif agi > 37850:
            stateBracket = .049
            margin = agi - 37850
            taxes += 768 + margin * stateBracket
        elif agi > 29850:
            stateBracket = .047
            margin = agi - 29850
            taxes += 392 + margin * stateBracket
        elif agi > 21850:
            stateBracket = .032
            margin = agi - 21850
            taxes += 136 + margin * stateBracket
        elif agi > 13850:
            stateBracket = .017
            taxes += agi * stateBracket
    
    else: # All other filing statuses
        if agi > 216925:
            stateBracket = .059
            margin = agi - 216925
            taxes += 10010.5 + margin * stateBracket
        elif agi > 22925:
            stateBracket = .049
            margin = agi - 22925
            taxes += 504.5 + margin * stateBracket
        elif agi > 17925:
            stateBracket = .047
            margin = agi - 17925
            taxes += 269.5 + margin * stateBracket
        elif agi > 12425:
            stateBracket = .032
            margin = agi - 12425
            taxes += 93.5 + margin * stateBracket
        elif agi > 6925:
            stateBracket = .017
            taxes += agi * stateBracket