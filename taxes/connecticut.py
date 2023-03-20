'''
CONNECTICUT INCOME TAX
https://portal.ct.gov/-/media/DRS/Forms/2022/Income/2022-CT-1040-Instructions_1222.pdf (Table B)
https://www.cga.ct.gov/2022/rpt/pdf/2022-R-0108.pdf 
https://www.cga.ct.gov/current/pub/chap_229.htm#sec_12-703 
Connecticut Taxable Income
Tax Rate    Single and Married Filing Separately   Head of Household        Married Filing Jointly
3%          $0 to $10,000                          $0 to $16,000             $0 to 20,000 
5%          $10,001 to $50,000                     $16,001 to $80,000        $20,001 to $100,000
5.5%        $50,001 to $100,000                    $80,001 to $160,000       $100,001 to $200,000
6%          $100,001 to $200,000                   $160,001 to $320,000      $200,001 to $400,000
6.5%        $200,001 to $250,000                   $320,001 to $400,000      $400,001 to $500,000
6.9%        $250,001 to $500,000                   $400,001 to $800,000      $500,01 to $1,000,000
6.99%       > $500,000                             > $800,000                > $1,000,000

DEDUCTIONS AND CREDITS
https://portal.ct.gov/-/media/DRS/Forms/2022/Income/2022-CT-1040-Instructions_1222.pdf
Table A - Personal Exemption
Single      Married Filing Separately        Married Filing Jointly          Head of Household
$15,000     $12,000                          $24,000                         $19,000
If AGI < 2 * Exemption, then full amount of exemption is allowed, otherwise the exemption is phased out beginning at 2 * Exemption.
The following phase out formula applies (the exemption cannot be negative):
Final Exemption = Exemption - ceiling{(AGI - 2 * Exemption) / 1,000} * 1,000

Table C - 3% Tax Rate Phase-Out Add-Back
Single                                  Married Filing Separately               Married Filing Jointly                   Head of Household
AGI < 56,500 -> 0                       AGI < 50,250 -> 0                       AGI < 100,500 -> 0                       AGI < 78,500 -> 0
AGI > 56,500:                           AGI > 50,250:                           AGI > 100,500:                           AGI > 78,500:
ceiling{(AGI - 56,500) / 5,000} * 20    ceiling{(AGI - 50,250) / 2,500} * 20    ceiling{(AGI - 100,500) / 5,000} * 40    ceiling{(AGI - 78,500) / 4,000} * 32
max -> 200 at 101,500+                  max -> 200 at 72,750+                   max 400 at 145,500_                      max 320 at 114,500+

Table D - Tax Recapture
SIngle and Married Filing Separately        Married Filing Jointly                  Head of Household
200,000 < AGI < 345,000:                    400,000 < AGI < 690,000:                320,000 < AGI < 552,000:
celing{(AGI - 200,000)/5,000} * 90          celing{(AGI - 400,000)/10,000} * 180    celing{(AGI - 320,000)/8,000} * 140
345,000 < AGI < 500,000:                    690,000 < AGI < 1,000,000:              552,000 < AGI < 800,000:
2,700                                       5,500                                   4,200
490,000 < AGI < 540,000:                    1,000,000 < AGI < 10,080,000:           800,000 < AGI < 864,000:
celing{(AGI - 500,000)/5,000} * 50          celing{(AGI - 1,000,000)/10,000} * 100  celing{(AGI - 800,000)/8,000} * 80
Max Recapture -> 3,150 at 540,00+           Max Recapture -> 6,300 at 1,080,000+    Max Recapture -> 4,920 at 864,000+

Table E - Personal Tax Credits (Percentage of Federal EIC)
SINGLE AND MARRIED FILING SEPARATELY
Adjusted Gross Income               Amount of Credit
Over $15,000, but not over $18,800  75%
Over $18,800, but not over $19,300  70%
Over $19,300, but not over $19,800  65%
Over $19,800, but not over $20,300  60%
Over $20,300, but not over $20,800  55% 
Over $20,800, but not over $21,300  50%
Over $21,300, but not over $21,800  45%
Over $21,800, but not over $22,300  40%
Over $22,300, but not over $25,000  35%
Over $25,000, but not over $25,500  30%
Over $25,500, but not over $26,000  25%
Over $26,000, but not over $26,500  20%
Over $26,500, but not over $31,300  15%
Over $31,300, but not over $31,800  14%
Over $31,800, but not over $32,300  13%
Over $32,300, but not over $32,800  12%
Over $32,800, but not over $33,300  11%
Over $33,300, but not over $60,000  10%
Over $60,000, but not over $60,500  9%
Over $60,500, but not over $61,000  8%
Over $61,000, but not over $61,500  7%
Over $61,500, but not over $62,000  6%
Over $62,000, but not over $62,500  5%
Over $62,500, but not over $63,000  4%
Over $63,000, but not over $63,500  3%
Over $63,500, but not over $64,000  2%
Over $64,000, but not over $64,500  1%
Over $64,500                        0%

MARRIED FILING SEPARATELY
Adjusted Gross Income               Amount of Credit
Over $12,000, but not over $15,000  75%
Over $15,800, but not over $15,500  70%
Over $15,500, but not over $16,000  65%
Over $16,000, but not over $16,500  60%
Over $16,500, but not over $17,000  55% 
Over $17,000, but not over $17,500  50%
Over $17,500, but not over $18,000  45%
Over $18,000, but not over $18,500  40%
Over $18,500, but not over $20,000  35%
Over $20,000, but not over $20,500  30%
Over $20,500, but not over $21,000  25%
Over $21,000, but not over $21,500  20%
Over $21,500, but not over $25,000  15%
Over $25,000, but not over $25,500  14%
Over $25,500, but not over $26,000  13%
Over $26,000, but not over $26,500  12%
Over $26,500, but not over $27,000  11%
Over $27,000, but not over $48,000  10%
Over $48,000, but not over $48,500  9%
Over $48,500, but not over $49,000  8%
Over $49,000, but not over $49,500  7%
Over $49,500, but not over $50,000  6%
Over $50,000, but not over $50,500  5%
Over $50,500, but not over $51,000  4%
Over $51,000, but not over $51,500  3%
Over $51,500, but not over $52,000  2%
Over $52,000, but not over $52,500  1%
Over $52,500                        0%

HEAD OF HOUSEHOLD
Adjusted Gross Income               Amount of Credit
Over $19,000, but not over $24,000  75%
Over $24,000, but not over $24,500  70%
Over $24,500, but not over $25,000  65%
Over $25,000, but not over $25,500  60%
Over $25,500, but not over $26,000  55% 
Over $26,000, but not over $26,500  50%
Over $26,500, but not over $27,000  45%
Over $27,000, but not over $27,500  40%
Over $27,500, but not over $34,000  35%
Over $34,000, but not over $34,500  30%
Over $34,500, but not over $35,000  25%
Over $35,000, but not over $35,500  20%
Over $35,500, but not over $44,000  15%
Over $44,000, but not over $44,500  14%
Over $44,500, but not over $45,000  13%
Over $45,000, but not over $45,500  12%
Over $45,500, but not over $46,000  11%
Over $46,000, but not over $74,000  10%
Over $74,000, but not over $74,500  9%
Over $74,500, but not over $75,000  8%
Over $75,000, but not over $75,500  7%
Over $75,500, but not over $76,000  6%
Over $76,000, but not over $76,500  5%
Over $76,500, but not over $77,000  4%
Over $77,000, but not over $77,500  3%
Over $78,500, but not over $78,000  2%
Over $78,000, but not over $78,500  1%
Over $78,500                        0%

MARRIED FILING JOINTLY
Adjusted Gross Income                 Amount of Credit
Over $24,000, but not over $30,000    75%
Over $30,000, but not over $30,500    70%
Over $30,500, but not over $31,000    65%
Over $31,000, but not over $31,500    60%
Over $31,500, but not over $32,000    55% 
Over $32,000, but not over $32,500    50%
Over $32,500, but not over $33,000    45%
Over $33,000, but not over $33,500    40%
Over $33,500, but not over $40,000    35%
Over $40,000, but not over $40,500    30%
Over $40,500, but not over $41,000    25%
Over $41,000, but not over $41,500    20%
Over $41,500, but not over $50,000    15%
Over $50,000, but not over $50,500    14%
Over $50,500, but not over $51,000    13%
Over $51,000, but not over $51,500    12%
Over $51,500, but not over $52,000    11%
Over $52,000, but not over $96,000    10%
Over $96,000, but not over $96,500    9%
Over $96,500, but not over $97,000    8%
Over $97,000, but not over $97,500    7%
Over $97,500, but not over $98,000    6%
Over $98,000, but not over $98,500    5%
Over $98,500, but not over $99,000    4%
Over $99,000, but not over $99,500    3%
Over $99,500, but not over $100,000   2%
Over $100,000, but not over $100,500  1%
Over $100,500                         0%

CONNECTICUT CAPITAL GAINS TAXES
https://portal.ct.gov/DRS/Publications/TSSNs/TSSN-29#:~:text=An%20individual's%20net%20capital%20gains,portion%20of%20Social%20Security%20benefits.
Net capital gains are taxed at a rate of 7%

Dividends and interest income are treated as ordinary income
'''
class Connecticut:
    import math
    taxes = capitalGains * .07
    if stateDeductions == 0:
        exemptions = {'Married Filing Jointly': 24000, 'Single': 15000, 'Head of Household': 19000, 'Married Filing Separately': 12000}
        # No state deductions in this case
        if agi > 3 * exemptions[maritalStatus] - 1000:
            pass
        # Full exemption applies
        elif agi < exemptions[maritalStatus] * 2:
            stateDeductions = exemptions[maritalStatus]
        # Phaseout applies
        else:
            stateDeductions = exemptions[maritalStatus] - math.ceil((agi - 2 * exemptions[maritalStatus]) / 1000) * 1000
            
    if maritalStatus == 'Married':
        if agi > 1000000:
            stateBracket = .0699
            margin = agi - 1000000
            taxes = 63100 + margin * stateBracket
        elif agi > 500000:
            stateBracket = .069
            margin = agi - 500000
            taxes = 28600 + margin * stateBracket
        elif agi > 400000:
            stateBracket = .065
            margin = agi - 400000
            taxes = 22100 + margin * stateBracket
        elif agi > 200000:
            stateBracket = .06
            margin = agi - 200000
            taxes = 10100 + margin * stateBracket
        elif agi > 100000:
            stateBracket = .055
            margin = agi - 100000
            taxes = 4600 + margin * stateBracket
        elif agi > 20000:
            stateBracket = .05
            margin = agi - 20000
            taxes = 600 + margin * stateBracket
        else:
            stateBracket = .03
            taxes = agi * stateBracket
    else:
        if agi > 500000:
            stateBracket = .0699
            margin = agi - 500000
            taxes = 31550 + margin * stateBracket
        elif agi > 250000:
            stateBracket = .069
            margin = agi - 250000
            taxes = 14300 + margin * stateBracket
        elif agi > 200000:
            stateBracket = .065
            margin = agi - 200000
            taxes = 11050 + margin * stateBracket
        elif agi > 100000:
            stateBracket = .06
            margin = agi - 100000
            taxes = 5050 + margin * stateBracket
        elif agi > 50000:
            stateBracket = .055
            margin = agi - 50000
            taxes = 2300 + margin * stateBracket
        elif agi > 10000:
            stateBracket = .05
            margin = agi - 10000
            taxes = 300 + margin * stateBracket
        else:
            stateBracket = .03
            taxes = agi * stateBracket
    
    # 3% Phase-Out Add-Back:
    threhsolds = {'Married Filing Jointly': [100500, 145500],
                  'Head of Household': [78500, 114500],
                  'Single': [56500, 101500],
                  'Married Filing Separately': [50250, 72750]}
    
    if agi < threhsolds[maritalStatus][0]:
        pass
    
    else:
        differences = {'Married Filing Jointly': 5000,
                    'Head of Household': 4000,
                    'Single': 2500,
                    'Married Filing Separately': 2500}
        
        factors = {'Married Filing Jointly': 40,
                    'Head of Household': 32,
                    'Single': 20,
                    'Married Filing Separately': 20}
        
        if agi < threhsolds[maritalStatus][1]:
            taxes += math.ceil((agi - threhsolds[maritalStatus][0]) / differences[maritalStatus]) * factors[maritalStatus]
        
        # Maximum in this case, 10 times the factor
        else:
            taxes += 10 * factors[maritalStatus]
    
    if eic:
        credits = [1,.75,.70,.65,.60,.55,.50,.45,.40,.35,.30,.25,.20,.15,.14,.13,.12,.11,.10,.09,.08,.07,.06,.05,.04,.03,.02,.01]
        threhsolds = {'Married Filing Jointly': [24000,30000,30500,31000,31500,32000,32500,33000,33500,40000,40500,41000,41500,50000,50500,51000,51500,52000,96000,96500,97000,97500,98000,98500,99000,99500,100000,100500],
                      'Head of Household': [19000,24000,24500,25000,25500,26000,26500,27000,27500,34000,34500,35000,35500,44000,44500,45000,45500,46000,74000,74500,75000,75500,76000,76500,77000,77500,78000,78500],
                      'Single': [15000,18800,19300,19800,20300,20800,21300,21800,22300,25000,25500,26000,26500,31300,31800,32300,32800,33300,60000,60500,61000,61500,62000,62500,63000,63500,64000,64500],
                      'Married Filing Seperately': [12000,15800,15500,16000,16500,17000,17500,18000,18500,20000,20500,21000,21500,25000,25500,26000,26500,27000,48000,48500,49000,49500,50000,50500,51000,51500,52000,52500]}
        for i in range(len(threhsolds[maritalStatus])):
            if agi < threhsolds[maritalStatus][i]:
                taxes -= eic * credits[i]
                break

    # For Tax Recaputre, Married Filing Separately is treated as Single
    if maritalStatus == 'Married Filing Separately':
        maritalStatus = 'Single'
    
    # Tax Recapture:
    threhsolds = {'Married Filing Jointly': [400000, 690000, 1000000, 1080000],
                  'Head of Household': [320000, 552000, 800000, 864000],
                  'Single': [200000, 345000, 490000, 540000]}

    # No Tax Recapture
    if agi < threhsolds[maritalStatus][0]:
        pass
    
    # Maximum Tax Recapture
    elif agi > threhsolds[maritalStatus][3]:
        maxAmounts = {'Married Filing Jointly': 6300,
                      'Head of Household': 4920,
                      'Single': 3150}
        
        taxes += maxAmounts[maritalStatus]
    # Phase-Out Applies
    else:
        differences = {'Married Filing Jointly': 10000,
                       'Head of Household': 8000,
                       'Single': 5000}
        
        # Initial Phase-Out
        if agi < threhsolds[maritalStatus][1]:
            factors = {'Married Filing Jointly': 180,
                       'Head of Household': 140,
                       'Single': 90}
            taxes += math.ceil((agi - threhsolds[maritalStatus][0]) / differences[maritalStatus]) * factors[maritalStatus][0]
        
        elif agi < threhsolds[maritalStatus][3]:
            newTax = {'Married Filing Jointly': 5500,
                       'Head of Household': 4200,
                       'Single': 2700}
            # Second Phase-Out
            taxes += newTax[maritalStatus]

            # Third Phase-Out
            if agi > threhsolds[maritalStatus][2]:
                factors = {'Married Filing Jointly': 100,
                        'Head of Household': 80,
                        'Single': 50}
                taxes += math.ceil((agi - threhsolds[maritalStatus][2]) / differences[maritalStatus]) * factors[maritalStatus][0]
    