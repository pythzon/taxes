'''
MARYLAND INCOME TAXES (2022)
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
Over $300,000	               $15,072.50 plus 5.75% of the excess over $300,000

LOCAL INCOME TAX (2023)
https://www.marylandtaxes.gov/individual/income/tax-info/tax-rates.php
Your local income tax is based on where you live - not where you work
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
Other       	    	.0225

* Anne Arundel Co. The local tax rates for taxable year 2023 are as follows:
(1) .0270 of an individual’s Maryland taxable income of $1 through $50,000; and
(2) .0281 of an individual’s Maryland taxable income in excess of $50,000.

** Frederick Co. The local tax rates for taxable year 2023 are as follows:
(1) .0275 for taxpayers with Maryland taxable income of $100,000 or less and a filing status of married filing joint, head of household, and qualifying widow(er) with dependent child;
(2) .0275 for taxpayers with Maryland taxable income of $50,000 or less and a filing status of single, married filing separately, and dependent; and
(3) .0296 for all other taxpayers.    

EXEMPTIONS (Only if itemizing, not considered since federal deductions are more significant)
https://www.marylandtaxes.gov/forms/22_forms/Resident_Booklet.pdf (P. 33, Line 6)
$3,200 for each individual/spouse and dependent
$1,000 for each individual/spouse over 65

STANDARD DEDUCTION
https://www.marylandtaxes.gov/forms/22_forms/Resident_Booklet.pdf (P. 33, Line 4)
15% of AGI
Minumums:
    $1,600 for single, married filing separately
    $3,200 for married filing jointly, head of household
Maximums:
    $2,400 for single, married filing separately
    $4,850 for married filing jointly, head of household

RECIRPOCAL AGREEMENTS
https://www.marylandtaxes.gov/forms/Tax_Publications/Administrative_Releases/Income_and_Estate_Tax_Releases/ar_it37.pdf
VI. Recpirocal Agreement -> District of Columbia, Virginia, Pennsylvania, and West Virginia
'''
class Maryland:
    if resState in ['District of Columbia', 'Virginia', 'Pennsylvania', 'West Virginia']:
            workState = resState

    taxes = -stateCredits

    if stateDeductions == 0:
        if maritalStatus in ['Married Filing Jointly', 'Head of Household']:
            if agi > 32333.33:
                stateDeductions = 4850
            elif agi > 21333.33:
                stateDeductions = agi * .15
            else:
                stateDeductions = 3200
            # filers = 2
        else: # Single and married filing separately
            if agi > 16000:
                stateDeductions = 2400
            elif agi > 10666.67:
                stateDeductions = agi * .15
            else:
                stateDeductions = 1600
            # filers = 1
        # COMMENTED OUT PORTION IS FOR ITEMEIZING
        # stateDeductions += (dependents + filers) * 3200 + numOver65 * 1000
    agi -= stateDeductions

    if maritalStatus in ['Married Filing Jointly', 'Head of Household']:
        if agi > 250000:
            stateBracket = .0575
            margin = agi - 250000
            taxes += 12760 + margin * stateBracket
        elif agi > 150000:
            stateBracket = .055
            margin = agi - 150000
            taxes += 7260 + margin * stateBracket
        elif agi > 125000:
            stateBracket = .0525
            margin = agi - 125000
            taxes += 5947.5 + margin * stateBracket
        elif agi > 100000:
            stateBracket = .05
            margin = agi - 100000
            taxes += 4697.5 + margin * stateBracket
        elif agi > 3000:
            stateBracket = .0475
            margin = agi - 3000
            taxes += 90 + margin * stateBracket
        elif agi > 2000:
            stateBracket = .04
            margin = agi - 2000
            taxes += 50 + margin * stateBracket
        elif agi > 1000:
            stateBracket = .03
            margin = agi - 1000
            taxes += 20 + margin * stateBracket
        else:
            stateBracket = .02
            taxes += agi * stateBracket
    
    else: # All other filers
        if agi > 300000:
            stateBracket = .0575
            margin = agi - 300000
            taxes += 15072.5 + margin * stateBracket
        elif agi > 225000:
            stateBracket = .055
            margin = agi - 225000
            taxes += 10947.5 + margin * stateBracket
        elif agi > 175000:
            stateBracket = .0525
            margin = agi - 175000
            taxes += 8322.5 + margin * stateBracket
        elif agi > 150000:
            stateBracket = .05
            margin = agi - 100000
            taxes += 7072.5 + margin * stateBracket
        elif agi > 3000:
            stateBracket = .0475
            margin = agi - 3000
            taxes += 90 + margin * stateBracket
        elif agi > 2000:
            stateBracket = .04
            margin = agi - 2000
            taxes += 50 + margin * stateBracket
        elif agi > 1000:
            stateBracket = .03
            margin = agi - 1000
            taxes += 20 + margin * stateBracket
        else:
            stateBracket = .02
            taxes = agi * stateBracket

    if county == 'Anne Arundel County':
        if agi > 50000:
            localBracket = .0281
            marginLocal = agi - 50000
            taxes += 1350 + margin * localBracket
            
            # Return closeset margin to determine next tax bracket recalculation
            if marginLocal < margin:
                margin = marginLocal
        else:
            localBracket = .0270
            taxes += agi * localBracket

    elif county == 'Frederick County':
        if maritalStatus == 'Single' and agi < 50000:
            localBracket = .0275
            marginLocal = agi - 50000
        elif agi < 100000: # All other filers
            localBracket = .0275
            marginLocal = agi - 100000
        else:
            localBracket = .0296
            marginLocal = 999999
        taxes += agi * localBracket

        # Return closeset margin to determine next tax bracket recalculation
        if marginLocal < margin:
            margin = marginLocal
    else:
        marylandCounties = {
                        "Other":            	    .0225,
                        "Allegany County":		    .0303,
                        "Baltimore City":	    	.0320,
                        "Baltimore County":		    .0320,
                        "Calvert County":	    	.0300,
                        "Caroline County":	        .0320,
                        "Carroll County":	        .0303,
                        "Cecil County":	            .0280,
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
                        "Washington County":        .0295,
                        "Wicomico County":	        .0320,
                        "Worcester County":    	    .0225}
        localBracket = marylandCounties[county]
        taxes += agi * localBracket
    stateBracket += localBracket 