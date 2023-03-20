'''
CALIFORNIA INCOME TAXES
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

CREDITS doesn't specify formula for credits, hence excluded
https://www.ftb.ca.gov/about-ftb/newsroom/caleitc/eligibility-and-credit-information.html
2022 CalEITC
# qualifying children	California maximum income	CalEITC(up to)	YCTC (up to)	FYTC (up to)   Federal EITC (up to)
None	                $30,000	                    $275	        $0	            $1,083	       $560
1	                    $30,000	                    $1,843	        $1,083	        $1,083	       $3,733
2	                    $30,000	                    $3,037	        $1,083	        $1,083	       $6,164
3 or more	            $30,000	                    $3,417	        $1,083	        $1,083	       $6,935

CAPITAL GAINS
https://www.ftb.ca.gov/file/personal/income-types/capital-gains-and-losses.html#:~:text=California%20does%20not%20have%20a,are%20taxed%20as%20ordinary%20income.
Taxed as ordinary income
'''

class California:    
    # TODO? agi += capitalGains

    taxes = -stateCredits

    if maritalStatus == 'Single':
        if stateDeductions == 0:
            stateDeductions = 5202
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