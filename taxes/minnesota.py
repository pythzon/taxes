'''
MINNESOTA INCOME TAXES
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

RECIRPOCAL AGREEMENTS
https://mn.gov/mmb/assets/mwr_form_tcm1059-128581.pdf
North Dakota and Michigan
'''
    
class Minnesota:
    if resState in ['North Dakota', 'Michigan']:
            workState = resState
    
    taxes = -stateCredits
    
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