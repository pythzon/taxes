'''
WISCONSIN INCOME TAXES (2023)
https://www.revenue.wi.gov/TaxForms2023/2023-Form1-ES-Inst.pdf

For single, head of household, estates, and trusts with taxable income:
over	    but not over	2022 tax is 	    of the amount over
$0	        $13,810	        3.54%	            $0
$13,810     $27,630	        $451.70 + 4.65%	    $13,810
$27,630	    $304,170	    $1,045.04 + 5.3%	$27,630
$304,170                  	$14,582.83 + 7.65%	$304,170

For married taxpayers filing a joint return with taxable income:
over	    but not over	2022 tax is	        of the amount over
$0	        $18,420         3.54%	            $0
$18,420     $36,840         $602.15 + 4.65%	    $18,420
$36,840     $405,550        $1,393.58 + 5.3%	$36,840
$405,550                    $19,443.79 + 7.65%	$405,550

For married taxpayers filing separate returns with taxable income:
over	    but not over	2022 tax is	        of the amount over
$0	        $9,210          3.54%	            $0      
$9,210      $18,420         $301.25 + 4.65% 	$9,210
$18,420     $187,300	    $696.50 + 5.3%	    $18,420
$202,780                    $9,721.87 + 7.65%	$202,780

WISCONSIN DEDUCTIONS
STANDARD DEDUCTION (2023)
Single
over        but not over    deduction
$0          $18,399 	    $12,760
$18,399     $124,733 	    $12,760 - 12% of the amount over $18,400
$124,733                    $0

Head of Household
over        but not over    deduction
$0          $18,399 	    $16,840
$18,399     $53,778 	    $16,840 - 22.515% of the amount over $18,400
$53,778     $124,733 	    $12,760 - 12% of the amount over $18,400
$124,733                    $0

Married Filing Jointly
over        but not over    deduction
$0          $26,549 	    $23,620
$26,549     $124,733 	    $23,620 - 19.778% of the amount over $26,550
$145,976                    $0

Married Filing Separately
over        but not over    deduction
$0          $12,599 	    $11,220
$12,599     $69,330 	    $11,220 - 19.778% of the amount over $12,600
$69,330                     $0

EXEMPTIONS (2023)
$700 for yourself, $700 for your spouse if filing a joint return, and $700 for each dependent.
Add $250 to the total if you are 65 years of age or over and, if filing a joint return, add
$250 if your spouse is 65 years of age or over. Exemptions must also be prorated using the
same ratio as standard deductions.

RECIRPOCAL AGREEMENTS
https://www.revenue.wi.gov/Pages/FAQS/pcs-work.aspx
Illinois, Indiana, Kentucky, and Michigan

WISCNSIN CAPITAL GAINS TAXES 
https://www.revenue.wi.gov/DOR%20Publications/pb103.pdf               
30% of long term gains are deducted, but all gains are treated as ordinary income (P. 4)
'''

class Wisconsin:
    agi += shortCapitalGains + (longCapitalGains * .7)
    if resState in ['Illinois', 'Indiana', 'Kentucky', 'Michigan']:
            workState = resState

    taxes = -stateCredits
    
    if maritalStatus == 'Married':
        if stateDeductions == 0:
            exemptions = 1400 + (dependents * 700)
            deductions = 23620
            if agi > 145976:
                stateDeductions = 0
            elif agi > 26549:
                stateDeductions = deduction - (agi - 26549) * .19778
            else:
                stateDeductions = deduction
            # Calculates prorated exemptions
            stateDeductions += (stateDeductions / deduction) * exemptions

        agi -= stateDeductions
        if agi > 405550:
            stateBracket = .0765
            margin = agi - 405550
            taxes = 19443.79 + margin * stateBracket
        elif agi > 36840:
            stateBracket = .053
            margin = agi - 36840
            taxes = 1393.58 + margin * stateBracket
        elif agi > 18420:
            stateBracket = .0465
            margin = agi - 18420
            taxes = 602.15 + margin * stateBracket
        else:
            stateBracket = .0354
            taxes = agi * stateBracket

    if maritalStatus == 'Married Filing Separately':
        if stateDeductions == 0:
            exemptions = 1400 + (dependents * 700)
            deduction = 11220
            if agi > 69330:
                stateDeductions = 0
            elif agi > 12599:
                stateDeductions = deduction - (agi - 12599) * .19778
            else:
                stateDeductions = deduction
            stateDeductions += (stateDeductions / deduction) * exemptions
        agi -= stateDeductions
        if agi > 202780:
            stateBracket = .0765
            margin = agi - 202780
            taxes = 9721.87 + margin * stateBracket
        elif agi > 18420:
            stateBracket = .053
            margin = agi - 18420
            taxes = 696.5 + margin * stateBracket
        elif agi > 9210:
            stateBracket = .0465
            margin = agi - 9210
            taxes = 301.25 + margin * stateBracket
        else:
            stateBracket = .0354
            taxes = agi * stateBracket

    else: # Single and Head of Household
        if stateDeductions == 0:
            exemptions = 700 + (dependents * 700)
            if maritalStatus == 'Single':
                deduction = 12760
                if agi > 124733:
                    stateDeductions = 0
                elif agi > 18399:
                    stateDeductions = deduction - (agi - 18399) * .12
                else:
                    stateDeductions = deduction  
            # Head of Household
            else:
                deduction = 16840
                if agi > 124733:
                    stateDeductions = 0
                elif agi > 53778:
                    stateDeductions = deduction - (agi - 53778) * .22515
                elif agi > 18399:
                    stateDeductions = deduction - (agi - 18399) * .12
                else:
                    stateDeductions = deduction  
            stateDeductions = (stateDeductions / deduction) * exemptions
        agi -= stateDeductions

        if agi > 304170:
            stateBracket = .0765
            margin = agi - 304170
            taxes = 14582.83 + margin * stateBracket
        elif agi > 27630:
            stateBracket = .053
            margin = agi - 27630
            taxes = 1045.04 + margin * stateBracket
        elif agi > 13810:
            stateBracket = .0465
            margin = agi - 13810
            taxes = 451.7 + margin * stateBracket
        else:
            stateBracket = .0354
            taxes = agi * stateBracket
        