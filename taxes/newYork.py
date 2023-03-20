'''
NEW YORK INCOME TAXES
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
https://www.tax.ny.gov/pit/file/nonresident-faqs.htm
ONLY FOR RESIDENTS, NOT WORKERS

YONKERS
https://www.tax.ny.gov/forms/html-instructions/2022/it/it201i-2022.htm#yonkers-tax-rate-schedule
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

class NewYork:
    taxes = -stateCredits
    
    if maritalStatus == 'Married Filing Jointly':
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
    elif maritalStatus in ['Single', 'Married Filing Separately']:
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
        if stateDeductions == 0:
            stateDeductions = 11200 + (dependents * 1000)
        agi -= stateDeductions
        
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
        
        else: # Single or married filing seperately in this case
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