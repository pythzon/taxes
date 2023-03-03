# These states do not impose income taxes: Alaska, Florida, Nevada, South Dakota, Tennessee, Texas, Washington, and Wyoming

def statetaxes(state, county, agi, maritalStatus, federalTaxes, stateDeductions, stateCredits, dependents, payPeriod=24):
    taxes = 0
    stateBracket = 0
    localBracket = 0
    margin = 999999
    # Alabama allows for federal deductions from state income tax !capital gains treated as income
    '''
    STATE INCOME TAXES
    https://www.revenue.alabama.gov/faqs/what-is-alabamas-individual-income-tax-rate/
    
    For single persons, heads of families, and married persons filing separate returns:
    2% First $500 of taxable income
    4% Next $2,500 of taxable income
    5% All taxable income over $3,000

    For married persons filing a joint return:
    2% First $1,000 of taxable income
    4% Next $5,000 of taxable income
    5% All taxable income over $6,000

    STATE DEDUCTIONS?
    https://www.revenue.alabama.gov/wp-content/uploads/2022/06/21f40abk.pdf

    '''
    if state == 'Alabama':
        # Alabama allows you to deduct without itemizing your federal income taxes
        agi -= federalTaxes
        if maritalStatus == 'Married':
            # Use standard deduction in this case
            if stateDeductions == 0:
                if agi < 20000:
                    stateDeductions = 10500 + dependents * 1000
                elif agi < 23000:
                    stateDeductions = 10500 + dependents * 500
                elif agi < 33000:
                    stateDeductions = 10500 - (33000 - agi) * .35 + dependents * 500
                elif agi < 100000:
                    stateDeductions = 7000 + dependents * 500
                else:
                    stateDeductions = 7000 + dependents * 300
            # Add standard deduction
            agi -= stateDeductions
            if agi > 6000:
                stateBracket = .05
                margin = agi - 6000
                taxes = 220 + margin * stateBracket
            elif agi > 1000:
                stateBracket = .04
                margin = agi - 1000
                taxes = 20 + margin * stateBracket
            else:
                stateBracket = 0.02
                taxes = agi * stateBracket
        # Condition for unmarried filers
        else:
            # Use standard deduction in this case
            if stateDeductions == 0:
                if agi < 20000:
                    stateDeductions = 4000 + dependents * 1000
                elif agi < 23000:
                    stateDeductions = 4000 + dependents * 500
                elif agi < 33000:
                    stateDeductions = 3500 - (33000 - agi) * .05 + dependents * 500
                elif agi < 100000:
                    stateDeductions = 3500 + dependents * 500
                else:
                    stateDeductions = 3500 + dependents * 300
            # !Add personal exemption
            agi -= stateDeductions
            if agi > 3000:
                stateBracket = .05
                margin = agi - 3000
                taxes = 110 + margin * stateBracket
            elif agi > 500:
                stateBracket = .04
                margin = agi - 500
                taxes = 10 + margin * stateBracket
            else:
                stateBracket = 0.02
                taxes = agi * stateBracket
        if county == 'Bessemer':
            localBracket = .01
        elif county == 'Birmingham':
            localBracket = .01
        elif county == 'Gadsden':
            localBracket = .02
        elif county == 'Macon County':
            localBracket = .01
        else:
            return taxes, stateBracket, margin
        taxes += localBracket * agi
    
    '''
    STATE INCOME TAXES
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

    DEDUCTIONS
    https://azdor.gov/forms/individual/form-140-resident-personal-income-tax-form-calculating


    '''
    # $100 dependent credit
    elif state == "Arizona":
        # Arizona only lets you claim 1 dependent
        if dependents:
            taxes = -100
        if maritalStatus == 'Married':
            # Use standard deduction in this case same as federal
            if stateDeductions == 0:
                stateDeductions = 25100
            agi -= stateDeductions
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
        # Condition for unmarried filers
        else:
            # Use standard deduction in this case same as federal
            if stateDeductions == 0:
                stateDeductions = 12550
            agi -= stateDeductions
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
    '''
    STATE INCOME TAXES
    https://www.arkansasedc.com/why-arkansas/business-climate/tax-structure/personal-income-tax

    PERSONAL INCOME TAX RATES FOR TAX YEAR BEGINNING JANUARY 1, 2022
    Income Tax Rate for Individuals with Net Income of Less Than or Equal to $84,500	 
    $0      - $4,999	0.0%
    $5,000  - $9,999	2.0%
    $10,000 - $14,299	3.0%
    $14,300 - $23,599	3.4%
    $23,600 - $84,500	4.9%

    Income Tax Rate for Individuals with a Net Income Greater Than $84,500	 
    $0      - $4,300	    2.0%
    $4,301  - $8,500	    4.0%
    $8,501+
    '''
    elif state == 'Arkansas':
        if stateDeductions == 0:
            if maritalStatus == 'Married':
                # $58 credit for married couples
                taxes = -58
                stateDeductions = 4400
            else:
                # $29 credit for individuals
                taxes = -58
                stateDeductions = 2200
            # $29 credit per dependent
            taxes -= 29 * dependents
        agi -= stateDeductions
        # Same tax state brackets regardless of marital status
        if agi > 84500:
            stateBracket = .049
            # TODO verify edge case
            margin = agi - 84500
            # $254 = $4,300 * 2% + $4,200 * 4%
            taxes += 254 + (agi - 8500) * stateBracket
        elif agi > 23600:
            stateBracket = .049
            margin = agi - 23600
            taxes += 545.2 + margin * stateBracket
        elif agi > 14300:
            stateBracket = .034
            margin = agi - 14300
            taxes += 229 + margin * stateBracket
        elif agi > 10000:
            stateBracket = .03
            margin = agi - 10000
            taxes += 100 + margin * stateBracket
        elif agi > 5000:
            stateBracket = .02
            taxes += (agi - 5000) * stateBracket
        else:
            stateBracket = 0

    '''
    STATE INCOME TAXES
    https://www.ftb.ca.gov/forms/2022/2022-540-tax-rate-schedules.pdf

    SINGLE OR MARRIED FILING SEPARATELY
    Taxable Income
    Is over      But not over     Taxes                Of the amount over
    $0           $10,099          1.00%                $0
    $10,099      $23,942          $100.99    + 2.0%    $10,099
    $23,942      $37,788          $377.85    + 4.0%    $23,942
    $37,788      $52,455          $931.69    + 6.0%    $37,788
    $52,455      $66,295          $1,811.71  + 8.0%    $52,455
    $66,295      $338,639         $2,918.91  + 9.3%    $66,295
    $338,639     $406,364         $28,246.9  + 10.3%   $338,639
    $406,364     $677,275         $35,222.58 + 11.3%   $406,364
    $677,275                      $65,835.52 + 12.3%   $677,275
                                                                       
    MARRIED FILING JOINTLY OR QUALIFYING SURVIVING SPOUSE                                                                                                                                      
    Taxable Income
    Is over      But not over     Taxes                 Of the amount over
    $0           $20,198          1.00%                 $0
    $20,198      $47,884          $201.98     + 2.0%    $20,198
    $47,884      $75,576          $755.7      + 4.0%    $47,884
    $75,576      $104,910         $1,863.38   + 6.0%    $75,576
    $104,910     $132,590         $3,623.42   + 8.0%    $104,910
    $132,590     $677,278         $5,837.82   + 9.3%    $132,590
    $677,278     $812,728         $56,493.8   + 10.3%   $677,278 
    $812,728     $1,354,550       $35,222.58  + 11.3%   $812,728
    $1,354,550                    $131,671.04 + 12.3%   $1,354,550     
                                                                       
    HEAD OF HOUSEHOLD
    Taxable Income
    Is over      But not over     Taxes                Of the amount over
    $0           $20,212          1.00%                $0
    $20,212      $47,887          $202.12    + 2.0%    $20,212
    $47,887      $61,730          $755.62    + 4.0%    $47,887
    $61,730      $76,397          $1,309.34  + 6.0%    $61,730
    $76,397      $90,240          $2,189.36  + 8.0%    $76,397
    $90,240      $460,547         $3,296.8   + 9.3%    $90,240
    $460,547     $552,658         $37,735.35 + 10.3%   $460,547
    $552,658     $921,095         $47,222.78 + 11.3%   $552,658
    $921,095                      $88,856.16 + 12.3%   $677,275                                                                

    DEDUCTIONS
    https://www.ftb.ca.gov/file/personal/deductions/index.html

    SINGLE OR MARRIED FILING SEPARATELY:
    $5,202
    
    MARRIED FILING JOINTLY, HEAD OF HOUSEHOLD, OR QUALIFYING SURVIVING SPOUSE:
    $10,404
    '''
    elif state == 'California':
        # $383 credit per dependent?
        if maritalStatus == 'Single':
            if stateDeductions == 0:
                stateDeductions = 5202
                # taxes = -(248 + (dependents * 383))
            agi -= stateDeductions
            if agi > 667275:
                stateBracket = .123
                margin = agi - 667275
                taxes += 65835.52 + margin * stateBracket
            elif agi > 406364:
                stateBracket = .113
                margin = agi - 406364
                taxes += 35222.58 + margin * stateBracket
            elif agi > 338639:
                stateBracket = .103
                margin = agi - 338639
                taxes += 28246.9 + margin * stateBracket
            elif agi > 66295:
                stateBracket = .093
                margin = agi - 66295
                taxes += 2918.91 + margin * stateBracket
            elif agi > 52455:
                stateBracket = .08
                margin = agi - 52455
                taxes += 1811.71 + margin * stateBracket
            elif agi > 37788:
                stateBracket = .06
                margin = agi - 37788
                taxes += 931.69 + margin * stateBracket
            elif agi > 23942:
                stateBracket = .04
                margin = agi - 23942
                taxes += 377.85 + margin * stateBracket
            elif agi > 10099:
                stateBracket = .02
                margin = agi - 10099
                taxes += 100.99 + margin * stateBracket
            else:
                stateBracket = .01
                taxes += agi * stateBracket
        else:
            if stateDeductions == 0:
                # taxes = -(124 + (dependents * 383))
                stateDeductions = 10404
                 agi -= stateDeductions
            if maritalStatus == 'Married Filing Jointly':
                if agi > 1354550:
                    stateBracket = .123
                    margin = agi - 1354550
                    taxes += 131671.04 + margin * stateBracket
                elif agi > 812728:
                    stateBracket = .113
                    margin = agi - 812728
                    taxes += 47333.78 + margin * stateBracket
                elif agi > 677278:
                    stateBracket = .103
                    margin = agi - 677278
                    taxes += 56493.38 + margin * stateBracket
                elif agi > 132590:
                    stateBracket = .093
                    margin = agi - 132590
                    taxes += 5837.82 + margin * stateBracket
                elif agi > 104910:
                    stateBracket = .08
                    margin = agi - 104910
                    taxes += 3623.42 + margin * stateBracket
                elif agi > 75576:
                    stateBracket = .06
                    margin = agi - 75576
                    taxes += 1863.38 + margin * stateBracket
                elif agi > 47884:
                    stateBracket = .04
                    margin = agi - 47884
                    taxes += 755.7 + margin * stateBracket
                elif agi > 20198:
                    stateBracket = .02
                    margin = agi - 20198
                    taxes += 201.98 + margin * stateBracket
                else:
                    stateBracket = .01
                    taxes += agi * stateBracket
            elif maritalStatus == 'Head of Household':
                if agi > 667275:
                    stateBracket = .123
                    margin = agi - 667275
                    taxes += 88856.16 + margin * stateBracket
                elif agi > 552658:
                    stateBracket = .113
                    margin = agi - 552658
                    taxes += 47222.78 + margin * stateBracket
                elif agi > 460547:
                    stateBracket = .103
                    margin = agi - 460547
                    taxes += 37735.35 + margin * stateBracket
                elif agi > 90240:
                    stateBracket = .093
                    margin = agi - 90240
                    taxes += 3296.8 + margin * stateBracket
                elif agi > 76397:
                    stateBracket = .08
                    margin = agi - 76397
                    taxes += 1811.71 + margin * stateBracket
                elif agi > 61730:
                    stateBracket = .06
                    margin = agi - 61730
                    taxes += 1309.34 + margin * stateBracket
                elif agi > 47887:
                    stateBracket = .04
                    margin = agi - 47887
                    taxes += 755.62 + margin * stateBracket
                elif agi > 20212:
                    stateBracket = .02
                    margin = agi - 20212
                    taxes += 202.12 + margin * stateBracket
                else:
                    stateBracket = .01
                    taxes += agi * stateBracket
            else:
                raise Exception('Marital Status not recognized')  
    '''
    STATE INCOME TAX
    https://leg.colorado.gov/agencies/legislative-council-staff/individual-income-tax%C2%A0
    
    4.55%

    LOCAL INCOME TAXES
    https://www.auroragov.org/business_services/taxes/occupational_privilege_tax
    Aurora
    $2 per month

    https://www.denvergov.org/Government/Agencies-Departments-Offices/Agencies-Departments-Offices-Directory/Department-of-Finance/Our-Divisions/Treasury/Business-Tax-Information#:~:text=Occupational%20privilege%20tax,-%28show%20below%29&text=Each%20taxable%20employee%20is%20liable,month%20for%20each%20taxable%20employee.
    Denver
    $5.75 per month

    https://www.glendale.co.us/355/Occupational-Privilege-Tax
    Glendale
    $5 per month    

    https://www.greenwoodvillage.com/1220/Occupational-Privilege-Tax-OPT
    Greenwood Village
    $2 per month
    
    https://ci.sheridan.co.us/288/Occupational-Privilege-Tax
    Sheridan 
    $3 per month
    '''
    elif state == 'Colorado':
        # if stateDeductions == 0:
        #     if maritalStatus == 'Married':
        #         stateDeductions = 25100
        #     else:
        #         stateDeductions = 12550
        # agi -= stateDeductions
        stateBracket = .0455
        taxes = agi * stateBracket
        if county == 'Aurora':
            taxes += 24
        elif county == 'Denver':
            taxes += 69
        elif county == 'Glendale':
            taxes += 60
        elif county == 'Greenwood Village':
            taxes += 24
        elif county == 'Sheridan':
            taxes += 36
    
    '''
    STATE INCOME TAX
    https://www.cga.ct.gov/2022/rpt/pdf/2022-R-0108.pdf

    Connecticut Taxable Income
    Tax Rate    Single and Married Filing Separately   Heads of Household        Married Filing Jointly
    3%          $0 to $10,000                          $0 to $16,000             $0 to 20,000 
    5%          $10,001 to $50,000                     $16,001 to $80,000        $20,001 to $100,000
    5.5%        $50,001 to $100,000                    $80,001 to $160,000       $100,001 to $200,000
    6%          $100,001 to $200,000                   $160,001 to $320,000      $200,001 to $400,000
    6.5%        $200,001 to $250,000                   $320,001 to $400,000      $400,001 to $500,000
    6.9%        $250,001 to $500,000                   $400,001 to $800,000      $500,01 to $1,000,000
    6.99%       > $500,000                             > $800,000                > $1,000,000
    
    TODO EVIL ATTACHMENT (TAX RECAPTURE, 3% PHASE-OUT ADD-BACK)
    https://portal.ct.gov/-/media/DRS/Forms/2021/Income/CT-1040-TCS_1221.pdf


    PERSONAL TAX CREDITS
    https://www.cga.ct.gov/current/pub/chap_229.htm#sec_12-703

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

    '''
    # !Several weird rules
    elif state == 'Conecticut':
        if maritalStatus == 'Married':
            if stateDeductions == 0:
                stateDeductions = 15000
            agi -= stateDeductions
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
            if stateDeductions == 0:
                stateDeductions = 24000
            agi -= stateDeductions
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

    ''' 
    DELAWARE STATE INCOME TAXES
    https://revenue.delaware.gov/software-developer/tax-rate-changes/

    Taxable income range	        Base	    Rate
    At least	But less than
    $0	        $2,000	            $0	        0%
    $2,000	    $5,000	            $0	        2.2%
    $5,000	    $10,000	            $66	        3.9%
    $10,000	    $20,000	            $261	    4.8%
    $20,000	    $25,000	            $741	    5.2%
    $25,000	    $60,000	            $1,001	    5.55%
    $60,000		                    $2943.50	6.6%

    CREDITS AND DEDUCTIONS
    https://revenuefiles.delaware.gov/2022/PIT-RES_TY22_2022-01_PaperInteractive.pdf
    
    LINE 19 - STANDARD DEDUCTION 
    MARRIED - 6500
    OTHERWISE - 3250

    LINE 26A. - PERSONAL CREDITS?
    NUMBER OF EXEMPTIONS * $110

    LINE 30
    CHILD TAX CARE CREDIT - 50% OF FEDERAL CREDIT

    LOCAL INCOME TAXES
    https://www.newcastlede.gov/DocumentCenter/View/20147/City-of-Wilmington-Wage-Tax-Information-PDF
    WILMINGTON 1.25% GROSS WAGES
    '''
    # !Tax on lump sum tax credit or deduction?
    elif state == 'Delaware':
        # $110 dependent tax credit
        if stateDeductions == 0:
            if maritalStatus == 'Married':
                    taxes = -(220 + (dependents * 110))
                    stateDeductions = 6500
            else:
                if stateDeductions == 0:
                    taxes = -(110 + (dependents * 110))
                    stateDeductions = 3250
        agi -= stateDeductions
        if agi > 60000:
            stateBracket = .066
            margin = agi - 60000
            taxes = 2943.50 + margin * stateBracket
        elif agi > 25000:
            stateBracket = .0555
            margin = agi - 25000
            taxes = 1001 + margin * stateBracket
        elif agi > 20000:
            stateBracket = .052
            margin = agi - 20000
            taxes = 741 + margin * stateBracket
        elif agi > 10000:
            stateBracket = .048
            margin = agi - 10000
            taxes = 261 + margin * stateBracket
        elif agi > 5000:
            stateBracket = .039
            margin = agi - 5000
            taxes = 66 + margin * stateBracket
        elif agi > 2000:
            stateBracket = .022
            margin = agi - 2000
            taxes = margin * stateBracket
        if county == 'Wilmington':
            # TODO GROSS WAGES, NOT AGI
            taxes += .0125 * agi

    '''
    STATE INCOME TAXES
    https://dor.georgia.gov/tax-tables-georgia-tax-rate-schedule
    
    Single
    If Georgia Taxable Income Is
    Over        But not over    Amount of Tax Is
    $0          $750            1% of taxable income
    $750        $2,250          $8.00 Plus 2% of the amount over $750
    $2,250      $3,750          $38.00 Plus 3% of the amount over $2,250
    $3,750      $5,250          $83.00 Plus 4% of the amount over $3,750
    $5,250      $7,000          $143.00 Plus 5% of the amount over $5,250
    $7,000                      $230.00 Plus 5.75% of the amount over $7,000

    Married Filing Joint or Head of Household
    If Georgia Taxable Income Is
    Over        But not over    Amount of Tax Is
    $0          $1,000          1% of taxable income
    $1,000      $3,000          $10.00 Plus 2% of the amount over $1,000
    $3,000      $5,000          $50.00 Plus 3% of the amount over $3,000
    $5,000      $7,000          $110.00 Plus 4% of the amount over $5,000
    $7,000      $10,000         $190.00 Plus 5% of the amount over $7,000
    $10,000                     $340.00 Plus 5.75% of the amount over $10,000
    
    Married Filing Separate
    If Georgia Taxable Income Is
    Over        But not over    Amount of Tax Is
    $0          $500            1% of taxable income
    $500        $1,500          $5.00 Plus 2% of the amount over $500
    $1,500      $2,500          $25.00 Plus 3% of the amount over $1,500
    $2,500      $3,500          $55.00 Plus 4% of the amount over $2,500
    $3,500      $5,000          $95.00 Plus 5% of the amount over $3,500
    $5,000                      $170.00 Plus 5.75% of the amount over $5,000


    DEPENDENTS
    https://apps.dor.ga.gov/FillableForms/PDFViewer/Index?form=2022GA500
    $3,000 for each dependent
    '''
    elif state == "Georgia":
        if maritalStatus == 'Married':
            if stateDeductions == 0:
                stateDeductions = 13400 + 3000 * dependents
            agi -= stateDeductions
            if agi > 10000:
                stateBracket = .055
                margin = agi - 10000
                taxes = 340 + margin * stateBracket
            elif agi > 7000:
                stateBracket = .05
                margin = agi - 7000
                taxes = 190 + margin * stateBracket
            elif agi > 5000:
                stateBracket = .04
                margin = agi - 5000
                taxes = 110 + margin * stateBracket
            elif agi > 3000:
                stateBracket = .03
                margin = agi - 3000
                taxes = 50 + margin * stateBracket
            elif agi > 1000:
                stateBracket = .02
                margin = agi - 1000
                taxes = 10 + margin * stateBracket
            else:
                stateBracket = .01
                taxes = agi * stateBracket
        else:
            if stateDeductions == 0:
                stateDeductions = 7300 + 3000 * dependents
            agi -= stateDeductions
            if agi > 7000:
                stateBracket = .055
                margin = agi - 7000
                taxes = 230 + margin * stateBracket
            elif agi > 5250:
                stateBracket = .05
                margin = agi - 5250
                taxes = 142.5 + margin * stateBracket
            elif agi > 3750:
                stateBracket = .04
                margin = agi - 3750
                taxes = 82.5 + margin * stateBracket
            elif agi > 2250:
                stateBracket = .03
                margin = agi - 2250
                taxes = 37.5 + margin * stateBracket
            elif agi > 750:
                stateBracket = .02
                margin = agi - 750
                taxes = 7.5 + margin * stateBracket
            else:
                stateBracket = .01
                taxes = agi * stateBracket
    '''
    STATE INCOME TAXES
    https://tax.hawaii.gov/forms/d_18table-on/
    https://files.hawaii.gov/tax/forms/2018/18table-on.pdf (P. 14)

    SINGLE TAXPAYERS AND MARRIED FILING SEPARATE RETURNS
    If taxable income is:                   Your tax is:
    Not over $2,400                         1.40% of taxable income
    Over $2,400 but not over $4,800         $34 plus 3.20% over $2,400
    Over $4,800 but not over $9,600         $110 plus 5.50% over $4,800
    Over $9,600 but not over $14,400        $374 plus 6.40% over $9,600
    Over $14,400 but not over $19,200       $682 plus 6.80% over $14,400
    Over $19,200 but not over $24,000       $1,030 plus 7.20% over $19,200
    Over $24,000 but not over $36,000       $1,354 plus 7.60% over $24,000
    Over $36,000 but not over $48,000       $2,266 plus 7.90% over $36,000
    Over $48,000 but not over $150,000      $3,214 plus 8.25% over $48,000
    Over $150,000 but not over $175,000     $11,629 plus 9.00% over $150,000
    Over $175,000 but not over $200,000     $13,879 plus 10.00% over $175,000
    Over $200,000                           $16,379 plus 11.00% over $200,000 
    
    MARRIED TAXPAYERS FILING JOINT RETURNS AND CERTAIN WIDOWS AND WIDOWERS
    If taxable income is:                   Your tax is:
    Not over $4,800                         1.40% of taxable income
    Over $4,800 but not over $9,600         $67 plus 3.20% over $4,800
    Over $9,600 but not over $19,200        $221 plus 5.50% over $9,600
    Over $19,200 but not over $28,800       $749 plus 6.40% over $19,200
    Over $28,800 but not over $38,400       $1,363 plus 6.80% over $28,800
    Over $38,400 but not over $48,000       $2,016 plus 7.20% over $38,400
    Over $48,000 but not over $72,000       $2,707 plus 7.60% over $48,000
    Over $72,000 but not over $96,000       $4,531 plus 7.90% over $72,000
    Over $96,000 but not over $300,000      $6,427 plus 8.25% over $96,000
    Over $300,000 but not over $350,000     $23,257 plus 9.00% over $300,000
    Over $350,000 but not over $400,000     $27,757 plus 10.00% over $350,000
    Over $400,000                           $32,757 plus 11.00% over $400,000
     
    UNMARRIED HEADS OF HOUSEHOLD
    If taxable income is:                   Your tax is:
    Not over $3,600                         1.40% of taxable income
    Over $3,600 but not over $7,200         $50 plus 3.20% over $3,600
    Over $7,200 but not over $14,400        $166 plus 5.50% over $7,200
    Over $14,400 but not over $21,600       $562 plus 6.40% over $14,400
    Over $21,600 but not over $28,800       $1,022 plus 6.80% over $21,600
    Over $28,800 but not over $36,000       $1,512 plus 7.20% over $28,800
    Over $36,000 but not over $54,000       $2,030 plus 7.60% over $36,000
    Over $54,000 but not over $72,000       $3,398 plus 7.90% over $54,000
    Over $72,000 but not over $225,000      $4,820 plus 8.25% over $72,000
    Over $225,000 but not over $262,500     $17,443 plus 9.00% over $225,000
    Over $262,500 but not over $300,000     $20,818 plus 10.00% over $262,500
    Over $300,000                           $24,568 plus 11.00% over $300,000

    DEDUCTIONS AND EXEMPTIONS
    https://files.hawaii.gov/tax/news/pubs/22outline.pdf
    PERSONAL EXEMPTION: $1,144 [(1) NET INCOME, MEASURE AND RATE OF TAX]
    STANDARD DEDUCTION:
    MARRIED FILING JOINTLY OR SURVIVING SPOUSE WITH DEPENDENT CHILD: $4,400
    SINGLE OR MARRIED FILING SEPARATELY: $2,200
    HEAD OF HOUSEHOLD: $3,212
    
    '''
    elif state == 'Hawaii':
        # $1144 dependent dedcution
        if maritalStatus == "Married":
            if stateDeductions == 0:
                stateDeductions = 6688 + 1144 * dependents
            if agi > 400000:
                stateBracket = .11
                margin = agi - 400000
                taxes = 32757.2 + margin * stateBracket
            elif agi > 350000:
                stateBracket = .1
                margin = agi - 350000
                taxes = 27757.2 + margin * stateBracket
            elif agi > 300000:
                stateBracket = .09
                margin = agi - 300000
                taxes = 23257.2 + margin * stateBracket
            elif agi > 96000:
                stateBracket = .0825
                margin = agi - 96000
                taxes = 6427.2 + margin * stateBracket
            elif agi > 72000:
                stateBracket = .079
                margin = agi - 72000
                taxes = 4531.2 + margin * stateBracket
            elif agi > 48000:
                stateBracket = .076
                margin = agi - 48000
                taxes = 2707.2 + margin * stateBracket
            elif agi > 38400:
                stateBracket = .072
                margin = agi - 38400
                taxes = 2016 + margin * stateBracket
            elif agi > 28800:
                stateBracket = .068
                margin = agi - 28800
                taxes = 1363.2 + margin * stateBracket
            elif agi > 19200:
                stateBracket = .064
                margin = agi - 19200
                taxes = 748.8 + margin * stateBracket
            elif agi > 9600:
                stateBracket = .055
                margin = agi - 9600
                taxes = 220.8 + margin * stateBracket
            elif agi > 4800:
                stateBracket = .032
                margin = agi - 4800
                taxes = 67.2 + margin * stateBracket
            else:
                stateBracket = .014
                taxes = agi * stateBracket
        else:
            if stateDeductions == 0:
                stateDeductions = 3344 + 1144 * dependents
            agi -= stateDeductions
            if agi > 200000:
                stateBracket = .11
                margin = agi - 200000
                taxes = 16378.6 + margin * stateBracket
            elif agi > 175000:
                stateBracket = .1
                margin = agi - 175000
                taxes = 13878.6 + margin * stateBracket
            elif agi > 150000:
                stateBracket = .09
                margin = agi - 150000
                taxes = 11628.6 + margin * stateBracket
            elif agi > 48000:
                stateBracket = .0825
                margin = agi - 48000
                taxes = 3213.6 + margin * stateBracket
            elif agi > 36000:
                stateBracket = .079
                margin = agi - 36000
                taxes = 2265.6 + margin * stateBracket
            elif agi > 24000:
                stateBracket = .076
                margin = agi - 24000
                taxes = 1353.6 + margin * stateBracket
            elif agi > 19200:
                stateBracket = .072
                margin = agi - 19200
                taxes = 1008 + margin * stateBracket
            elif agi > 14400:
                stateBracket = .068
                margin = agi - 14400
                taxes = 681.6 + margin * stateBracket
            elif agi > 9600:
                stateBracket = .064
                margin = agi - 9600
                taxes = 374.4 + margin * stateBracket
            elif agi > 4800:
                stateBracket = .055
                margin = agi - 4800
                taxes = 110.4 + margin * stateBracket
            elif agi > 2400:
                stateBracket = .032
                margin = agi - 2400
                taxes = 33.6 + margin * stateBracket
            else:
                stateBracket = .014
                taxes = agi * stateBracket

    '''
    STATE INCOME TAXES
    https://tax.idaho.gov/taxes/income-tax/individual-income/individual-income-tax-rate-schedule/
    Single
    At least	Less than	Tax	Rate
    $1	        $1,662	    $0.00	plus 1.0% of the amount over $0
    $1,662  	$4,987	    $16.62	plus 3.0% of the amount over $1,662
    $4,987	    $8,311	    $116.36	plus 4.5% of the amount over $4,987
    $8,311		            $265.96	plus 6.0% of the amount over $8,311
    Married
    At least	Less than	Tax	Rate
    $1	        $3,324	    $0.00	plus 1.0% of the amount over $0
    $3,324	    $9,974	    $33.24	plus 3.0% of the amount over $3,324
    $9,974	    $16,622	    $232.72	plus 4.5% of the amount over $9,974
    $16,622		            $531.92	plus 6.0% of the amount over $16,622
    
    '''
    elif state == 'Idaho':
        if maritalStatus == 'Married':
            if stateDeductions == 0:
                stateDeductions = 25100
            agi -= stateDeductions
            if agi > 23520:
                stateBracket = .06925
                margin = agi - 23520
                taxes = 1058.4 + margin * stateBracket
            elif agi > 15680:
                stateBracket = .06625
                margin = agi - 15680
                taxes = 568.4 + margin * stateBracket
            elif agi > 12544:
                stateBracket = .05625
                margin = agi - 12544
                taxes = 392 + margin * stateBracket
            elif agi > 9408:
                stateBracket = .04625
                margin = agi - 9408
                taxes = 246.96 + margin * stateBracket
            elif agi > 6272:
                stateBracket = .03625
                margin = agi - 6272
                taxes = 133.28 + margin * stateBracket
            elif agi > 3136:
                stateBracket = .03125
                margin = agi - 3136
                taxes = 35.28 + margin * stateBracket
            else:
                stateBracket = .01125
                taxes = agi * stateBracket
        else:
            if stateDeductions == 0:
                stateDeductions = 12550
            agi -= stateDeductions
            if agi > 11760:
                stateBracket = .06925
                margin = agi - 11760
                taxes = 529.2 + margin * stateBracket
            elif agi > 7840:
                stateBracket = .06625
                margin = agi - 7840
                taxes = 284.2 + margin * stateBracket
            elif agi > 6272:
                stateBracket = .05625
                margin = agi - 6272
                taxes = 196 + margin * stateBracket
            elif agi > 4704:
                stateBracket = .04625
                margin = agi - 4704
                taxes = 123.48 + margin * stateBracket
            elif agi > 3136:
                stateBracket = .03625
                margin = agi - 3136
                taxes = 66.64 + margin * stateBracket
            elif agi > 1568:
                stateBracket = .03125
                margin = agi - 1568
                taxes = 17.64 + margin * stateBracket
            else:
                stateBracket = .01125
                taxes = agi * stateBracket

    '''
    STATE INCOME TAXES
    https://tax.illinois.gov/research/taxrates/income.html#IndividualIncome
    4.95% on all income

    DEDUCTIONS
    https://tax.illinois.gov/content/dam/soi/en/web/tax/forms/incometax/documents/currentyear/individual/il-1040-instr.pdf
    (P.8) SINGLE DEDUCTION $2,425?
    MARRIED FILINJ JOINTLY DEDUCTION $4,850?

    RECIPROCITY AGREEMENTS
    https://tax.illinois.gov/content/dam/soi/en/web/tax/forms/incometax/documents/currentyear/individual/il-1040-instr.pdf
    (P.3) Iowa, Kentucky, Michigan, or Wisconsin
    '''
    elif state == 'Illinois':
        if maritalStatus == 'Married':
            # Cannot claim personal exemption if AGI above 500k
            if stateDeductions == 0 and agi < 500000:
                stateDeductions = 4850 + (dependents * 2425)
        else:
            # Cannot claim personal exemption if AGI above 500k
            if stateDeductions == 0 and agi < 250000:
                stateDeductions = 2425 + (dependents * 2425)
        # $2325 deduction per dependent
        agi -= stateDeductions
        stateBracket = .0495
        taxes = agi * stateBracket
    '''
    STATE INCOME TAXES
    https://www.in.gov/dor/tax-forms/2022-individual-income-tax-forms/ (IT-40PNR Booklet)
    3.23% on all income
    
    LOCAL INCOME TAXES
    https://www.in.gov/dor/files/2022-county-tax-rates-and-codes.pdf

    RECRIPROCAL AGREEMENTS
    Kentucky, Ohio, Wisconsin, Michigan, Pennsylvania
    '''
    elif state == 'Indiana':
        # ! $1000-1500 dependent deduction but 1500 in nearly all cases (19 or younger or in college)
        if stateDeductions == 0:
            if maritalStatus == 'Married':
                stateDeductions = 2000 + (dependents * 1500)
            else:
                stateDeductions = 1000 + (dependents * 1500)
        agi -= stateDeductions
        stateBracket = .0323
        taxes = agi * stateBracket
        indianaCounties = {
        'Adams': .0162,
        'Allen': .0148,
        'Bartholomew': .0175,
        'Benton': .0179,
        'Blackford': .0150,
        'Boone': .0150,
        'Brown': .0252,
        'Carroll': .0227,
        'Cass': .0260,
        'Clark': .0200,
        'Clay': .0225,
        'Clinton': .0225,
        'Crawford': .0100,
        'Daviess': .0150,
        'Dearborn': .0120,
        'Decatur': .0235,
        'DeKalb': .0213,
        'Delaware': .0150,
        'Dubois': .0100,
        'Elkhart': .0200,
        'Fayette': .0237,
        'Floyd': .0135,
        'Fountain': .0210,
        'Franklin': .0150,
        'Fulton': .0238,
        'Gibson': .0070,
        'Grant': .0255,
        'Greene': .0175,
        'Hamilton': .0100,
        'Hancock': .0174,
        'Harrison': .0100,
        'Hendricks': .0150,
        'Henry': .0150,
        'Howard': .0175,
        'Huntington': .0195,
        'Jackson': .0210,
        'Jasper': .0286,
        'Jay': .0245,
        'Jefferson': .0035,
        'Jennings': .0315,
        'Johnson': .0100,
        'Knox': .0100,
        'Kosciusko': .0100,
        'LaGrange': .0165,
        'Lake': .0150,
        'LaPorte': .0095,
        'Lawrence': .0175,
        'Madison': .0175,
        'Marion': .0202,
        'Marshall': .0125,
        'Martin': .0175,
        'Miami': .0254,
        'Monroe': .0135,
        'Montgomery': .0230,
        'Morgan': .0272,
        'Newton': .0100,
        'Noble': .0175,
        'Ohio': .0125,
        'Orange': .0175,
        'Owen': .0130,
        'Parke': .0265,
        'Perry': .0181,
        'Pike': .0075,
        'Porter': .0050,
        'Posey': .0125,
        'Pulaski': .0338,
        'Putnam': .0200,
        'Randolph': .0225,
        'Ripley': .0138,
        'Rush': .0210,
        'St. Joseph': .0175,
        'Scott': .0216,
        'Shelby': .0150,
        'Spencer': .0080,
        'Starke': .0171,
        'Steuben': .0179,
        'Sullivan': .0060,
        'Switzerland': .0100,
        'Tippecanoe': .0110,
        'Tipton': .0260,
        'Union': .0175,
        'Vanderburgh': .0120,
        'Vermillion': .0150,
        'Vigo': .0200,
        'Wabash': .0290,
        'Warren': .0212,
        'Warrick': .0050,
        'Washington': .0200,
        'Wayne': .0150,
        'Wells': .0210,
        'White': .0232,
        'Whitley': .0148}
        localBracket = indianaCountie[county]
        taxes += agi * localBracket
        stateBracket += localBracket

    '''
    STATE INCOME TAXES
    https://tax.iowa.gov/2023-changes-iowa-individual-income-tax#:~:text=Individual%20Income%20Tax%20Rates%20(HF%202317)&text=Beginning%20in%20tax%20year%202026,who%20file%20a%20joint%20return.
    
    Income Tax Brackets	Rates (Brackets double for married filing jointly)
    Lower Limit	    Upper Limit	    TY 2023	    TY 2024 	TY 2025	    TY 2026
    $0	            $6,000	        4.40%	    4.40%   	4.40%   	3.90%
    $6,001	        $30,000	        4.82%   	4.82%   	4.82%   	3.90%
    $30,001	        $75,000	        5.70%	    5.70%	    4.82%   	3.90%
    $75,001	And over            	6.00%	    5.70%   	4.82%   	3.90%

    LOCAL INCOME TAXES
    www.freetaxusa.com/FreeTaxUSA/formdownload?form=ia_school_dist.pdf

    RETIREMENT INCOME EXCLUSION
    https://tax.iowa.gov/2023-changes-iowa-individual-income-tax#:~:text=Individual%20Income%20Tax%20Rates%20(HF%202317)&text=Beginning%20in%20tax%20year%202026,who%20file%20a%20joint%20return.
    ALLOWS FOR FREE TRADITIONAL IRA TO ROTH IRA CONVERSION!?

    RECIPROCITY AGREEMENTS
    https://tax.iowa.gov/iowa-illinois-reciprocal-agreement
    Illinois 

    '''
    elif state == 'Iowa':
        # $40 credit per dependent
        if stateDeductions == 0:
            if maritalStatus == 'Married':
                stateDeductions = 5240
                taxes = -(80 + (dependents * 40))
            else:
                stateDeductions = 2130
                taxes = -(40 + (dependents * 40))
            # Iowa lets you deduct federal income taxes
            stateDeductions += federalTaxes
        agi -= stateDeductions
        taxes -= dependents * 40
        if maritalStatus != 'Married':
            if agi > 75000:
                stateBracket = .06
                margin = agi - 75000
                taxes += 3985.8 +  margin * stateBracket
            elif agi > 30000:
                stateBracket = .057
                margin = agi - 30000
                taxes += 1420.8 + margin * stateBracket
            elif agi > 6000:
                stateBracket = .0482
                margin = agi - 6000
                taxes += 264 + margin * stateBracket
            else:
                stateBracket = .044
                taxes += agi * stateBracket
        else:
            if agi > 150000:
                stateBracket = .06
                margin = agi - 150000
                taxes += 7971.6 +  margin * stateBracket
            elif agi > 60000:
                stateBracket = .057
                margin = agi - 60000
                taxes += 2841.6 + margin * stateBracket
            elif agi > 12000:
                stateBracket = .0482
                margin = agi - 12000
                taxes += 528 + margin * stateBracket
            else:
                stateBracket = .044
                taxes += agi * stateBracket
        
        # County Taxes https://www.freetaxusa.com/FreeTaxUSA/formdownload?form=ia_school_dist.pdf
        if county == 'Appanoose County':
            localBracket = .01
            taxes += agi * localBracket
            stateBracket += localBracket
        # Levies taxes as a percentage of state taxes
        else:
            iowaCounties = {'AGWSR SD': 0.08,
                    'AHSTW SD': 0.09,
                    'Adair-Casey SD': 0.08,
                    'Akron-Westfield SD': 0.04,
                    'Albia SD': 0.02,
                    'Alburnett SD': 0.01,
                    'Alden SD': 0.09,
                    'Algona SD': 0.06,
                    'Allamakee SD': 0.08,
                    'Alta-Aurelia SD': 0.09,
                    'Ames SD': 0.04,
                    'Anamosa SD': 0.07,
                    'Andrew SD': 0.05,
                    'Aplington-Parkersburg SD': 0.08,
                    'Ar-We-Va SD': 0.09,
                    'Atlantic SD': 0.12,
                    'Audubon SD': 0.06,
                    'BCLUW SD': 0.09,
                    'Ballard SD': 0.02,
                    'Baxter SD': 0.09,
                    'Bedford SD': 0.10,
                    'Belle Plaine SD': 0.06,
                    'Bellevue SD': 0.03,
                    'Belmond-Klemme SD': 0.03,
                    'Bennett SD': 0.01,
                    'Benton SD': 0.03,
                    'Bondurant-Farrar SD': 0.03,
                    'Boone SD': 0.06,
                    'Boyden-Hull SD': 0.04,
                    'Boyer Valley SD': 0.10,
                    'B-G-M SD': 0.05,
                    'CAL SD': 0.16,
                    'CAM SD': 0.10,
                    'Calamus-Wheatland SD': 0.06,
                    'Cardinal SD': 0.10,
                    'Carroll SD': 0.03,
                    'Cedar Rapids SD': 0.05,
                    'Center Point-Urbana SD': 0.06,
                    'Centerville SD': 0.03,
                    'Central Clayton SD': 0.01,
                    'Central De Witt SD': 0.07,
                    'Central Decatur SD': 0.03,
                    'Central Lee SD': 0.09,
                    'Central Lyon SD': 0.08,
                    'Central Springs SD': 0.07,
                    'Chariton SD': 0.02,
                    'Charles City SD': 0.06,
                    'Charter Oak-Ute SD': 0.10,
                    'Cherokee SD': 0.05,
                    'Clarinda SD': 0.08,
                    'Clarke SD': 0.05,
                    'Clarksville SD': 0.09,
                    'Clear Creek-Amana SD': 0.07,
                    'Clear Lake SD': 0.05,
                    'Clinton SD': 0.08,
                    'Colfax-Mingo SD': 0.07,
                    'Collins-Maxwell SD': 0.08,
                    'Columbus SD': 0.10,
                    'Coon Rapids-Bayard SD': 0.07,
                    'Corning SD': 0.07,
                    'Creston SD': 0.06,
                    'Danville SD': 0.02,
                    'Davis County SD': 0.01,
                    'Decorah SD': 0.06,
                    'Delwood SD': 0.09,
                    'Denison SD': 0.08,
                    'Denver SD': 0.04,
                    'Diagonal SD': 0.12,
                    'Dike-New Hartford SD': 0.08,
                    'Dunkerton SD': 0.06,
                    'Durant SD': 0.09,
                    'Eagle Grove SD': 0.07,
                    'East Buchanan SD': 0.05,
                    'East Marshall SD': 0.10,
                    'East Mills SD': 0.11,
                    'East Sac County SD': 0.01,
                    'East Union SD': 0.13,
                    'Eastern Allamakee SD': 0.10,
                    'Easton Valley SD': 0.04,
                    'Eddyville-Blakesburg-Fremont SD': 0.05,
                    'Edgewood-Colesburg SD': 0.08,
                    'Eldora-New Providence SD': 0.05,
                    'Emmetsburg SD': 0.13,
                    'English Valleys SD': 0.16,
                    'Essex SD': 0.09,
                    'Estherville-Lincoln Cent. SD': 0.10,
                    'Exira-Elk Horn-Kimballton SD': 0.07,
                    'Fairfield SD': 0.01,
                    'Forest City SD': 0.10,
                    'Fort Dodge SD': 0.02,
                    'Fort Madison SD': 0.06,
                    'Fremont-Mills SD': 0.17,
                    'GMG SD': 0.10,
                    'Galva-Holstein SD': 0.02,
                    'Garner-Hayfield-Vent. SD': 0.06,
                    'George-Little Rock SD': 0.12,
                    'Gilmore City-Bradgate SD': 0.05,
                    'Gladbrook-Reinbeck SD': 0.03,
                    'Glenwood SD': 0.07,
                    'Glidden-Ralston SD': 0.08,
                    'Graettinger-Terril SD': 0.02,
                    'Greene County SD': 0.12,
                    'Grinnell-Newburg SD': 0.02,
                    'Griswold SD': 0.09,
                    'Grundy Center SD': 0.06,
                    'Guthrie Center SD': 0.07,
                    'Hamburg SD': 0.07,
                    'Hampton-Dumont SD': 0.03,
                    'Harlan SD': 0.07,
                    'Harmony SD': 0.10,
                    'Hartley-Melvin-Sanborn SD': 0.07,
                    'Highland SD': 0.07,
                    'Hinton SD': 0.07,
                    'Howard-Winneshiek SD': 0.06,
                    'Hudson SD': 0.02,
                    'Humboldt SD': 0.01,
                    'IKM-Manning SD': 0.08,
                    'Independence SD': 0.07,
                    'Indianola SD': 0.05,
                    'Iowa City SD': 0.05,
                    'Iowa Falls SD': 0.07,
                    'Iowa Valley SD': 0.13,
                    'Janesville SD': 0.07,
                    'Keota SD': 0.01,
                    'Kingsley-Pierson SD': 0.04,
                    'Knoxville SD': 0.06,
                    'Lake Mills SD': 0.10,
                    'Lamoni SD': 0.08,
                    'Laurens-Marathon SD': 0.08,
                    'Lawton-Bronson SD': 0.07,
                    'Lenox SD': 0.02,
                    'Lewis Central SD': 0.04,
                    'Lisbon SD': 0.01,
                    'Logan-Magnolia SD': 0.07,
                    'Lone Tree SD': 0.08,
                    'Louisa-Muscatine SD': 0.09,
                    'Lu Verne SD': 0.13,
                    'Lynnville-Sully SD': 0.07,
                    'MFL Mar Mac SD': 0.08,
                    'Madrid SD': 0.04,
                    'Manson-Northwest Webster SD': 0.07,
                    'Maple Valley-Anthon Oto SD': 0.04,
                    'Maquoketa SD': 0.09,
                    'Marcus-Meriden Cleghorn SD': 0.08,
                    'Marion SD': 0.04,
                    'Martensdale-St Marys SD': 0.01,
                    'Mason City SD': 0.07,
                    'Mediapolis SD': 0.10,
                    'Melcher-Dallas SD': 0.05,
                    'Mid-Prairie SD': 0.14,
                    'Midland SD': 0.14,
                    'Missouri Valley SD': 0.05,
                    'Moc-Floyd Valley SD': 0.04,
                    'Montezuma SD': 0.08,
                    'Monticello SD': 0.04,
                    'Moravia SD': 0.11,
                    'Mormon Trail SD': 0.06,
                    'Morning Sun SD': 0.01,
                    'Moulton-Udell SD': 0.12,
                    'Mount Ayr SD': 0.06,
                    'Mount Pleasant SD': 0.05,
                    'Mount Vernon SD': 0.06,
                    'Murray SD': 0.11,
                    'Muscatine SD': 0.01,
                    'Nashua-Plainfield SD': 0.09,
                    'Nevada SD': 0.05,
                    'New Hampton SD': 0.06,
                    'New London SD': 0.09,
                    'Newell-Fonda SD': 0.10,
                    'Newton SD': 0.07,
                    'Nodaway Valley SD': 0.03,
                    'North Cedar SD': 0.10,
                    'North Fayette Valley SD': 0.05,
                    'North Iowa SD': 0.11,
                    'North Kossuth SD': 0.06,
                    'North Linn SD': 0.05,
                    'North Mahaska SD': 0.03,
                    'North Polk SD': 0.01,
                    'North Scott SD': 0.01,
                    'North Tama SD': 0.07,
                    'North Union SD': 0.08,
                    'North Winneshiek SD': 0.10,
                    'Northeast SD': 0.10,
                    'Northeast Hamilton SD': 0.05,
                    'Northwood-Kensett SD': 0.05,
                    'OABCIG SD': 0.01,
                    'Oelwein SD': 0.07,
                    'Ogden SD': 0.05,
                    'Okoboji SD': 0.02,
                    'Orient-Macksburg SD': 0.15,
                    'Osage SD': 0.02,
                    'Oskaloosa SD': 0.04,
                    'PCM SD': 0.05,
                    'Panorama SD': 0.04,
                    'Paton-Churdan SD': 0.05,
                    'Pekin SD': 0.09,
                    'Pella SD': 0.04,
                    'Perry SD': 0.03,
                    'Pleasantville SD': 0.09,
                    'Pocahontas Area SD': 0.01,
                    'Postville SD': 0.15,
                    'Prairie Valley SD': 0.06,
                    'Red Oak SD': 0.10,
                    'Remsen-Union SD': 0.07,
                    'Riceville SD': 0.10,
                    'River Valley SD': 0.10,
                    'Riverside SD': 0.09,
                    'Roland-Story SD': 0.08,
                    'Rudd-Rockford-Marble Rock SD': 0.03,
                    'Ruthven-Ayrshire SD': 0.10,
                    'Schaller-Crestland SD': 0.02,
                    'Schleswig SD': 0.01,
                    'Seymour SD': 0.10,
                    'Sheldon SD': 0.07,
                    'Shenandoah SD': 0.12,
                    'Sibley-Ocheyedan SD': 0.10,
                    'Sidney SD': 0.20,
                    'Sigourney SD': 0.01,
                    'Sioux Center SD': 0.05,
                    'Sioux Central SD': 0.08,
                    'Sioux City SD': 0.03,
                    'Solon SD': 0.05,
                    'South Hamilton SD': 0.08,
                    'South O\'Brien SD': 0.10,
                    'South Page SD': 0.13,
                    'South Tama SD': 0.09,
                    'South Winneshiek SD': 0.06,
                    'Southeast Polk SD': 0.05,
                    'Southeast Warren SD': 0.10,
                    'Southeast Webster-Grand SD': 0.02,
                    'Spencer SD': 0.04,
                    'Spirit Lake SD': 0.06,
                    'Springville SD': 0.06,
                    'St Ansgar SD': 0.07,
                    'Stanton SD': 0.08,
                    'Starmont SD': 0.02,
                    'Storm Lake SD': 0.03,
                    'Stratford SD': 0.08,
                    'Sumner-Fredericksburg SD': 0.07,
                    'Tipton SD': 0.10,
                    'Treynor SD': 0.05,
                    'Tri-Center SD': 0.01,
                    'Tripoli SD': 0.09,
                    'Twin Cedars SD': 0.04,
                    'Twin Rivers SD': 0.10,
                    'Union SD': 0.08,
                    'United SD': 0.07,
                    'Van Buren SD': 0.09,
                    'Van Meter SD': 0.04,
                    'Villisca SD': 0.05,
                    'Vinton-Shellsburg SD': 0.07,
                    'Wapello SD': 0.08,
                    'Wapsie Valley SD': 0.12,
                    'Washington SD': 0.09,
                    'Waverly-Shell Rock SD': 0.06,
                    'Wayne SD': 0.02,
                    'Webster City SD': 0.04,
                    'West Branch SD': 0.02,
                    'West Central SD': 0.13,
                    'West Central Valley SD': 0.05,
                    'West Delaware Co SD': 0.05,
                    'West Fork SD': 0.01,
                    'West Hancock SD': 0.10,
                    'West Harrison SD': 0.02,
                    'West Liberty SD': 0.15,
                    'West Lyon SD': 0.10,
                    'West Marshall SD': 0.09,
                    'West Monona SD': 0.06,
                    'West Sioux SD': 0.09,
                    'Western Dubuque Co SD': 0.06,
                    'Westwood SD': 0.07,
                    'Whiting SD': 0.05,
                    'Williamsburg SD': 0.08,
                    'Wilton SD': 0.05,
                    'Winfield-Mt Union SD': 0.07,
                    'Winterset SD': 0.04,
                    'Woodbine SD': 0.14,
                    'Woodbury Central SD': 0.03,
                    'Woodward-Granger SD': 0.07}
            # Sets the local bracket to the local income tax rate
            localBracket = iowaCounties[county]
            # Multiplies state taxes and state bracket by the county factor
            taxes *= (1 + localBracket)
            stateBracket *= (1 + localBracket)

    ''' https://www.ksrevenue.gov/taxrates.html
     Tax year 2018 and all tax years thereafter
     Tax Rates, Resident, married, joint
        taxable income not over $30,000: 3.1 % (K.S.A. 79-32,110)
        taxable income over $30,000 but not over $60,000: $930 plus 5.25 % of excess over $30,000 (K.S.A. 79-32,110)
        taxable income over $60,000: $2,505 plus 5.7 % of excess over $60,000 (K.S.A. 79-32,110)
     Tax Rates, Resident, others
        taxable income not over $15,000: 3.1 % (79-32,110)
        taxable income over $15,000 but not over $30,000: $465 plus 5.25 % of excess over $15,000 (K.S.A. 79-32,110)
        taxable income over $30,000: $1252.50 plus 5.7 % of excess over $30,000 (K.S.A. 79-32,110)
    Privilege Tax:
        Banks total net income: 2.25% plus 2.125% surtax on taxable income over $25,000 4.375% K.S.A. (79-1107)
        Trusts and S&Ls total net income: 2.25% plus 2.25% surtax on taxable income over $25,000 4.50% (K.S.A. 79-1108)'''
    
    elif state == 'Kansas':
        if stateDeductions == 0:
            # $2250 dependent deduction
            if maritalStatus == 'Married':
                stateDeductions = 12000 + (dependents * 2250)
            else:
                stateDeductions = 5250 + (dependents * 2250)
        agi -= stateDeductions
        if agi > 30000:
            stateBracket = .057
            margin = agi - 30000
            taxes += 16.76 + margin * stateBracket
        elif agi > 15000:
            stateBracket = .0525
            margin = agi - 15000
            taxes += 5.53 + margin * stateBracket
        else:
            stateBracket = .031
            taxes += agi * stateBracket

    '''
    STATE INCOME TAX RATES
    https://revenue.ky.gov/News/Pages/DOR-Announces-Updates-to-Individual-Income-Tax-for-2023-Tax-Year.aspx
    https://revenue.ky.gov/Individual/Individual-Income-Tax/Pages/default.aspx

    DEDUCTIONS
    https://revenue.ky.gov/News/Pages/DOR-Announces-Updates-to-Individual-Income-Tax-for-2023-Tax-Year.aspx
    MARRIED - $5,960
    OTHERWISE - $2,980

    CHILD AND DEPENDENT CARE CREDIT
    https://revenue.ky.gov/Individual/Individual-Income-Tax/Pages/default.aspx
    20% OF THE FEDERAL CREDIT
    '''
    # !lots of weird local taxes
    elif state == 'Kentucky':
        if stateDeductions == 0:
            if maritalStatus == 'Married':
                stateDeductions = 5960
            else:
                stateDeductions = 2980
        # TODO add portion of federal child and dependent care credit
        agi -= stateDeductions
        stateBracket = .045
        taxes = agi * stateBracket
    
    '''
    STATE INCOME TAX RATES
    https://revenue.louisiana.gov/individualincometax
    
    MARRIED FILING JOINTLY OR QUALIFYING SURVIVING SPOUSE
    TAX BRACKET         RATE
    $0 - $25,000        1.85%
    $25,001 - $100,000   3.50%
    $100,001+            4.25%

    SINGLE, HEAD OF HOUESEHOLD, MARRIED FILING SEPERATELY
    TAX BRACKET         RATE
    $0 - $12,500        1.85%
    $12,501 - $50,000   3.50%
    $50,001+            4.25%

    DEDUCTIONS
    CREDIT OF $1,000 FOR EACH DEPENDENT OR EACH TAXPAYER/SPOUSE AGE 65 OR OLDER

    STANDARD DEDUCTION
    https://www.revenue.louisiana.gov/taxforms/6935(11_02)F.pdf
    MARRIED FILING JOINTLY OR QUALIFYING SURVIVING SPOUSE - $9,000
    SINGLE, HEAD OF HOUSEHOLD, MARRIED FILING SEPERATELY - $4,500
    '''
    elif state == 'Louisiana':
        # $1000 dependent tax deduction
        if maritalStatus == 'Married':
            if stateDeductions == 0:
                stateDeductions = 9000 + (dependents * 1000)
            agi -= stateDeductions
            if agi > 100000:
                stateBracket = .0425
                margin = agi - 100000
                taxes += 3087.5 + margin * stateBracket
            elif agi > 25000:
                stateBracket = .035
                margin = agi - 25000
                taxes += 462.5 + margin * stateBracket
            else:
                stateBracket = .0185
                taxes += agi * stateBracket
        else:
            if stateDeductions == 0:
                stateDeductions = 4500 + (dependents * 1000)
            agi -= stateDeductions
            if agi > 50000:
                stateBracket = .0425
                margin = agi - 50000
                taxes += 1543.75 + margin * stateBracket
            elif agi > 12500:
                stateBracket = .035
                margin = agi - 12500
                taxes += 231.25 + margin * stateBracket
            else:
                stateBracket = .0185
                taxes += agi * stateBracket

    '''
    STATE INCOME TAX
    https://www.maine.gov/revenue/tax-return-forms/individual-income-tax-2022
    https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/ind_tax_rate_sched_2022.pdf

    For Single Individuals and Married Persons Filing Separate Returns 
    If the taxable income is:           The tax is:  
    Less than $23,000                   5.8% of Maine taxable income
    $23,000 but less than $54,450       $1,334 plus 6.75% of excess over $23,000
    $54,450 or more                     $3,457 plus 7.15% of excess over $54,450
      
    Unmarried or Legally Separated Individuals who Qualify as Heads of Household
    If the taxable income is:           The tax is:  
    Less than $34,500                   5.8% of Maine taxable income
    $34,500 but less than $81,700       $2,001 plus 6.75% of excess over $34,500
    $81,700 or more                     $5,187 plus 7.15% of excess over $81,700       
    
    Married Individuals and Surviving Spouses Filing Joint Returns
    If the taxable income is:           The tax is:  
    Less than $46,000                   5.8% of Maine taxable income  
    $46,000 but less than $108,900      $2,668 plus 6.75% of excess over $46,000
    $108,900 or more                    $6,914 plus 7.15% of excess over $108,900 

    PERSONAL EXEMPTION - 4450
    
    STANDARD DEDUCTION MATCHES FEDERAL


    '''
    # !Personal deduction has phaseout, $300 dependent credit
    elif state == 'Maine':
        if maritalStatus == 'Married':
            if stateDeductions == 0:
                if agi < 167700:
                    stateDeductions = 33700
                # !$300 dependent tax credit, maybe phaseout range?
                taxes = -(dependents * 300)
            agi -= stateDeductions
            if agi > 108900:
                stateBracket = .0715
                margin = agi - 108900
                taxes += 6914 + margin * stateBracket
            elif agi > 46000:
                stateBracket = .0675
                margin = agi - 46000
                taxes += 2668 + margin * stateBracket
            else:
                stateBracket = .058
                taxes += agi * stateBracket
        elif maritalStatus == 'Single':
            # if stateDeductions == 0:
            #     if maritalStatus =='Single':
            #         if agi < 83850:
            #                 stateDeductions = 16850
            #         else:
            #             # !Phaseout range
            #             stateDeductions = 16850
            #     # marital status head of household
            #     else:
            #         if agi < 125750:
            #             stateDeductions = 16850
            #         else:
            #             # !Phaseout range
            #             stateDeductions = 16850
            #     # !$300 dependent tax credit, maybe phaseout range?
            #     taxes = -(dependents * 300)
            # agi -= stateDeductions
            if agi > 54450:
                stateBracket = .0715
                margin = agi - 54450
                taxes += 3457 + margin * stateBracket
            elif agi > 23000:
                stateBracket = .0675
                margin = agi - 23000
                taxes += 1334 + margin * stateBracket
            else:
                stateBracket = .058
                taxes += agi * stateBracket
        elif maritalStatus == 'Head of Household':
            if agi > 81700:
                stateBracket = .0715
                margin = agi - 81700
                taxes += 5187 + margin * stateBracket
            elif agi > 34500:
                stateBracket = .0675
                margin = agi - 34500
                taxes += 2001 + margin * stateBracket
            else:
                stateBracket = .058
                taxes += agi * stateBracket
        else:
            raise Exception('Marital status not recognized')
    
    '''
    STATE INCOME TAX
    https://www.marylandtaxes.gov/individual/income/tax-info/tax-rates.php
    
    2022
    Taxpayers Filing as Single, Married Filing Separately, Dependent Taxpayers or Fiduciaries	  
    Taxable Net Income	            Maryland Tax	                                              
    $0 - $1,000	                    2.00%	                                                      
    $1,000 - $2,000	                $20 plus 3.00% of the excess over $1,000	                  
    $2,000 - $3,000	                $50 plus 4.00% of the excess over $2,000	                  
    $3,000 - $100,000	            $90 plus 4.75% of the excess over $3,000	                 
    $100,000 - $125,000	            $4,697.50 plus 5.00% of the excess over $100,000	         
    $125,000 - $150,000	            $5,947.50 plus 5.25% of the excess over $125,000	          
    $150,000 - $250,000	            $7,260.00 plus 5.50% of the excess over $150,000	          
    Over $250,000	                $12,760.00 plus 5.75% of the excess of $250,000	              

    Taxpayers Filing Joint Returns, Head of Household, or Qualifying Widows/Widowers	 	 
    Taxable Net Income	           Maryland Tax
    $0 - $1,000	                   2.00%
    $1,000 - $2,000	               $20 plus 3.00% of the excess over $1,000
    $2,000 - $3,000	               $50 plus 4.00% of the excess over $2,000
    $3,000 - $150,000	           $90 plus 4.75% of the excess over $3,000
    $150,000 - $175,000	           $7,072.50 plus 5.00% of the excess over $150,000
    $175,000 - $225,000	           $8,322.50 plus 5.25% of the excess over $175,000
    $225,000 - $300,000	           $10,947.50 plus 5.50% of the excess over $225,000
    Over $300,000	                   $15,072.50 plus 5.75% of the excess over $300,000

    LOCAL INCOME TAX (SAME LINK)
    Local Tax Area	        2023
    Allegany County		    .0303
    Anne Arundel County     .0281*
    Baltimore City	    	.0320
    Baltimore County		.0320
    Calvert County	    	.0300
    Caroline County	        .0320
    Carroll County	        .0303
    Cecil County	        .0280
    Charles County	        .0303
    Dorchester County	    .0320
    Frederick County	   	.0296**
    Garrett County	        .0265
    Harford County	        .0306
    Howard County	        .0320
    Kent County	            .0320
    Montgomery County	  	.0320
    Prince George's County	.0320
    Queen Anne's County	    .0320
    St. Mary's County	    .0300
    Somerset County	        .0320
    Talbot County	        .0240
    Washington County       .0295
    Wicomico County	        .0320
    Worcester County    	.0225
    Nonresidents	    	.0225

    * Anne Arundel Co. The local tax rates for taxable year 2023 are as follows:
    (1) .0270 of an individual’s Maryland taxable income of $1 through $50,000; and
    (2) .0281 of an individual’s Maryland taxable income in excess of $50,000.

    ** Frederick Co. The local tax rates for taxable year 2023 are as follows:
    (1) .0275 for taxpayers with Maryland taxable income of $100,000 or less and a filing status of married filing joint, head of household, and qualifying widow(er) with dependent child;
    (2) .0275 for taxpayers with Maryland taxable income of $50,000 or less and a filing status of single, married filing separately, and dependent; and
    (3) .0296 for all other taxpayers.    
    '''
    # Longer list for local taxes and lower local taxes for nonresidents
    elif state == 'Maryland':
        if maritalStatus == 'Married':
            if stateDeductions == 0:
                # Deduction is 15% of AGI with a $3100 minimum and a $4650 cap
                if agi > 31000:
                    stateDeductions = 4650
                elif agi > 20666.67:
                    stateDeductions = agi * .15
                else:
                    stateDeductions = 3100
                # !$3200 dependent tax deduction, move for itemized?
                stateDeductions += dependents * 3200
            agi -= stateDeductions
            if agi > 250000:
                stateBracket = .0575
                margin = agi - 250000
                taxes = 12760 + margin * stateBracket
            elif agi > 150000:
                stateBracket = .055
                margin = agi - 150000
                taxes = 7260 + margin * stateBracket
            elif agi > 125000:
                stateBracket = .0525
                margin = agi - 125000
                taxes = 5947.5 + margin * stateBracket
            elif agi > 100000:
                stateBracket = .05
                margin = agi - 100000
                taxes = 4697.5 + margin * stateBracket
            elif agi > 3000:
                stateBracket = .0475
                margin = agi - 3000
                taxes = 90 + margin * stateBracket
            elif agi > 2000:
                stateBracket = .04
                margin = agi - 2000
                taxes = 50 + margin * stateBracket
            elif agi > 1000:
                stateBracket = .03
                margin = agi - 1000
                taxes = 20 + margin * stateBracket
            else:
                stateBracket = .02
                taxes = agi * stateBracket
        else:
            if stateDeductions == 0:
                if agi > 31000:
                    stateDeductions = 4650
                elif agi > 20666.67:
                    stateDeductions = agi * .15
                else:
                    stateDeductions = 3100
                # !$3200 dependent tax deduction
                stateDeductions += dependents * 3200
            agi -= stateDeductions
            if agi > 300000:
                stateBracket = .0575
                margin = agi - 300000
                taxes = 15072.5 + margin * stateBracket
            elif agi > 225000:
                stateBracket = .055
                margin = agi - 225000
                taxes = 10947.5 + margin * stateBracket
            elif agi > 175000:
                stateBracket = .0525
                margin = agi - 175000
                taxes = 8322.5 + margin * stateBracket
            elif agi > 150000:
                stateBracket = .05
                margin = agi - 100000
                taxes = 7072.5 + margin * stateBracket
            elif agi > 3000:
                stateBracket = .0475
                margin = agi - 3000
                taxes = 90 + margin * stateBracket
            elif agi > 2000:
                stateBracket = .04
                margin = agi - 2000
                taxes = 50 + margin * stateBracket
            elif agi > 1000:
                stateBracket = .03
                margin = agi - 1000
                taxes = 20 + margin * stateBracket
            else:
                stateBracket = .02
                taxes = agi * stateBracket
        # TODO SPECIAL TAXES
        # Anne Arundel County     .0281*
        # Frederick County	   	.0296**
        marylandCounties = {
                            "Allegany County":		    .0303,
                            "Baltimore City":	    	.0320,
                            "Baltimore County":		.0320,
                            "Calvert County":	    	.0300,
                            "Caroline County":	        .0320,
                            "Carroll County":	        .0303,
                            "Cecil County":	        .0280,
                            "Charles County":	        .0303,
                            "Dorchester County":	    .0320,
                            "Garrett County":	        .0265,
                            "Harford County":	        .0306,
                            "Howard County":	        .0320,
                            "Kent County":	            .0320,
                            "Montgomery County":	  	.0320,
                            "Prince George's County":	.0320,
                            "Queen Anne's County":	    .0320,
                            "St. Mary's County":	    .0300,
                            "Somerset County":	        .0320,
                            "Talbot County":	        .0240,
                            "Washington County":       .0295,
                            "Wicomico County":	        .0320,
                            "Worcester County":    	.0225}
        localBracket = marylandCounties[county]
        taxes += agi * localBracket
        stateBracket += localBracket 
        #TODO Nonresidents	    	.0225
    '''
    STATE INCOME TAX 
    https://www.mass.gov/service-details/massachusetts-tax-rates
    5%

    CAPITAL GAINS TAX (SAME LINK)
    LONG TERM - 12%
    SHORT TERM - 5%

    STATE DEDUCTIONS 
    https://www.mass.gov/service-details/view-massachusetts-personal-income-tax-exemptions
    $1000 deduction per dependent

    STANDARD DEDUCTION
    SINGLE OR MARRIED FILING SEPARATELY - $4,400
    MARRIED FILING JOINTLY OR QUALIFYING WIDOW - $8,800
    HEAD OF HOUSEHOLD - $6,800

    https://www.mass.gov/service-details/view-child-and-dependent-related-credits
    $240 credit per dependent, max 2

    '''
    elif state == 'Massachusetts':
        if stateDeductions == 0:
            stateDeductions = 1000 * dependents
            if maritalStatus == 'Married':
                stateDeductions += 8800
            elif maritalStatus == 'Head of household':
                stateDeductions += 6800
            else:
                stateDeductions += 4400
        if dependents > 2:
            dependents = 2
        # TODO IMPLEMENT THIS CASE
        if maritalStatus != 'Married filing separately':
            taxes = -dependents * 240
        agi -= stateDeductions
        stateBracket = .05
        taxes = agi * stateBracket
    
    '''
    STATE INCOME TAXES
    https://www.michigan.gov/taxes/iit/new-developments-for-tax-year-2022
    
    4.25% tax rate

    Exemption allowances:
    $5,000 for personal and dependent exemptions
    $2,900 for special exemptions
    $400 for qualified disabled veterans
    $5,000 for number of certificates of stillbirth from MDHHS

    LOCAL INCOME TAXES
    https://www.michigan.gov/taxes/questions/iit/accordion/general/what-cities-impose-an-income-tax

    Albion	          1%	
    Battle Creek	  1%	
    Benton Harbor     1%	
    Big Rapids	      1%	
    Detroit           2.4%  
    East Lansing	  1%
    Flint	          1%	
    Grand Rapids      1.5%
    Grayling	      1% 
    Hamtramck	      1%
    Highland Park     2%
    Hudson	          1%
    Ionia	          1%
    Jackson	          1%
    Lansing	          1%
    Lapeer	          1%
    Muskegon	      1%
    Muskegon Heights  1%
    Pontiac	          1%
    Port Huron        1%
    Portland	      1%
    Saginaw           1.5%
    Springfield	      1%
    Walker	          1%
    
    '''
    #!longer list of counties
    elif state == 'Michigan':
        if stateDeductions == 0:
            # $4900 dependent deduction
            if maritalStatus == 'Married':
                stateDeductions = 10000 + (dependents * 5000)
            else:
                stateDeductions = 5000 + (dependents * 5000)
        agi -= stateDeductions
        stateBracket = .0425
        taxes = agi * stateBracket
        michiganCounties = {  
                            "Albion":	          .01,
                            "Battle Creek":	      .01,
                            "Benton Harbor":      .01,
                            "Big Rapids":	      .01,
                            "Detroit":            .024,
                            "East Lansing":	      .01,
                            "Flint":	          .01,
                            "Grand Rapids":       .015,
                            "Grayling":	          .01,
                            "Hamtramck":	      .01,
                            "Highland Park":      .02,
                            "Hudson":	          .01,
                            "Ionia":	          .01,
                            "Jackson":	          .01,
                            "Lansing":	          .01,
                            "Lapeer":	          .01,
                            "Muskegon":	          .01,
                            "Muskegon Heights":   .01,
                            "Pontiac":	          .01,
                            "Port Huron":         .01,
                            "Portland":	          .01,
                            "Saginaw":            .015,
                            "Springfield":	      .01,
                            "Walker":	          .01}
        localBracket = michiganCounties[county]
        taxes += agi * localBracket
        stateBracket += localBracket
    
    '''
    STATE INCOME TAXES
    https://www.revenue.state.mn.us/minnesota-income-tax-rates-and-brackets

    2023
    ​	        	 MARRIED FILING JOINTLY      	      MARRIED FILING SEPARATE​Ly
 	RATE    More Than​	     But not more than​	      More than​	    But not more than​
    5.35%	$0	            $43,950	                $0	             $21,975
    6.80%	$43,950	        $174,610	​            $21,975    	  $87,305
    7.85%	$174,610	    $304,970 ​	             $87,305	      $152,485
    9.85%	$304,970	 	                        $152,485	 
    

    ​	        HEAD OF HOUSEHOLD​	        	                SINGLE	
    RATE    More Than​	    But not more than​        More than​	But not more than​
    5.35%​	 $0	            $37,010	                 $0	          $30,070
    6.80%	$37,010	       $148,730	                $30,070	     $98,760
    7.85%	$148,730       $243,720	                $98,760	     $183,340
    9.85%	$243,720	                            $183,340
    
    DEPENDENT DEDUCTIONS AND CREDITS
    https://www.revenue.state.mn.us/child-and-dependent-care-credit

    https://www.revenue.state.mn.us/dependent-exemptions
    
    STANDARD DEDUCTION
    https://www.revenue.state.mn.us/minnesota-standard-deduction
    SINGLE OR MARRIED FILING SEPERATELY- $12,900
    MARRIED FILING JOINTLY OR QUALIFYING SURVIVING SPOUSE- $25,800
    HEAD OF HOUSEHOLD - $19,400
    '''
    elif state == 'Minnesota':
        if maritalStatus == 'Married':
            if stateDeductions == 0:
                stateDeductions = 25800 + (dependents * 4950)
            agi -= stateDeductions
            if agi > 304970:
                stateBracket = .0985
                margin = agi - 304970
                taxes += 21469.465 + margin * stateBracket
            elif agi > 174610:
                stateBracket = .0785
                margin = agi - 174610
                taxes += 11236.205 + margin * stateBracket
            elif agi > 43950:
                stateBracket = .068
                margin = agi - 43950
                taxes += 2351.325 + margin * stateBracket
            else:
                stateBracket = .0535
                taxes += agi * stateBracket
        elif maritalStatus == 'Head of Household':
            if stateDeductions == 0:
                stateDeductions = 19400 + (dependents * 4950)
            agi -= stateDeductions
            if agi > 243720:
                stateBracket = .0985
                margin = agi - 243720
                taxes += 17033.71 + margin * stateBracket
            elif agi > 148730:
                stateBracket = .0785
                margin = agi - 148730
                taxes += 5687.085 + margin * stateBracket
            elif agi > 9576.995:
                stateBracket = .068
                margin = agi - 37010
                taxes += 1980.035 + margin * stateBracket
            else:
                stateBracket = .0535
                taxes += agi * stateBracket
        elif maritalStatus == 'Single':
            if stateDeductions == 0:
                stateDeductions = 12900 + (dependents * 4950)
            agi -= stateDeductions
            if agi > 183340:
                stateBracket = .0985
                margin = agi - 183340
                taxes += 12919.195 + margin * stateBracket
            elif agi > 98760:
                stateBracket = .0785
                margin = agi - 98760
                taxes += 6279.665 + margin * stateBracket
            elif agi > 30070:
                stateBracket = .068
                margin = agi - 30070
                taxes += 1608.745 + margin * stateBracket
            else:
                stateBracket = .0535
                taxes += agi * stateBracket
        elif maritalStatus == 'Married Fililng Separately':
            if stateDeductions == 0:
                stateDeductions = 12900 + (dependents * 4950)
            agi -= stateDeductions
            if agi > 152485:
                stateBracket = .0985
                margin = agi - 152485
                taxes += 10734.7325 + margin * stateBracket
            elif agi > 87305:
                stateBracket = .0785
                margin = agi - 87305
                taxes += 5618.1025 + margin * stateBracket
            elif agi > 21975:
                stateBracket = .068
                margin = agi - 21975
                taxes += 1175.6625 + margin * stateBracket
            else:
                stateBracket = .0535
                taxes += agi * stateBracket
    
    '''
    STATE INCOME TAXES
    https://www.dor.ms.gov/individual/tax-rates

    0% on the first $5,000 of taxable income.​                                                                                                                                                                                                                                                                                                      
    4% on the next $5,000 of taxable income.                                                                                                                                                                                                                                                                                                                            
    5% on the remaining taxable income in excess of $10,000.

    EXEMPTIONS (SAME LINK)
    Married Filing Joint or Combined*​	 	$12,000	 
    Married Spouse Deceased	 	           $12,000	 
    Married Filing Separate     	       $6,000 
    Head of Family	 	                   $8,000
    Single	 	                           $6,000	 
    Dependent                       	   $1,500	 
    Taxpayer or Spouse over 65	 	       $1,500	 

    DEDUCTIONS (SAME LINK)
    Married Filing Joint or Combined    $ 4,600	 
    Married Spouse Deceased	 	        $ 4,60​0	 
    Married Filing Separate	 	        $ 2,300
    Head of Family	 	                $ 3,400	 
    Single	 	                        $ 2,300
    
    '''
    if state == 'Mississippi':
        if stateDeductions == 0:
            # COMBINED DEDUCTIONS AND EXEMPTIONS
            stateDeductions = (dependents * 1500)
            if maritalStatus == 'Married':
                stateDeductions = 16600
            elif maritalStatus == 'Head of Household':
                stateDeductions = 11400
            elif maritalStatus == 'Single' or 'Married Filing Separately':
                stateDeductions = 8300
        agi -= stateDeductions
        if agi > 10000:
            stateBracket = .05
            margin = agi - 10000
            taxes = 230 + margin * stateBracket
        elif agi > 5000:
            stateBracket = .04
            margin = agi - 5000
            taxes = margin * stateBracket

    '''
    STATE INCOME TAXES
    https://dor.mo.gov/taxation/individual/tax-types/income/year-changes/
    If the Missouri taxable income is   The tax is
    $0 to $111	                        $0
    At least $112 but not over $1,121	1.5% of the Missouri taxable income
    Over $1,121 but not over $2,242	    $17 plus 2.0% of excess over $1,121
    Over $2,242 but not over $3,363	    $39 plus 2.5% of excess over $2,242
    Over $3,363 but not over $4,484	    $67 plus 3.0% of excess over $3,363
    Over $4,484 but not over $5,605	    $101 plus 3.5% of excess over $4,484
    Over $5,605 but not over $6,726	    $140 plus 4.0% of excess over $5,605
    Over $6,726 but not over $7,847	    $185 plus 4.5% of excess over $6,726
    Over $7,847 but not over $8,968	    $235 plus 5.0% of excess over $7,847
    Over $8,968	                        $291 plus 5.3% of excess over $8,968

    STATE DEDUCTIONS ARE THE SAME AS FEDERAL (SAME LINK)    

    LOCAL INCOME TAXES
    https://www.kcmo.gov/city-hall/departments/finance/earnings-
    KCMO 1%
    
    https://www.stlouis-mo.gov/government/departments/collector/earnings-tax/individual-earnings-tax-info.cfm
    St. Louis 1%

    '''
    elif state == 'Missouri':
        if stateDeductions == 0:
            stateDeductions = federalDeductions
        agi -= stateDeductions
        if agi > 8968:
            stateBracket = .053
            margin = agi - 8584
            taxes = 291 + margin * stateBracket
        elif agi > 7847:
            stateBracket = .05
            margin = agi - 7847
            taxes = 235 + margin * stateBracket
        elif agi > 6726:
            stateBracket = .045
            margin = agi - 6726
            taxes = 185 + margin * stateBracket
        elif agi > 5605:
            stateBracket = .04
            margin = agi - 5605
            taxes = 140 + margin * stateBracket
        elif agi > 4484:
            stateBracket = .035
            margin = agi - 4484
            taxes = 101 + margin * stateBracket
        elif agi > 3363:
            stateBracket = .03
            margin = agi - 3363
            taxes = 67 + margin * stateBracket
        elif agi > 2242:
            stateBracket = .025
            margin = agi - 2242
            taxes = 39 + margin * stateBracket
        elif agi > 1121:
            stateBracket = .02
            margin = agi - 1121
            taxes = 17 + margin * stateBracket
        elif agi > 112:
            stateBracket = .015
            margin = agi - 112
            taxes = margin * stateBracket
        if county == 'Kansas City' or 'St. Louis':
            localBracket = .01
            taxes += agi * localBracket
            stateBracket += localBracket

    # !Federal deduction only applies if itemizing !margin with deductions *sigh*
    elif state == 'Montana':
        if stateDeductions == 0:
            if maritalStatus == 'Married':
                # Deduction is 20% of AGI with a $4260 minimum and a $9580 cap
                if agi > 47900:
                    stateDeductions = 9580
                elif agi > 21300:
                    stateDeductions = agi * .2
                else:
                    stateDeductions = 4260
            else:
                # Deduction is 20% of AGI with a $2130 minimum and a $4790 cap
                if agi > 23950:
                    stateDeductions = 4790
                elif agi > 10650:
                    stateDeductions = agi * .2
                else:
                    stateDeductions = 2130
            stateDeductions += (dependents * 2560)
        agi -= stateDeductions
        if agi > 18700:
            stateBracket = .069
            margin = agi - 18700
            taxes += 634 + margin * stateBracket
        elif agi > 14500:
            stateBracket = .06
            margin = agi - 14500
            taxes += 442 + margin * stateBracket
        elif agi > 11300:
            stateBracket = .05
            margin = agi - 11300
            taxes += 282 + margin * stateBracket
        elif agi > 8400:
            stateBracket = .04
            margin = agi - 8400
            taxes += 166 + margin * stateBracket
        elif agi > 5500:
            stateBracket = .03
            margin = agi - 5500
            taxes += 79 + margin * stateBracket
        elif agi > 3100:
            stateBracket = .02
            margin = agi - 3100
            taxes += 31 + margin * stateBracket
        else:
            stateBracket = .01
            taxes += agi * stateBracket
    elif state == 'Nebraska':
        # $142 child credit
        if maritalStatus == 'Married':
            # $284 credit for married couples
            taxes = -(284 + (dependents * 142))
            if stateDeductions == 0:
                stateDeductions = 14200
            agi -= stateDeductions
            if agi > 64430:
                stateBracket = .0684
                margin = agi - 64430
                taxes += 2558.163 + margin * stateBracket
            elif agi > 39990:
                stateBracket = .0501
                margin = agi - 39990
                taxes += 1333.719 + margin * stateBracket
            elif agi > 6660:
                stateBracket = .0351
                margin = agi - 6660
                taxes += 163.836 + margin * stateBracket
            else:
                stateBracket = .0246
                taxes += agi * stateBracket
        else:
            # $142 credit for individuals
            taxes -= (142 + (dependents * 142))
            if stateDeductions == 0:
                stateDeductions = 7100
            agi -= stateDeductions
            if agi > 32210:
                stateBracket = .0684
                margin = agi - 32210
                taxes += 1278.8 + margin * stateBracket
            elif agi > 19990:
                stateBracket = .0501
                margin = agi - 19990
                taxes += 666.58 + margin * stateBracket
            elif agi > 3340:
                stateBracket = .0351
                margin = agi - 3340
                taxes += 82.164 + margin * stateBracket
            else:
                stateBracket = .0246
                taxes += agi * stateBracket
    # !Only interest and dividend income
    # elif state == 'New Hampshire':
    #     # ! $1000-1500 dependent deduction
    #     if maritalStatus == 'Married':
    #         if stateDeductions == 0:
    #             stateDeductions = 4800
    #         agi -= stateDeductions
    #     else:
    #         if stateDeductions == 0:
    #             stateDeductions = 2400
    #         agi -= stateDeductions
    #     stateBracket = .05
    #     taxes = agi * stateBracket
    #

    '''
    STATE INCOME TAXES
    https://www.state.nj.us/treasury/taxation/taxtables.shtml

    SINGLE OR MARRIED FILING SEPARATELY
    If Taxable Income is:
    Over       But not over        Tax is
    $0         $20,000             1.4%  
    $20,000    $35,000             1.75% - $70
    $35,000    $40,000             3.5% - $682.50
    $40,000    $75,000             5.525% - $1,492.50
    $75,000    $500,000            6.37% - $2,126.25
    $500,000   $1,000,000          8.97% - $15,126.25
    $1,000,000                     10.75% - $32,926.25
       
    Married/CU filing joint, Head of household, OR Qualifying widow(er)/surviving CU partner STEP
    SINGLE OR MARRIED FILING SEPARATELY
    If Taxable Income is:
    Over       But not over        Tax is
    $0         $20,000             1.4%  
    $20,000    $50,000             1.75% - $70
    $50,000    $70,000             2.45% - $420
    $70,000    $80,000             3.5% - $1,154.5
    $80,000    $150,000            5.525% - $2,775
    $150,000   $500,000            6.37% - $4,042.5
    $500,000   $1,000,000          8.97% - $17,042.5
    $1,000,000                     10.75% - $34,842.5

    DEDUCTIONS AND EXEMPTIONS
    https://www.state.nj.us/treasury/taxation/njit13.shtml

    Regular Exemptions
    You can claim a $1,000 exemption for yourself and your spouse/CU partner (if filing a joint return) or your Domestic Partner.
    
    Senior 65+ Exemptions
    You can claim a $1,000 exemption if you were 65 or older on the last day of the tax year. If you are filing jointly, your spouse can take a $1,000 exemption if they were 65 or older on the last day of the tax year. You cannot claim this exemption for your domestic partner or dependents.

    Dependent Exemptions
    You can claim a $1,500 exemption for each child or dependent who qualifies as your dependent for federal tax purposes.


    '''
    elif state == 'New Jersey':
        # $1500 dependent tax credit
        if maritalStatus == ('Single' or "Married Filing Separately"):
            if stateDeductions == 0:
                stateDeductions = 1000 + (dependents * 1500)
            agi -= stateDeductions
            if agi > 1000000:
                stateBracket = .01075
                margin = agi - 1000000
                taxes += margin * stateBracket - 34842.5
            elif agi > 500000:
                stateBracket = .0897
                margin = agi - 500000
                taxes += margin * stateBracket - 17042.5
            elif agi > 150000:
                stateBracket = .0637
                margin = agi - 150000
                taxes += margin * stateBracket - 4042.5
            elif agi > 80000:
                stateBracket = .05525
                margin = agi - 80000
                taxes += margin * stateBracket - 2775
            elif agi > 70000:
                stateBracket = .035
                margin = agi - 70000
                taxes += margin * stateBracket - 1154.5
            elif agi > 50000:
                stateBracket = .0245
                margin = agi - 50000
                taxes += margin * stateBracket - 420
            elif agi > 20000:
                stateBracket = .0175
                margin = agi - 20000
                taxes += margin * stateBracket - 70
            else:
                stateBracket = .014
                taxes += agi * stateBracket
        # MARRIED OR HEAD OF HOUSEHOLD
        else:
            if stateDeductions == 0:
                stateDeductions = 2000 + (dependents * 1500)
            agi -= stateDeductions
            if agi > 1000000:
                stateBracket = .01075
                margin = agi - 1000000
                taxes += margin * stateBracket - 32926.25
            elif agi > 500000:
                stateBracket = .0897
                margin = agi - 500000
                taxes += margin * stateBracket - 15126.25
            elif agi > 75000:
                stateBracket = .0637
                margin = agi - 75000
                taxes += margin * stateBracket - 2126.25
            elif agi > 40000:
                stateBracket = .05525
                margin = agi - 40000
                taxes += margin * stateBracket - 1492.5
            elif agi > 35000:
                stateBracket = .035
                margin = agi - 35000
                taxes += margin * stateBracket - 682.5
            elif agi > 20000:
                stateBracket = .0175
                margin = agi - 20000
                taxes += margin * stateBracket - 70
            else:
                stateBracket = .014
                taxes += agi * stateBracket
    '''
    STATE INCOME TAXES
    https://klvg4oyd4j.execute-api.us-west-2.amazonaws.com/prod/PublicFiles/34821a9573ca43e7b06dfad20f5183fd/fdf3c548-8aba-4b9c-9eb4-bb564c716015/FYI-104.pdf

    SINGLE
    If the amount                                                             
    Is over      but not over     Tax is                                   
    $6,925       $12,425          1.7% of income over $6,925
    $12,425      $17,925          $93.5 + 3.2% of ncome over $12,425
    $17,925      $22,925          $269.5 + 4.7% of income over $17,925
    $22,925      $216,925         $504.5 +  4.9% if income over $22,925
    $216,925                      $10,010.5 + 5.9% of income over 216,925

    MARRIED OR HEAD OF HOUSEHOLD
    If the amount                                                             
    Is over      but not over     Tax is                                   
    $13,850      $21,850          1.7% of ncome over $13,850
    $21,850      $29,850          $136 + 3.2% of income over $21,850
    $29,850      $37,850          $392 + 4.7% of income over $29,850
    $37,850      $328,850         $768 + 4.9% if income over $37,850
    $328,850                      $15,027 + 5.9% of income over 216,925

    CREDITS
    https://www.tax.newmexico.gov/individuals/file-your-taxes-overview/credits-rebates/

    
    '''
    elif state == 'New Mexico':
        # $4000 dependent credit for at most one dependent
        if stateDeductions == 0 and dependents:
            stateDeductions += 4000
        if maritalStatus == 'Married':
            agi -= stateDeductions - federalDeductions
            if agi > 328850:
                stateBracket = .059
                margin = agi - 315000
                taxes = 15027 + margin * stateBracket
            elif agi > 37850:
                stateBracket = .049
                margin = agi - 37850
                taxes = 768 + margin * stateBracket
            elif agi > 29850:
                stateBracket = .047
                margin = agi - 29850
                taxes = 392 + margin * stateBracket
            elif agi > 21850:
                stateBracket = .032
                margin = agi - 21850
                taxes = 136 + margin * stateBracket
            elif agi > 13850:
                stateBracket = .017
                taxes = agi * stateBracket
        else:
            agi -= stateDeductions - federalDeductions
            if agi > 216925:
                stateBracket = .059
                margin = agi - 216925
                taxes = 10010.5 + margin * stateBracket
            elif agi > 22925:
                stateBracket = .049
                margin = agi - 22925
                taxes = 504.5 + margin * stateBracket
            elif agi > 17925:
                stateBracket = .047
                margin = agi - 17925
                taxes = 269.5 + margin * stateBracket
            elif agi > 12425:
                stateBracket = .032
                margin = agi - 12425
                taxes = 93.5 + margin * stateBracket
            elif agi > 6925:
                stateBracket = .017
                taxes = agi * stateBracket
    # !Tax benefit recapture  
    # !ignoring MTA and NY-NJ waterfront
    '''
    STATE INCOME TAXES
    https://www.tax.ny.gov/forms/html-instructions/2022/it/it201i-2022.htm#nys-tax-rate-schedule

    Married filing jointly or qualifying surviving spouse
    over	    but not over            The tax is 
    $0	        $17,150			        4%
    $17,150	    $23,600	                $686       plus 4.5%  of the excess over $17,150
    $23,600	    $27,900	                $976       plus 5.25% of the excess over $23,600
    $27,900	    $161,550	            $1,202     plus 5.85% of the excess over $27,900
    $161,550	$323,200	            $9,021	   plus 6.25% of the excess over $161,550
    $323,200	$2,155,350	            $19,124	   plus 6.85% of the excess over $323,200
    $2,155,350	$5,000,000	            $144,626   plus 9.65% of the excess over $2,155,350
    $5,000,000	$425,000,000	        $419,135   plus 10.3% of the excess over $5,000,000
    $25,000,000		                    $2,479,135 plus 10.9% of the excess over $25,000,000

    Single or married filing separately
    over	    but not over            The tax is:
    $0	        $8,500			        4%
    $8,500	    $11,700	                $340	   plus	4.5%  of the excess over $8,500
    $11,700	    $13,900	                $484	   plus	5.25% of the excess over $11,700
    $13,900	    $80,650	                $600	   plus	5.85% of the excess over $13,900
    $80,650	    $215,400	            $4,504	   plus	6.25% of the excess over $80,650
    $215,400	$1,077,550	            $12,926	   plus	6.85% of the excess over $215, 400
    $1,077,550	$5,000,000	            $71,984	   plus	9.65% of the excess over $1,077,550
    $5,000,000	$25,000,000	            $450,500   plus	10.3% of the excess over $5,000,000
    $25,000,000	            	        $2,510,500 plus	10.9% of the excess over $25,000,000

    Head of household
    over	    but not over            The tax is:
    $0	        $12,800			        4%
    $12,800	    $17,650	                $512	   plus	4.5%  of the excess over $12,800
    $17,650	    $20,900	                $730       plus	5.25% of the excess over $17,650
    $20,900	    $107,650	            $901	   plus	5.85% of the excess over $20,900
    $107,650	$269,300                $5,976	   plus	6.25% of the excess over $107,650
    $269,300	$1,616,450	            $16,079	   plus	6.85% of the excess over $269,300
    $1,616,450	$5,000,000	            $108,359   plus	9.65% of the excess over $1,616,450
    $5,000,000	$25,000,000	            $434,871   plus	10.3% of the excess over $5,000,000
    $25,000,000		                    $2,494,871 plus	10.9% of the excess over $25,000,000
    
    STANDARD DEDUCTION - (SAME LINK)
    Single and dependent	                    $3,100
    Single and independent	                    $8,000
    Married filing joint return	                $16,050
    Married filing separate return	            $8,000
    Head of household (with qualifying person)	$11,200
    Qualifying surviving spouse 	            $16,050

    DEPENDENT EXEMPTION - $1,000 PER DEPENDENT (SAME LINK)

    LOCAL INCOME TAXES
    YONKERS (SAME LINK)
    16.75% OF STATE INCOME TAX

    NEW YORK CITY
    https://www.tax.ny.gov/forms/html-instructions/2022/it/it201i-2022.htm#nyc-tax-rate-schedule
    
    Married filing jointly and qualifying surviving spouse
    over	    but not over    the tax is
    $0	        $21,600			3.078%
    $21,600	    $45,000	        $665 + 3.762% of the excess over $21,600
    $45,000	    $90,000	        $1,545 + 3.819%	of the excess over $45,000
    $90,000	                    $3,264 + 3.876%	of the excess over $90,000
    
    Single and married filing separately
    over	    but not over    the tax is
    $0	        $12,000			3.078%
    $12,000	    25,000	        $369 + 3.762% of the excess over $12,000
    $25,000	    $50,000	        $858 + 3.819% of the excess over $25,000
    $50,000		                $1,813 + 3.876%	of the excess over $50,000
    
    Head of household
    over	    but not over    the tax is:
    $0	        $14,400			3.078%	of line 47	
    $14,400  	$30,000	        $443 + 3.762% of the excess over $14,400
    $30,000	    $60,000	        $1,030 + 3.819%	of the excess over $30,000
    $60,000	                    $2,176 + 3.876%	of the excess over $60,000

    '''

    elif state == 'New York':
        # $1000 dependent deduction
        if maritalStatus == 'Married':
            if stateDeductions == 0:
                stateDeductions = 16050 + (dependents * 1000)
            agi -= stateDeductions
            if agi > 250000000:
                stateBracket = .109
                margin = agi - 250000000
                taxes += 2479135 + margin * stateBracket
            elif agi > 50000000:
                stateBracket = .103
                margin = agi - 50000000
                taxes += 419135 + margin * stateBracket
            elif agi > 2155350:
                stateBracket = .0965
                margin = agi - 2155350
                taxes += 144626 + margin * stateBracket
            elif agi > 323200:
                stateBracket = .0685
                margin = agi - 323200
                taxes += 19124 + margin * stateBracket
            elif agi > 161550:
                stateBracket = .0625
                margin = agi - 161550
                taxes += 9021 + margin * stateBracket
            elif agi > 27900:
                stateBracket = .0585
                margin = agi - 27900
                taxes += 1202 + margin * stateBracket
            elif agi > 23600:
                stateBracket = .0525
                margin = agi - 23600
                taxes += 976 + margin * stateBracket
            elif agi > 17150:
                stateBracket = .045
                margin = agi - 17150
                taxes += 686 + agi * stateBracket
            else:
                stateBracket = .04
                taxes += agi * stateBracket
        elif maritalStatus == 'Single':
            if stateDeductions == 0:
                stateDeductions = 8000 + (dependents * 1000)
            agi -= stateDeductions
            if agi > 250000000:
                stateBracket = .109
                margin = agi - 250000000
                taxes += 2510500 + margin * stateBracket
            elif agi > 50000000:
                stateBracket = .103
                margin = agi - 50000000
                taxes += 450500 + margin * stateBracket
            elif agi > 1077550:
                stateBracket = .0965
                margin = agi - 1077550
                taxes += 71984 + margin * stateBracket
            elif agi > 215400:
                stateBracket = .0685
                margin = agi - 215400
                taxes += 12926 + margin * stateBracket
            elif agi > 80650:
                stateBracket = .0625
                margin = agi - 80650
                taxes += 4504 + margin * stateBracket
            elif agi > 13900:
                stateBracket = .0585
                margin = agi - 13900
                taxes += 600 + margin * stateBracket
            elif agi > 11700:
                stateBracket = .0525
                margin = agi - 11700
                taxes += 484 + margin * stateBracket
            elif agi > 8500:
                stateBracket = .045
                margin = agi - 8500
                taxes += 340 + agi * stateBracket
            else:
                stateBracket = .04
                taxes += agi * stateBracket
        elif maritalStatus == 'Head of Household':
            if agi > 250000000:
                stateBracket = .109
                margin = agi - 250000000
                taxes += 2510500 + margin * stateBracket
            elif agi > 50000000:
                stateBracket = .103
                margin = agi - 50000000
                taxes += 450500 + margin * stateBracket
            elif agi > 1616450:
                stateBracket = .0965
                margin = agi - 1616450
                taxes += 71984 + margin * stateBracket
            elif agi > 269300:
                stateBracket = .0685
                margin = agi - 269300
                taxes += 12926 + margin * stateBracket
            elif agi > 107650:
                stateBracket = .0625
                margin = agi - 107650
                taxes += 4504 + margin * stateBracket
            elif agi > 20900:
                stateBracket = .0585
                margin = agi - 20900
                taxes += 600 + margin * stateBracket
            elif agi > 17650:
                stateBracket = .0525
                margin = agi - 17650
                taxes += 484 + margin * stateBracket
            elif agi > 12800:
                stateBracket = .045
                margin = agi - 12800
                taxes += 340 + agi * stateBracket
            else:
                stateBracket = .04
                taxes += agi * stateBracket
        # Yonkers 16.75% tax as a percentage of state income taxes
        if county == 'Yonkers':
            taxes *= 1.1675
        # Special rules for New York City
        elif county == 'New York City':
            if maritalStatus == 'Married':
                if agi > 90000:
                    localBracket = .03876
                    localMargin = agi - 90000
                    taxes += 3264 + localMargin * localBracket
                elif agi > 45000:
                    localBracket = .03819
                    localMargin = agi - 45000
                    taxes += 1545 + localMargin * localBracket
                elif agi > 21600:
                    localBracket = .03762
                    localMargin = agi - 21600
                    taxes += 665 + localMargin * localBracket
                else:
                    localBracket = .03078
                    taxes += agi * localBracket
            elif maritalStatus == 'Head of Household':
                if agi > 60000:
                    localBracket = .03876
                    localMargin = agi - 60000
                    taxes += 2176 + localMargin * localBracket
                elif agi > 30000:
                    localBracket = .03819
                    localMargin = agi - 30000
                    taxes += 1030 + localMargin * localBracket
                elif agi > 14400:
                    localBracket = .03762
                    localMargin = agi - 14400
                    taxes += 443 + localMargin * localBracket
                else:
                    localBracket = .03078
                    taxes += agi * localBracket
            # Single or married filing seperately in this case
            else:
                if agi > 50000:
                    localBracket = .03876
                    localMargin = agi - 50000
                    taxes += 1813 + localMargin * localBracket
                elif agi > 25000:
                    localBracket = .03819
                    localMargin = agi - 25000
                    taxes += 858 + localMargin * localBracket
                elif agi > 12000:
                    localBracket = .03762
                    localMargin = agi - 12000
                    taxes += 369 + localMargin * localBracket
                else:
                    localBracket = .03078
                    taxes += agi * localBracket
        # Special rules for New York City
        elif county == 'NY-NJ Waterfront':
            taxes += agi * .02
            # Combines the salt brackets so both are accounted for when doing optimization
            stateBracket += localBracket
            # Sets the margin to the local margin if it is lower so that the taxes are recalculated
            if localMargin < margin:
                margin = localMargin
    '''
    STATE INCOME TAXES
    https://www.ncdor.gov/taxes-forms/tax-rate-schedules

    2022 -> 4.99%
    2023 -> 4.75%
    2024 -> 4.6%
    2025 -> 4.5%
    2026 -> 4.25%
    2027 -> 4% (TYPO ON WEBSITE??)

    STATE DEDUCTIONS
    https://www.ncdor.gov/taxes-forms/individual-income-tax/north-carolina-standard-deduction-or-north-carolina-itemized-deductions
    f your filing status is:	                                    Your standard deduction is:
    Single	                                                        $12,750
    Married Filing Jointly/Qualifying Widow(er)/Surviving Spouse	$25,500
    Married Filing Separately	 
        Spouse does not claim itemized deductions                   $12,750
        Spouse claims itemized deductions                           $0
    Head of Household	                                            $19,125
    '''
    elif state == 'North Carolina':
        if stateDeductions == 0:
            if maritalStatus == 'Married':
                stateDeductions = 25500
            else:
                stateDeductions = 10750
        agi -= stateDeductions
        stateBracket = .0499
        taxes = agi * stateBracket
    '''
    STATE INCOME TAXES
    https://www.tax.nd.gov/forms

    https://www.tax.nd.gov/sites/www/files/documents/forms/2022-individual-income-tax-booklet.pdf
    Single
    If North Dakota Taxable Income Is:
    Over        But Not Over    Your Tax Is: 
    $ 0         $41,775         1.10% of North Dakota Taxable Income   
    $41,775     $101,050        $459.53 + 2.04% of amount over $ 41,775
    $101,050    $210,825        $1,668.74 + 2.27% of amount over $101,050
    $210,825    $458,350        $4,160.63 + 2.64% of amount over $210,825
    $458,350                    $10,695.29 + 2.90% of amount over $458,350

    TAX CREDITS
    https://www.tax.nd.gov/tax-exemptions-credits/income-tax-exemptions-credits
    '''
    # !Federal deductions and exemptions, add federal deductions including dependents as a parameter for this case?
    elif state == 'North Dakota':
        if maritalStatus == 'Married':
            if stateDeductions == 0:
                stateDeductions = 25100
            agi -= stateDeductions
            if agi > 440600:
                stateBracket = .029
                margin = agi - 440600
                taxes = 9716.225 + margin * stateBracket
            elif agi > 246700:
                stateBracket = .0264
                margin = agi - 246700
                taxes = 4597.335 + margin * stateBracket
            elif agi > 161950:
                stateBracket = .0227
                margin = agi - 161950
                taxes = 2673.51 + margin * stateBracket
            elif agi > 67050:
                stateBracket = .0204
                margin = agi - 67050
                taxes = 737.55 + margin * stateBracket
            else:
                stateBracket = .011
                taxes = agi * stateBracket
        else:
            if stateDeductions == 0:
                stateDeductions = 12550
            agi -= stateDeductions
            if agi > 440600:
                stateBracket = .029
                margin = agi - 440600
                taxes = 10281.415 + margin * stateBracket
            elif agi > 202650:
                stateBracket = .0264
                margin = agi - 202650
                taxes = 3999.535 + margin * stateBracket
            elif agi > 97150:
                stateBracket = .0227
                margin = agi - 97150
                taxes = 1604.685 + margin * stateBracket
            elif agi > 40125:
                stateBracket = .0204
                margin = agi - 40125
                taxes = 441.375 + margin * stateBracket
            else:
                stateBracket = .011
                taxes = agi * stateBracket
    # !Special margin 
    '''
    STATE INCOME TAX RATES
    https://tax.ohio.gov/individual/resources/annual-tax-rates
    For taxable years beginning in 2022:
        Ohio Taxable Income	  Tax Calculation
        0 - $26,050           0.000%
        $26,051 - $46,100     $360.69 + 2.765% of excess over $26,050
        $46,100- $92,150      $915.07 + 3.226% of excess over $46,100
        $92,150 - $115,300    $2,400.64 + 3.688% of excess over $92,150
        more than $115,300    $3,254.41+ 3.990% of excess over $115,300
    
    LOCAL INCOME TAX RATES
    https://www.ritaohio.com/TaxRatesTable
    '''
    elif state == 'Ohio':
        if stateDeductions == 0:
            if maritalStatus == 'Married':
                if agi < 40000:
                    stateDeductions = 4800
                elif agi < 80000:
                    stateDeductions = 4300
                else:
                    stateDeductions = 3800
            else:
                if agi < 40000:
                    stateDeductions = 2400
                elif agi < 80000:
                    stateDeductions = 2150
                else:
                    stateDeductions = 1900
            stateDeductions += (dependents * 2400)
        agi -= stateDeductions
        if agi > 221300:
            stateBracket = .04797
            margin = agi - 221300
            taxes = 7826.9705 + margin * stateBracket
        elif agi > 110650:
            stateBracket = .04413
            margin = agi - 110650
            taxes = 2493.986 + margin * stateBracket
        elif agi > 88450:
            stateBracket = .03802
            margin = agi - 88450
            taxes = 2099.942 + margin * stateBracket
        elif agi > 44250:
            stateBracket = .03326
            margin = agi - 44250
            taxes = 629.85 + margin * stateBracket
        elif agi > 22150:
            stateBracket = .0285
            margin = agi - 22150
            taxes = margin * stateBracket
         ohioCounties = {'Aberdeen': 0.0100,
                    'Ada': 0.0165,
                    'Addyston': 0.0150,
                    'Adelphi': 0.0100,
                    'Akron': 0.0250,
                    'Alger': 0.0100,
                    'Alliance': 0.0200,
                    'Alvordton': 0.0100,
                    'Amanda': 0.0100,
                    'Amberley': 0.0200,
                    'Amelia': 0.0100,
                    'Amherst': 0.0150,
                    'Amsterdam': 0.0100,
                    'Andover': 0.0150,
                    'Anna': 0.0175,
                    'Ansonia': 0.0100,
                    'Antwerp': 0.0100,
                    'Apple Creek': 0.0100,
                    'Arcanum': 0.0100,
                    'Archbold': 0.0150,
                    'Arlington': 0.0100,
                    'Arlington Heights': 0.0210,
                    'Ashland': 0.0200,
                    'Ashley': 0.0100,
                    'Ashtabula': 0.0180,
                    'Ashville': 0.0100,
                    'Athens': 0.0185,
                    'Aurora': 0.0200,
                    'Avon': 0.0175,
                    'Avon Lake': 0.0150,
                    'Baltic': 0.0150,
                    'Baltimore': 0.0100,
                    'Barberton': 0.0225,
                    'Barnesville': 0.0100,
                    'Batavia': 0.0100,
                    'Bay Village': 0.0150,
                    'Beach City': 0.0100,
                    'Beachwood': 0.0200,
                    'Beaverdam': 0.0100,
                    'Bedford': 0.0300,
                    'Bedford Heights': 0.0200,
                    'Bellaire': 0.0100,
                    'Belle Center': 0.0100,
                    'Bellefontaine': 0.0133,
                    'Bellevue': 0.0200,
                    'Bellville': 0.0100,
                    'Belpre': 0.0100,
                    'Bentleyville': 0.0100,
                    'Berea': 0.0200,
                    'Bethel': 0.0050,
                    'Bettsville': 0.0100,
                    'Beverly': 0.0100,
                    'Bexley': 0.0250,
                    'Bloomdale': 0.0100,
                    'Bloomingdale': 0.0100,
                    'Bloomville': 0.0100,
                    'Blue Ash': 0.0125,
                    'Bluffton': 0.0125,
                    'Bolivar': 0.0100,
                    'Boston Heights': 0.0200,
                    'Botkins': 0.0150,
                    'Bowerston': 0.0100,
                    'Bowling Green': 0.0200,
                    'Bradford': 0.0100,
                    'Bradner': 0.0100,
                    'Brady Lake': 0.0100,
                    'Bratenahl': 0.0150,
                    'Brecksville': 0.0200,
                    'Bremen': 0.0100,
                    'Brewster': 0.0150,
                    'Brice': 0.0200,
                    'Broadview Heights': 0.0200,
                    'Brooklyn': 0.0250,
                    'Brooklyn Heights': 0.0250,
                    'Brook Park': 0.0200,
                    'Brookville': 0.0200,
                    'Brunswick': 0.0200,
                    'Bryan': 0.0180,
                    'Buckland': 0.0100,
                    'Bucyrus': 0.0200,
                    'Burton': 0.0100,
                    'Butler': 0.0100,
                    'Byesville': 0.0100,
                    'Cadiz': 0.0100,
                    'Cairo': 0.0050,
                    'Caldwell': 0.0100,
                    'Cambridge': 0.0200,
                    'Camden': 0.0100,
                    'Campbell': 0.0250,
                    'Canal Fulton': 0.0150,
                    'Canal Winchester': 0.0200,
                    'Canfield': 0.0100,
                    'Canton': 0.0250,
                    'Cardington': 0.0100,
                    'Carey': 0.0150,
                    'Carlisle': 0.0150,
                    'Carroll': 0.0075,
                    'Carrollton': 0.0100,
                    'Catawba': 0.0100,
                    'Cecil': 0.0100,
                    'Cedarville': 0.0125,
                    'Celina': 0.0150,
                    'Centerburg': 0.0100,
                    'Centerville': 0.0225,
                    'Chagrin Falls': 0.0185,
                    'Chardon': 0.0200,
                    'Chesterville': 0.0100,
                    'Cheviot': 0.0200,
                    'Chillicothe': 0.0200,
                    'Cincinnati': 0.0210,
                    'Circleville': 0.0200,
                    'Clarksville': 0.0100,
                    'Clay Center': 0.0150,
                    'Clayton': 0.0150,
                    'Cleveland': 0.0250,
                    'Cleveland Heights': 0.0225,
                    'Clinton': 0.0100,
                    'Clyde': 0.0150,
                    'Coal Grove': 0.0100,
                    'Coldwater': 0.0100,
                    'Columbiana': 0.0100,
                    'Columbus': 0.0250,
                    'Columbus Grove': 0.0125,
                    'Commercial Point': 0.0075,
                    'Conesville': 0.0050,
                    'Conneaut': 0.0165,
                    'Continental': 0.0100,
                    'Convoy': 0.0100,
                    'Corwin': 0.0050,
                    'Coshocton': 0.0200,
                    'Covington': 0.0150,
                    'Crestline': 0.0200,
                    'Creston': 0.0100,
                    'Cridersville': 0.0100,
                    'Crooksville': 0.0150,
                    'Cuyahoga Falls': 0.0200,
                    'Cuyahoga Heights': 0.0250,
                    'Cygnet': 0.0100,
                    'Dalton': 0.0100,
                    'Danville': 0.0150,
                    'Darbyville': 0.0100,
                    'Dayton': 0.0250,
                    'Deer Park': 0.0150,
                    'Defiance': 0.0180,
                    'De Graff': 0.0100,
                    'Delaware': 0.0185,
                    'Delphos': 0.0175,
                    'Delta': 0.0150,
                    'Dennison': 0.0200,
                    'Deshler': 0.0100,
                    'Dover': 0.0150,
                    'Doylestown': 0.0200,
                    'Dresden': 0.0100,
                    'Dublin': 0.0200,
                    'Dunkirk': 0.0100,
                    'East Canton': 0.0150,
                    'East Cleveland': 0.0200,
                    'Eastlake': 0.0200,
                    'East Liverpool': 0.0150,
                    'East Palestine': 0.0100,
                    'Eaton': 0.0150,
                    'Edgerton': 0.0175,
                    'Edison': 0.0050,
                    'Edon': 0.0150,
                    'Elida': 0.0075,
                    'Elmore': 0.0175,
                    'Elmwood Place': 0.0200,
                    'Elyria': 0.0225,
                    'Empire': 0.0100,
                    'Englewood': 0.0175,
                    'Euclid': 0.0285,
                    'Evendale': 0.0120,
                    'Fairborn': 0.0150,
                    'Fairfax': 0.0175,
                    'Fairfield': 0.0150,
                    'Fairlawn': 0.0200,
                    'Fairport Harbor': 0.0200,
                    'Fairview Park': 0.0200,
                    'Farmersville': 0.0100,
                    'Fayette': 0.0150,
                    'Felicity': 0.0100,
                    'Findlay': 0.0100,
                    'Forest': 0.0125,
                    'Forest Park': 0.0150,
                    'Fort Jennings': 0.0100,
                    'Fort Loramie': 0.0150,
                    'Fort Recovery': 0.0100,
                    'Fostoria': 0.0200,
                    'Franklin': 0.0200,
                    'Frazeysburg': 0.0100,
                    'Fredericksburg': 0.0100,
                    'Fredericktown': 0.0100,
                    'Fremont': 0.0150,
                    'Gahanna': 0.0250,
                    'Galena': 0.0100,
                    'Galion': 0.0200,
                    'Gallipolis': 0.0100,
                    'Gambier': 0.0150,
                    'Garfield Heights': 0.0200,
                    'Garrettsville': 0.0175,
                    'Gates Mills': 0.0100,
                    'Geneva': 0.0150,
                    'Geneva-On-The-Lake': 0.0150,
                    'Genoa': 0.0150,
                    'Georgetown': 0.0100,
                    'Germantown': 0.0150,
                    'Gettysburg': 0.0100,
                    'Gibsonburg': 0.0100,
                    'Girard': 0.0200,
                    'Glandorf': 0.0150,
                    'Glenwillow': 0.0200,
                    'Gnadenhutten': 0.0150,
                    'Golf Manor': 0.0170,
                    'Grafton': 0.0150,
                    'Grand Rapids': 0.0100,
                    'Grand River': 0.0200,
                    'Grandview Heights': 0.0250,
                    'Granville': 0.0150,
                    'Gratis': 0.0100,
                    'Green': 0.0200,
                    'Greenfield': 0.0163,
                    'Greenhills': 0.0150,
                    'Green Springs': 0.0100,
                    'Greenville': 0.0150,
                    'Greenwich': 0.0100,
                    'Grove City': 0.0200,
                    'Groveport': 0.0200,
                    'Hamilton': 0.0200,
                    'Hamler': 0.0100,
                    'Hanover': 0.0100,
                    'Harrisburg': 0.0100,
                    'Harrison': 0.0100,
                    'Harrod': 0.0100,
                    'Hartville': 0.0100,
                    'Haskins': 0.0100,
                    'Heath': 0.0200,
                    'Hebron': 0.0150,
                    'Hicksville': 0.0100,
                    'Highland Heights': 0.0200,
                    'Highland Hills': 0.0250,
                    'Hilliard': 0.0200,
                    'Hillsboro': 0.0150,
                    'Hiram': 0.0225,
                    'Holgate': 0.0100,
                    'Holland': 0.0225,
                    'Hopedale': 0.0100,
                    'Hubbard': 0.0150,
                    'Huber Heights': 0.0225,
                    'Hudson': 0.0200,
                    'Huntsville': 0.0100,
                    'Huron': 0.0100,
                    'Independence': 0.0200,
                    'Ironton': 0.0100,
                    'Jackson': 0.0100,
                    'Jackson Center': 0.0150,
                    'Jamestown': 0.0050,
                    'Jefferson': 0.0150,
                    'Jeffersonville': 0.0100,
                    'Jerry City': 0.0100,
                    'Jewett': 0.0100,
                    'Johnstown': 0.0100,
                    'Kalida': 0.0100,
                    'Kent': 0.0225,
                    'Kenton': 0.0150,
                    'Kettering': 0.0225,
                    'Killbuck': 0.0100,
                    'Kirby': 0.0100,
                    'Kirkersville': 0.0100,
                    'Kirtland': 0.0200,
                    'Lagrange': 0.0150,
                    'Lakeline': 0.0100,
                    'Lakemore': 0.0225,
                    'Lakeview': 0.0150,
                    'Lakewood': 0.0150,
                    'Lancaster': 0.0175,
                    'Lebanon': 0.0100,
                    'Leesburg': 0.0100,
                    'Leetonia': 0.0150,
                    'Leipsic': 0.0150,
                    'Lewisburg': 0.0175,
                    'Lexington': 0.0100,
                    'Liberty Center': 0.0100,
                    'Lima': 0.0150,
                    'Lincoln Heights': 0.0200,
                    'Linndale': 0.0200,
                    'Lisbon': 0.0150,
                    'Lithopolis': 0.0150,
                    'Lockbourne': 0.0100,
                    'Lockland': 0.0210,
                    'Lodi': 0.0100,
                    'Logan': 0.0200,
                    'London': 0.0150,
                    'Lorain': 0.0250,
                    'Lordstown': 0.0100,
                    'Loudonville': 0.0175,
                    'Louisville': 0.0200,
                    'Loveland': 0.0100,
                    'Lowellville': 0.0200,
                    'Luckey': 0.0100,
                    'Lyndhurst': 0.0200,
                    'Lyons': 0.0100,
                    'Mcclure': 0.0100,
                    'Mccomb': 0.0100,
                    'Mcconnelsville': 0.0100,
                    'Mcdonald': 0.0200,
                    'Macedonia': 0.0250,
                    'Mcguffey': 0.0100,
                    'Madeira': 0.0100,
                    'Madison': 0.0100,
                    'Maineville': 0.0100,
                    'Malinta': 0.0100,
                    'Malta': 0.0100,
                    'Malvern': 0.0100,
                    'Manchester': 0.0100,
                    'Mansfield': 0.0200,
                    'Mantua': 0.0150,
                    'Maple Heights': 0.0250,
                    'Marble Cliff': 0.0200,
                    'Marengo': 0.0100,
                    'Mariemont': 0.0125,
                    'Marietta': 0.0185,
                    'Marion': 0.0200,
                    'Marshallville': 0.0100,
                    'Martins Ferry': 0.0100,
                    'Marysville': 0.0150,
                    'Mason': 0.0112,
                    'Massillon': 0.0200,
                    'Maumee': 0.0150,
                    'Mayfield': 0.0200,
                    'Mayfield Heights': 0.0100,
                    'Mechanicsburg': 0.0100,
                    'Medina': 0.0125,
                    'Melrose': 0.0100,
                    'Mentor': 0.0200,
                    'Mentor-On-The-Lake': 0.0200,
                    'Metamora': 0.0100,
                    'Miamisburg': 0.0225,
                    'Middleburg Heights': 0.0200,
                    'Middlefield': 0.0125,
                    'Middle Point': 0.0150,
                    'Middleport': 0.0100,
                    'Middletown': 0.0175,
                    'Midvale': 0.0100,
                    'Mifflin': 0.0100,
                    'Milan': 0.0100,
                    'Milford': 0.0100,
                    'Milford Center': 0.0100,
                    'Millbury': 0.0150,
                    'Miller City': 0.0100,
                    'Millersburg': 0.0150,
                    'Millersport': 0.0100,
                    'Mineral City': 0.0100,
                    'Minerva': 0.0175,
                    'Minerva Park': 0.0200,
                    'Mingo Junction': 0.0200,
                    'Minster': 0.0150,
                    'Mogadore': 0.0225,
                    'Monroe': 0.0200,
                    'Monroeville': 0.0100,
                    'Montgomery': 0.0100,
                    'Montpelier': 0.0160,
                    'Moraine': 0.0250,
                    'Moreland Hills': 0.0100,
                    'Morral': 0.0100,
                    'Morrow': 0.0100,
                    'Mount Blanchard': 0.0100,
                    'Mount Cory': 0.0100,
                    'Mount Eaton': 0.0100,
                    'Mount Gilead': 0.0100,
                    'Mount Healthy': 0.0200,
                    'Mount Orab': 0.0135,
                    'Mount Sterling': 0.0100,
                    'Mount Vernon': 0.0200,
                    'Mount Victory': 0.0100,
                    'Munroe Falls': 0.0225,
                    'Napoleon': 0.0150,
                    'Navarre': 0.0150,
                    'Nelsonville': 0.0175,
                    'New Albany': 0.0200,
                    'Newark': 0.0175,
                    'New Bavaria': 0.0100,
                    'New Bloomington': 0.0100,
                    'New Boston': 0.0250,
                    'New Bremen': 0.0150,
                    'Newburgh Heights': 0.0200,
                    'New Carlisle': 0.0150,
                    'Newcomerstown': 0.0200,
                    'New Concord': 0.0150,
                    'New Franklin': 0.0200,
                    'New Knoxville': 0.0150,
                    'New Lebanon': 0.0100,
                    'New Lexington': 0.0100,
                    'New London': 0.0150,
                    'New Madison': 0.0100,
                    'New Miami': 0.0175,
                    'New Paris': 0.0100,
                    'New Philadelphia': 0.0150,
                    'New Richmond': 0.0100,
                    'New Riegel': 0.0100,
                    'Newton Falls': 0.0100,
                    'Newtonsville': 0.0100,
                    'Newtown': 0.0100,
                    'New Washington': 0.0150,
                    'New Waterford': 0.0100,
                    'Ney': 0.0100,
                    'Niles': 0.0200,
                    'North Baltimore': 0.0100,
                    'North Canton': 0.0150,
                    'North College Hill': 0.0150,
                    'Northfield': 0.0200,
                    'North Kingsville': 0.0130,
                    'North Lewisburg': 0.0100,
                    'North Olmsted': 0.0200,
                    'North Perry': 0.0100,
                    'North Randall': 0.0275,
                    'North Ridgeville': 0.0100,
                    'North Robinson': 0.0100,
                    'North Royalton': 0.0200,
                    'North Star': 0.0050,
                    'Northwood': 0.0150,
                    'Norton': 0.0200,
                    'Norwalk': 0.0150,
                    'Norwood': 0.0200,
                    'Oak Harbor': 0.0100,
                    'Oak Hill': 0.0050,
                    'Oakwood': 0.0250,
                    'Oakwood': 0.0250,
                    'Oakwood': 0.0100,
                    'Oberlin': 0.0250,
                    'Obetz': 0.0250,
                    'Octa': 0.0100,
                    'Ohio City': 0.0100,
                    'Olmsted Falls': 0.0150,
                    'Ontario': 0.0150,
                    'Orange': 0.0200,
                    'Oregon': 0.0225,
                    'Orrville': 0.0100,
                    'Orwell': 0.0150,
                    'Osgood': 0.0100,
                    'Ostrander': 0.0100,
                    'Ottawa': 0.0100,
                    'Ottawa Hills': 0.0150,
                    'Ottoville': 0.0100,
                    'Owensville': 0.0100,
                    'Oxford': 0.0200,
                    'Painesville': 0.0200,
                    'Pandora': 0.0150,
                    'Parma': 0.0250,
                    'Parma Heights': 0.0300,
                    'Pataskala': 0.0100,
                    'Patterson': 0.0050,
                    'Paulding': 0.0100,
                    'Payne': 0.0100,
                    'Pemberville': 0.0100,
                    'Peninsula': 0.0200,
                    'Pepper Pike': 0.0100,
                    'Perry': 0.0200,
                    'Perrysburg': 0.0150,
                    'Perrysville': 0.0100,
                    'Phillipsburg': 0.0150,
                    'Pickerington': 0.0100,
                    'Piketon': 0.0100,
                    'Pioneer': 0.0100,
                    'Piqua': 0.0200,
                    'Plain City': 0.0150,
                    'Pleasant Hill': 0.0075,
                    'Pleasantville': 0.0100,
                    'Plymouth': 0.0100,
                    'Pomeroy': 0.0100,
                    'Portage': 0.0100,
                    'Port Clinton': 0.0150,
                    'Portsmouth': 0.0250,
                    'Port Washington': 0.0150,
                    'Powell': 0.0075,
                    'Powhatan Point': 0.0100,
                    'Quincy': 0.0100,
                    'Ravenna': 0.0250,
                    'Reading': 0.0200,
                    'Reminderville': 0.0150,
                    'Reynoldsburg': 0.0250,
                    'Richfield': 0.0200,
                    'Richmond Heights': 0.0225,
                    'Richwood': 0.0100,
                    'Ridgeway': 0.0050,
                    'Rio Grande': 0.0150,
                    'Ripley': 0.0100,
                    'Rittman': 0.0150,
                    'Riverside': 0.0150,
                    'Rock Creek': 0.0100,
                    'Rockford': 0.0100,
                    'Rocky River': 0.0200,
                    'Roseville': 0.0100,
                    'Rossford': 0.0225,
                    'Roswell': 0.0100,
                    'Rushsylvania': 0.0100,
                    'Russells Point': 0.0100,
                    'Russia': 0.0150,
                    'Sabina': 0.0150,
                    'St. Bernard': 0.0210,
                    'St. Clairsville': 0.0075,
                    'St. Henry': 0.0100,
                    'St. Louisville': 0.0100,
                    'St. Marys': 0.0150,
                    'St. Paris': 0.0100,
                    'Salem': 0.0125,
                    'Salineville': 0.0100,
                    'Sandusky': 0.0125,
                    'Sardinia': 0.0100,
                    'Scio': 0.0100,
                    'Sebring': 0.0200,
                    'Seven Hills': 0.0250,
                    'Seville': 0.0100,
                    'Shaker Heights': 0.0225,
                    'Sharonville': 0.0150,
                    'Shawnee Hills': 0.0200,
                    'Sheffield': 0.0200,
                    'Sheffield Lake': 0.0200,
                    'Shelby': 0.0150,
                    'Sherrodsville': 0.0100,
                    'Sherwood': 0.0100,
                    'Shreve': 0.0100,
                    'Sidney': 0.0175,
                    'Silver Lake': 0.0200,
                    'Silverton': 0.0125,
                    'Smithfield': 0.0100,
                    'Smithville': 0.0150,
                    'Solon': 0.0200,
                    'South Amherst': 0.0100,
                    'South Bloomfield': 0.0100,
                    'South Charleston': 0.0125,
                    'South Euclid': 0.0200,
                    'South Lebanon': 0.0100,
                    'South Russell': 0.0125,
                    'South Solon': 0.0100,
                    'South Vienna': 0.0100,
                    'South Zanesville': 0.0150,
                    'Spencerville': 0.0150,
                    'Springboro': 0.0150,
                    'Springdale': 0.0150,
                    'Springfield': 0.0240,
                    'Steubenville': 0.0200,
                    'Stone Creek': 0.0100,
                    'Stoutsville': 0.0100,
                    'Stow': 0.0200,
                    'Strasburg': 0.0150,
                    'Stratton': 0.0100,
                    'Streetsboro': 0.0200,
                    'Strongsville': 0.0200,
                    'Struthers': 0.0200,
                    'Stryker': 0.0150,
                    'Sugarcreek': 0.0150,
                    'Sugar Grove': 0.0075,
                    'Sunbury': 0.0100,
                    'Swanton': 0.0150,
                    'Sycamore': 0.0100,
                    'Sylvania': 0.0150,
                    'Tallmadge': 0.0200,
                    'Indian Hill': 0.0053,
                    'Thurston': 0.0100,
                    'Tiffin': 0.0200,
                    'Timberlake': 0.0100,
                    'Tipp City': 0.0150,
                    'Tiro': 0.0100,
                    'Toledo': 0.0225,
                    'Tontogany': 0.0100,
                    'Toronto': 0.0200,
                    'Tremont City': 0.0100,
                    'Trenton': 0.0150,
                    'Trimble': 0.0100,
                    'Trotwood': 0.0225,
                    'Troy': 0.0175,
                    'Tuscarawas': 0.0100,
                    'Twinsburg': 0.0200,
                    'Uhrichsville': 0.0200,
                    'Union': 0.0100,
                    'Union City': 0.0100,
                    'University Heights': 0.0250,
                    'Upper Arlington': 0.0250,
                    'Upper Sandusky': 0.0100,
                    'Urbana': 0.0140,
                    'Urbancrest': 0.0200,
                    'Utica': 0.0175,
                    'Valley Hi': 0.0100,
                    'Valley View': 0.0200,
                    'Valleyview': 0.0100,
                    'Vandalia': 0.0200,
                    'Vanlue': 0.0100,
                    'Van Wert': 0.0172,
                    'Vermilion': 0.0150,
                    'Versailles': 0.0150,
                    'Wadsworth': 0.0140,
                    'Wakeman': 0.0100,
                    'Walbridge': 0.0150,
                    'Walton Hills': 0.0250,
                    'Wapakoneta': 0.0150,
                    'Warren': 0.0250,
                    'Warrensville Heights': 0.0260,
                    'Washington': 0.0195,
                    'Washingtonville': 0.0050,
                    'Waterville': 0.0200,
                    'Wauseon': 0.0150,
                    'Waverly City': 0.0100,
                    'Wayne': 0.0075,
                    'Wayne Lakes': 0.0100,
                    'Waynesfield': 0.0100,
                    'Waynesville': 0.0050,
                    'Wellington': 0.0175,
                    'Wellston': 0.0100,
                    'Wellsville': 0.0150,
                    'West Alexandria': 0.0100,
                    'West Carrollton City': 0.0225,
                    'West Elkton': 0.0100,
                    'Westerville': 0.0200,
                    'Westfield Center': 0.0100,
                    'West Jefferson': 0.0100,
                    'West Lafayette': 0.0150,
                    'Westlake': 0.0150,
                    'West Liberty': 0.0100,
                    'West Mansfield': 0.0100,
                    'West Milton': 0.0150,
                    'Weston': 0.0100,
                    'West Salem': 0.0100,
                    'West Union': 0.0100,
                    'West Unity': 0.0150,
                    'Whitehall': 0.0250,
                    'Whitehouse': 0.0150,
                    'Wickliffe': 0.0200,
                    'Willard': 0.0138,
                    'Williamsburg': 0.0100,
                    'Williamsport': 0.0050,
                    'Willoughby': 0.0200,
                    'Willoughby Hills': 0.0200,
                    'Willowick': 0.0200,
                    'Willshire': 0.0100,
                    'Wilmington': 0.0150,
                    'Wilmot': 0.0175,
                    'Windham': 0.0150,
                    'Wintersville': 0.0100,
                    'Woodlawn': 0.0230,
                    'Woodmere': 0.0250,
                    'Woodsfield': 0.0100,
                    'Woodstock': 0.0100,
                    'Wooster': 0.0150,
                    'Worthington': 0.0250,
                    'Wyoming': 0.0100,
                    'Xenia': 0.0225,
                    'Yellow Springs': 0.0150,
                    'Youngstown': 0.0275,
                    'Zanesville': 0.0190,
                    'Ada EVSD': 0.0150,
                    'Anna LSD': 0.0150,
                    'Ansonia LSD': 0.0175,
                    'Antwerp LSD': 0.0150,
                    'Arcadia LSD': 0.0100,
                    'Arcanum-Butler LSD': 0.0150,
                    'Arlington LSD': 0.0125,
                    'Athens CSD': 0.0100,
                    'Ayersville LSD': 0.0100,
                    'Bellevue CSD': 0.0050,
                    'Berkshire LSD': 0.0100,
                    'Berne Union LSD': 0.0200,
                    'Bethel LSD': 0.0075,
                    'Bexley CSD': 0.0075,
                    'Big Walnut LSD': 0.0075,
                    'Bloom-Carroll LSD': 0.0125,
                    'Bluffton EVSD': 0.0050,
                    'Botkins LSD': 0.0125,
                    'Bowling Green CSD': 0.0050,
                    'Bradford EVSD': 0.0175,
                    'Bryan CSD': 0.0100,
                    'Buckeye Central LSD': 0.0150,
                    'Buckeye Valley LSD': 0.0100,
                    'Canal Winchester LSD': 0.0075,
                    'Cardington-Lincoln LSD': 0.0075,
                    'Carey EVSD': 0.0100,
                    'Carlisle LSD': 0.0100,
                    'Cedar Cliff LSD': 0.0125,
                    'Celina CSD': 0.0100,
                    'Centerburg LSD': 0.0075,
                    'Central LSD': 0.0075,
                    'Chippewa LSD': 0.0100,
                    'Circleville CSD': 0.0075,
                    'Clear Fork Valley LSD': 0.0100,
                    'Clermont-Northeastern LSD': 0.0100,
                    'Cloverleaf LSD': 0.0125,
                    'Clyde-Green Springs EVSD': 0.0100,
                    'Coldwater EVSD': 0.0050,
                    'Colonel Crawford LSD': 0.0125,
                    'Columbiana EVSD': 0.0100,
                    'Columbus Grove LSD': 0.0100,
                    'Continental LSD': 0.0100,
                    'Cory-Rawson LSD': 0.0175,
                    'Covington EVSD': 0.0200,
                    'Crestline EVSD': 0.0025,
                    'Crestview LSD (Columbiana Co.)': 0.0100,
                    'Crestview LSD (Van Wert Co.)': 0.0100,
                    'Dalton LSD': 0.0075,
                    'Danville LSD': 0.0150,
                    'Defiance CSD': 0.0050,
                    'Eastwood LSD': 0.0100,
                    'Eaton CSD': 0.0150,
                    'Edgerton LSD': 0.0100,
                    'Edon-Northwest LSD': 0.0100,
                    'Elgin LSD': 0.0075,
                    'Elmwood LSD': 0.0125,
                    'Evergreen LSD': 0.0175,
                    'Fairbanks LSD': 0.0100,
                    'Fairborn CSD': 0.0050,
                    'Fairfield Union LSD': 0.0200,
                    'Fairlawn LSD': 0.0075,
                    'Fayette LSD': 0.0100,
                    'Fort Loramie LSD': 0.0150,
                    'Fort Recovery LSD': 0.0150,
                    'Franklin Monroe LSD': 0.0075,
                    'Fremont CSD': 0.0125,
                    'Geneva Area CSD': 0.0125,
                    'Gibsonburg EVSD': 0.0100,
                    'Goshen LSD': 0.0100,
                    'Granville EVSD': 0.0075,
                    'Green LSD (Wayne Co.)': 0.0050,
                    'Greeneview LSD': 0.0100,
                    'Greenfield EVSD': 0.0125,
                    'Greenville CSD': 0.0050,
                    'Hardin Northern LSD': 0.0175,
                    'Hardin-Houston LSD': 0.0075,
                    'Hicksville EVSD': 0.0075,
                    'Highland LSD (Morrow Co.)': 0.0050,
                    'Hillsboro CSD': 0.0100,
                    'Hillsdale LSD': 0.0125,
                    'Holgate LSD': 0.0150,
                    'Hopewell-Loudon LSD': 0.0050,
                    'Jackson Center LSD': 0.0150,
                    'James A. Garfield LSD': 0.0150,
                    'Jefferson LSD': 0.0100,
                    'Jennings LSD': 0.0075,
                    'Johnstown-Monroe LSD': 0.0100,
                    'Jonathan Alder LSD': 0.0125,
                    'Kalida LSD': 0.0100,
                    'Kenton CSD': 0.0100,
                    'Lakota LSD (Sandusky Co.)': 0.0150,
                    'Lancaster CSD': 0.0150,
                    'Ledgemont LSD': 0.0125,
                    'Leipsic LSD': 0.0075,
                    'Liberty Center LSD': 0.0175,
                    'Liberty Union-Thurston LSD': 0.0175,
                    'Liberty-Benton LSD': 0.0075,
                    'Licking Valley LSD': 0.0100,
                    'Logan Elm LSD': 0.0100,
                    'London CSD': 0.0100,
                    'Loudonville-Perrysville EVSD': 0.0125,
                    'Madison LSD (Butler Co.)': 0.0050,
                    'Madison-Plains LSD': 0.0125,
                    'Mccomb LSD': 0.0150,
                    'Mechanicsburg EVSD': 0.0150,
                    'Miami East LSD': 0.0175,
                    'Millcreek-West Unity LSD': 0.0100,
                    'Miller City-New Cleveland Ls': 0.0125,
                    'Milton-Union EVSD': 0.0125,
                    'Minster LSD': 0.0100,
                    'Mississinawa Valley LSD': 0.0175,
                    'Mohawk LSD': 0.0100,
                    'Monroeville LSD': 0.0150,
                    'Montpelier EVSD': 0.0125,
                    'Mount Gilead EVSD': 0.0075,
                    'National Trail LSD': 0.0175,
                    'New Bremen LSD': 0.0100,
                    'New Knoxville LSD': 0.0125,
                    'New Lebanon LSD': 0.0125,
                    'New London LSD': 0.0100,
                    'New Miami LSD': 0.0100,
                    'New Riegel LSD': 0.0150,
                    'Newark CSD': 0.0100,
                    'Newton LSD': 0.0175,
                    'North Baltimore LSD': 0.0125,
                    'North Fork LSD': 0.0100,
                    'North Union LSD': 0.0100,
                    'Northeastern LSD (Clark Co.)': 0.0100,
                    'Northmor LSD': 0.0100,
                    'Northwest LSD (Stark Co.)': 0.0100,
                    'Northwestern LSD (Clark Co.)': 0.0100,
                    'Northwestern LSD (Wayne Co.)': 0.0125,
                    'Northwood LSD': 0.0025,
                    'Norton CSD': 0.0050,
                    'Norwalk CSD': 0.0050,
                    'Norwayne LSD': 0.0075,
                    'Oberlin CSD': 0.0200,
                    'Old Fort LSD': 0.0100,
                    'Otsego LSD': 0.0100,
                    'Ottawa-Glandorf LSD': 0.0150,
                    'Ottoville LSD': 0.0075,
                    'Pandora-Gilboa LSD': 0.0175,
                    'Parkway LSD': 0.0100,
                    'Patrick Henry LSD': 0.0175,
                    'Paulding EVSD': 0.0100,
                    'Perrysburg EVSD': 0.0050,
                    'Pettisville LSD': 0.0100,
                    'Pickerington LSD': 0.0100,
                    'Piqua CSD': 0.0125,
                    'Plymouth-Shiloh LSD': 0.0100,
                    'Preble Shawnee LSD': 0.0100,
                    'Reynoldsburg CSD': 0.0050,
                    'Ridgemont LSD': 0.0175,
                    'Riverdale LSD': 0.0100,
                    'Riverside LSD (Logan Co.)': 0.0175,
                    'Ross LSD': 0.0075,
                    'Russia LSD': 0.0075,
                    'Sebring LSD': 0.0100,
                    'Seneca East LSD': 0.0100,
                    'Shelby CSD': 0.0100,
                    'South Central LSD': 0.0125,
                    'Southeastern LSD': 0.0100,
                    'Southeastern LSD (Ross Co.)': 0.0075,
                    'Southwest Licking LSD': 0.0075,
                    'Southwest LSD': 0.0075,
                    'Spencerville LSD': 0.0100,
                    'Springfield LSD (Mahoning Co.)': 0.0100,
                    'St. Marys CSD': 0.0100,
                    'Stryker LSD': 0.0150,
                    'Swanton LSD': 0.0075,
                    'Talawanda CSD': 0.0100,
                    'Teays Valley LSD': 0.0150,
                    'Triad LSD': 0.0150,
                    'Tri-County North LSD': 0.0100,
                    'Tri-Village LSD': 0.0150,
                    'Triway LSD': 0.0075,
                    'Troy CSD': 0.0150,
                    'Twin Valley Community LSD': 0.0150,
                    'Union-Scioto LSD': 0.0050,
                    'United LSD': 0.0050,
                    'Upper Sandusky EVSD': 0.0125,
                    'Upper Scioto Valley LSD': 0.0050,
                    'Valley View LSD': 0.0125,
                    'Van Wert CSD': 0.0100,
                    'Vanlue LSD': 0.0100,
                    'Versailles EVSD': 0.0100,
                    'Walnut Twp LSD': 0.0175,
                    'Wapakoneta CSD': 0.0075,
                    'Wayne Trace LSD': 0.0125,
                    'Waynesfield-Goshen LSD': 0.0100,
                    'Wellington EVSD': 0.0100,
                    'West Liberty-Salem LSD': 0.0175,
                    'Western Reserve LSD (Huron Co.)': 0.0125,
                    'Willard CSD': 0.0075,
                    'Wilmington CSD': 0.0100,
                    'Wyoming CSD': 0.0125,
                    'Xenia Community CSD': 0.0050,
                    'Yellow Springs EVSD': 0.0100,
                    'Zane Trace LSD': 0.0075}   
        localBracket = ohioCounties[county]
        stateTaxes += localBracket * agi
        stateBracket += localBracket
    '''
    STATE INCOME TAXES
    TODO where to get state tax brackets?
    https://oklahoma.gov/content/dam/ok/en/tax/documents/forms/individuals/current/511-NR-Pkt.pdf
    '''
    elif state == 'Oklahoma':
        # $1000 dependent credit
        if maritalStatus == 'Married':
            if stateDeductions == 0:
                stateDeductions = 14700 + (dependents * 1000)
            agi -= stateDeductions
            if agi > 12200:
                stateBracket = .05
                margin = agi - 12200
                taxes = 255 + margin * stateBracket
            elif agi > 9800:
                stateBracket = .04
                margin = agi - 9800
                taxes = 159 + margin * stateBracket
            elif agi > 7500:
                stateBracket = .03
                margin = agi - 7500
                taxes = 90 + margin * stateBracket
            elif agi > 5000:
                stateBracket = .02
                margin = agi - 5000
                taxes = 40 + margin * stateBracket
            elif agi > 2000:
                stateBracket = .01
                margin = agi - 2000
                taxes = 10 + margin * stateBracket
            else:
                stateBracket = .005
                taxes = agi * stateBracket
        else:
            if stateDeductions == 0:
                stateDeductions = 12550 + (dependents * 1000)
            agi -= stateDeductions
            if agi > 7200:
                stateBracket = .05
                margin = agi - 7200
                taxes = 174.95 + margin * stateBracket
            elif agi > 4900:
                stateBracket = .04
                margin = agi - 4900
                taxes = 82.95 + margin * stateBracket
            elif agi > 3750:
                stateBracket = .03
                margin = agi - 3750
                taxes = 45 + margin * stateBracket
            elif agi > 2500:
                stateBracket = .02
                margin = agi - 2500
                taxes = 20 + margin * stateBracket
            elif agi > 1000:
                stateBracket = .01
                margin = agi - 1000
                taxes = 5 + margin * stateBracket
            else:
                stateBracket = .005
                taxes = agi * stateBracket
           
    '''
        STATE INCOME TAXES
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
    '''
    elif state == 'Oregon':
        # $210 dependent tax credit
        if maritalStatus == 'Married':
            if stateDeductions == 0:
                stateDeductions = 4630
                if agi < 200000:
                    taxes = -(420 + (dependents * 210))
            agi -= stateDeductions
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
        else:
            if stateDeductions == 0:
                stateDeductions = 2315
                if agi < 100000:
                    taxes = -(210 + (dependents * 210))
            agi -= stateDeductions
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
    elif state == 'Pennsylvania':
        taxes = agi * .0307
    
    '''
    STATE INCOME TAXES
    TODO FIX THIS 
    http://webserver.rilin.state.ri.us/Statutes/title44/44-30/44-30-12.HTM
    
    '''
    elif state == 'Rhode Island':
        if stateDeductions == 0:
            if maritalStatus == 'Married':
                stateDeductions = 18100
            elif maritalStatus == 'Head of Household':
                stateDeductions = 13550
            # Single in this case
            else:
                stateDeductions = 9050
            stateDeductions += (dependents * 4250)
        agi -= stateDeductions
        if agi > 155550:
            stateBracket = .0599
            margin = agi - 155550
            taxes = 6726.625 + margin * stateBracket

        elif agi > 66200:
            stateBracket = .0475
            margin = agi - 66200
            taxes = 2482.5 + margin * stateBracket
        else:
            stateBracket = .0375
            taxes = agi * stateBracket
    '''
    STATE INCOME TAXES
    https://dor.sc.gov/resources-site/lawandpolicy/Advisory%20Opinions/IL22-15.pdf
    For the 2022 tax year the new tax brackets, indexed for inflation, and tax computations for each bracket are:
    New Tax Brackets for Tax Year 2022      Bracket Amounts for Tax Year 2022       Compute the tax as follows for each bracket amount
    Tax Bracket #1                          $0 to $3,199                            0% times the amount (i.e., exempt from tax)
    Tax Bracket #2                          $3,200 to $16,039                       3% times the amount minus $96
    Tax Bracket #3                          $16,040 and up                          *6.5% times the amount minus $658
    '''
    elif state == 'South Carolina':
        # $4260 dependent deduction
        if stateDeductions == 0:
            if maritalStatus == 'Married':
                stateDeductions = 25100
            else:
                stateDeductions = 12550
            stateDeductions += (dependents * 4260)
        agi -= stateDeductions
        if agi > 15400:
            stateBracket = .07
            margin = agi - 15400
            taxes = 555 + margin * stateBracket
        elif agi > 12310:
            stateBracket = .06
            margin = agi - 12310
            taxes = 369.6 + margin * stateBracket
        elif agi > 9230:
            stateBracket = .05
            margin = agi - 9230
            taxes = 215.6 + margin * stateBracket
        elif agi > 6150:
            stateBracket = .04
            margin = agi - 6150
            taxes = 92.4 + margin * stateBracket
        elif agi > 3070:
            stateBracket = .03
            margin = agi - 3070
            taxes =  margin * stateBracket
    # !special margin !special tax credit
    elif state == 'Utah':
        # State credits are applied at the end
        # ! could be a bug, means user has deductions and not state credits
        if stateDeductions != 0 and stateCredits == 0:
            taxes = -stateDeductions * .06
        if stateDeductions == 0:
            taxes = 0
            if maritalStatus == 'Married':
                if agi < 29758:
                    taxes -= 1506
                elif agi < 115846.15:
                    margin = agi - 29758
                    taxes -= (1506 + (agi * .013))
            else:
                if agi < 14879:
                    taxes -= 753
                elif agi < 57923.07:
                    margin = agi - 14879
                    taxes -= (753 + (agi * .013))
            taxes -= (dependents * 590)
        agi -= stateDeductions
        stateBracket = .0495
        taxes += agi * stateBracket
    # !margin with special condition
    '''
    STATE INCOME TAXES
    https://tax.vermont.gov/individuals/personal-income-tax/rates
    
    Rate Schedule for Tax Year 2022
    https://tax.vermont.gov/sites/tax/files/documents/RateSched-2022.pdf

    Tax Tables for Tax Year 2022
    https://tax.vermont.gov/sites/tax/files/documents/TaxTables-2022.pdf

    TAXABLE INCOME
    https://tax.vermont.gov/individuals/personal-income-tax/taxable-income

    TAX CREDITS AND ADJSUTMENTS
    https://tax.vermont.gov/individuals/personal-income-tax/tax-credits

    '''
    elif state == 'Vermont':
        # $4350 dependent deduction
        if maritalStatus == 'Married':
            if stateDeductions == 0:
                stateDeductions = 21200 + (dependents * 4350)
            agi -= stateDeductions
            if agi > 248350:
                stateBracket = .0875
                margin = agi - 248350
                taxes = 15052.475 + margin * stateBracket
            elif agi > 163000:
                stateBracket = .076
                margin = agi - 163000
                taxes = 8575.875 + margin * stateBracket
            elif agi > 67450:
                stateBracket = .066
                margin = agi - 67450
                taxes = 2259.575 + margin * stateBracket
            else:
                stateBracket = .0335
                taxes = agi * stateBracket
        else:
            if stateDeductions == 0:
                stateDeductions = 10600 + (dependents * 4350)
            agi -= stateDeductions
            if agi > 204000:
                stateBracket = .0875
                margin = agi - 204000
                taxes = 13214.625 + margin * stateBracket
            elif agi > 97800:
                stateBracket = .076
                margin = agi - 97800
                taxes = 5143.425 + margin * stateBracket
            elif agi > 40350:
                stateBracket = .066
                margin = agi - 40350
                taxes = 1351.725 + margin * stateBracket
            else:
                stateBracket = .0335
                taxes = agi * stateBracket
        if taxes < .03 * agi:
            taxes = .03 * agi

    '''
    STATE INCOME TAXES
    TODO where are they?

    STATE STANDARD DEDUCTION
    https://www.tax.virginia.gov/sites/default/files/vatax-pdf/2022-760-instructions.pdf
    (P.1) Increase in Standard Deduction: New legislation enacted during the 2022 General Assembly session increases the standard deduction from $4,500 to $8,000 for single filers and from $9,000 to $16,000 for married f ilers filing jointly. 
    '''
    elif state == 'Virginia':
        # $930 dependent deduction
        if stateDeductions == 0:
            if maritalStatus == 'Married':
                stateDeductions = 10860
            else:
                stateDeductions = 5430
            stateDeductions += (dependents * 930)
        agi -= stateDeductions
        if agi > 17000:
            stateBracket = .057
            margin = agi - 17000
            taxes = 720 + margin * stateBracket
        elif agi > 5000:
            stateBracket = .05
            margin = agi - 5000
            taxes = 120 + margin * stateBracket
        elif agi > 3000:
            stateBracket = .03
            margin = agi - 3000
            taxes = 60 + margin * stateBracket
        else:
            stateBracket = .02
            taxes = agi * stateBracket

    '''
    STATE INCOME TAXES
    https://tax.wv.gov/Individuals/Pages/Individuals.aspx

    2022 PUBLICATION
    https://tax.wv.gov/Documents/PIT/2022/PersonalIncomeTaxFormsAndInstructions.2022.pdf
    
    2022  TAX RATE SCHEDULES
    RATE SCHEDULE I Use this schedule if you checked 1 (Single), 2 (Head of household), 3 (Married fi ling joint), or 5 (Widow[er] with dependent child) under “FILING STATUS”.
    Less than $10,000               3% of the taxable income
    At least    –But less than 
    $10,000     $25,000             $300.00 plus 4% of excess over $10,000
    $25,000     $40,000             $900.00 plus 4.5% of excess over $25,000
    $40,000     $60,000             $1,575.00 plus 6% of excess over $40,000
    $60,000                         $2,775.00 plus 6.5% of excess over $60,000
    
    RATE SCHEDULE II Use this schedule if you checked box 4 (Married fi ling separately) under “FILING STATUS”.
    Less than $5,000                3% of the taxable income
    At least    –But less than      
    $5,000$     12,500              $150.00 plus 4% of excess over $5,000
    $12,500     $20,000             $450.00 plus 4.5% of excess over $12,500
    $20,000     $30,000             $787.50 plus 6% of excess over $20,000
    $30,000                         $1,387.50 plus 6.5% of excess over $30,000


    
    '''
    elif state == 'West Virginia':
        if stateDeductions == 0:
            if maritalStatus == 'Married':
                stateDeductions = 10860
            else:
                stateDeductions = 5430
            # $2000 dependent deduction
            dependents += (dependents * 2000)
        agi -= stateDeductions
        if agi > 60000:
            stateBracket = .065
            margin = agi - 60000
            taxes = 720 + margin * stateBracket
        elif agi > 40000:
            stateBracket = .06
            margin = agi - 1000
            taxes = 120 + margin * stateBracket
        elif agi > 25000:
            stateBracket = .045
            margin = agi - 25000
            taxes = 120 + margin * stateBracket
        elif agi > 10000:
            stateBracket = .04
            margin = agi - 10000
            taxes = 60 + margin * stateBracket
        else:
            stateBracket = .03
            taxes = agi * stateBracket
        if county == 'Charleston':
            taxes += 6 * payPeriod
        elif county == 'Huntington':
            taxes += 5 * payPeriod
        elif county == 'Parkersburg':
            taxes += 5 * payPeriod
        elif county == 'Huntington':
            taxes += 10 * payPeriod
        elif county == 'Weirton':
            taxes += 104

    '''
    STATE INCOME TAXES
    https://www.revenue.wi.gov/Pages/FAQS/pcs-taxrates.aspx#tx1a

    For single taxpayers, taxpayers qualified to file as head of household, estates, and trusts with taxable income:
    over	    but not over	2022 tax is 	    of the amount over
    $0	        $12,760	        3.54%	            $0
    $12,760     $25,520	        $451.70 + 4.65%	    $12,760
    $25,520	    $280,950	    $1,045.04 + 5.3%	$25,520
    $280,950                	$14,582.83 + 7.65%	$280,950

    For married taxpayers filing a joint return with taxable income:
    over	    but not over	2022 tax is	        of the amount over
    $0	        $17,010         3.54%	            $0
    $17,010     $34,030         $602.15 + 4.65%	    $17,010
    $34,030     $374,600        $1,393.58 + 5.3%	$34,030
    $374,600                    $19,443.79 + 7.65%	$374,600

    For married taxpayers filing separate returns with taxable income:

    over	    but not over	2022 tax is	        of the amount over
    $0	        $8,510          3.54%	            $0      
    $8,510      $17,010         $301.25 + 4.65% 	$8,510
    $17,010     $187,300	    $696.50 + 5.3%	    $17,010
    $187,300                    $9,721.87 + 7.65%	$187,300
    '''
    elif state == 'Wisconsin':
        # $4350 dependent deduction
        if maritalStatus == 'Married':
            if stateDeductions == 0:
                stateDeductions = 21200 + (dependents * 4350)
            agi -= stateDeductions
            if agi > 355910:
                stateBracket = .0765
                margin = agi - 355910
                taxes = 20288.466 + margin * stateBracket
            elif agi > 32330:
                stateBracket = .0627
                margin = agi - 32330
                taxes = 1323.969 + margin * stateBracket
            elif agi > 16160:
                stateBracket = .0465
                margin = agi - 16160
                taxes = 572.064 + margin * stateBracket
            else:
                stateBracket = .0354
                taxes = agi * stateBracket
        else:
            if stateDeductions == 0:
                stateDeductions = 10600 + (dependents * 4350)
            agi -= stateDeductions
            if agi > 266930:
                stateBracket = .0765
                margin = agi - 266930
                taxes = 16209.129 + margin * stateBracket
            elif agi > 24250:
                stateBracket = .0627
                margin = agi - 24250
                taxes = 993.093 + margin * stateBracket
            elif agi > 12120:
                stateBracket = .0465
                margin = agi - 12120
                taxes = 429.048 + margin * stateBracket
            else:
                stateBracket = .0354
                taxes = agi * stateBracket
    '''
    https://otr.cfo.dc.gov/page/dc-individual-and-fiduciary-income-tax-rates
    Tax Rates: The tax rates for tax years beginning after 12/31/2021 are:

    If the taxable income is:	The tax is:
    Not over $10,000	4% of the taxable income.
    Over $10,000 but not over $40,000	$400, plus 6% of the excess over $10,000.
    Over $40,000 but not over $60,000	$2,200, plus 6.5% of the excess over $40,000.
    Over $60,000 but not over $250,000	$3,500, plus 8.5% of the excess over $60,000.
    Over $250,000 but not over $500,000	$19,650, plus 9.25% of the excess over $250,000.
    Over $500,000 but not over $1,000,000	$42,775, plus 9.75% of the excess above $500,000.
    Over $1,000,000	$91,525, plus 10.75% of the excess above $1,000,000.
    
    '''
    elif state == 'District of Columbia':
        if maritalStatus == 'Married':
            if stateDeductions == 0:
                stateDeductions = 25100
        else:
            if stateDeductions == 0:
                stateDeductions = 12550
        agi -= stateDeductions
        if agi > 1000000:
            stateBracket = .0895
            margin = agi - 1000000
            taxes = 85025 + margin * stateBracket
        elif agi > 350000:
            stateBracket = .0875
            margin = agi - 350000
            taxes = 28150 + margin * stateBracket
        elif agi > 60000:
            stateBracket = .085
            margin = agi - 60000
            taxes = 3500 + margin * stateBracket
        elif agi > 40000:
            stateBracket = .065
            margin = agi - 40000
            taxes = 2200 + margin * stateBracket
        elif agi > 10000:
            stateBracket = .06
            margin = agi - 10000
            taxes = 400 + margin * stateBracket
        else:
            stateBracket = .04
            taxes = agi * stateBracket
    # If user had credits reduce their tax burden
    if stateCredits:
        taxes -= stateCredits
    # stateBracket includes localBracket
    stateBracket += localBracket
    return taxes, stateBracket, margin
