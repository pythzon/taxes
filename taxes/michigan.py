'''
MICHIGAN INCOME TAXES 2023
https://www.michigan.gov/taxes/iit/new-developments-for-tax-year-2022

4.25% tax rate

EXEMPTIONS 2023
https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/2023/2023-SUW/446_Withholding-Guide_2023.pdf?rev=177ca3d8cb034392bf84e317ed78c320&hash=19C5F42F43A89A91863D229349F48883#:~:text=The%20exemption%20amount%20is%20%245%2C400,employee's%20Michigan%20income%20tax%20return.
$5,400 for personal and dependent exemptions

STANDARD DEDUCTIONS (Same as exemptions) 2023
https://www.michigan.gov/taxes/iit/retirement-and-pension-benefits/michigan-standard-deduction#:~:text=This%20deduction%20is%20referred%20to,using%20the%20Tier%20Structure%20Subtraction
If over age 67, $40,000 for married filing jointly, $20,000 for all others

LOCAL INCOME TAXES 2022
https://www.michigan.gov/taxes/questions/iit/accordion/general/what-cities-impose-an-income-tax

NON-RESIDENT IS 50% OF THE FOLLOWING RESIDENT RATES
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

RECIRPOCAL AGREEMENTS 2023
(Also listed in 2023 tax withholding guide)
https://www.michigan.gov/taxes/questions/iit/accordion/residency/are-my-wages-earned-in-another-state-taxable-in-michigan-if-i-am-a-michigan-resident-1
Illinois, Indiana, Kentucky, Minnesota, Ohio, and Wisconsin

CAPITAL GAINS 2023
https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/2022/2022-IIT-Forms/BOOK_MI-1040.pdf?rev=4524f1cbbc0243b194ab05a6680be75b&hash=40DFE71E651F7C1D65C31F6CD03D944F
If Age 67 or older, interest, dividends, and capital gains are deductible up to $25,394 for married filing jointly and $12,697 for all others
Otherwise, net capital gains are treated as ordinary income
'''

class Michigan:
    if resState in ['Illinois', 'Indiana', 'Kentucky', 'Minnesota', 'Ohio', 'Wisconsin']:
            workState = resState

    if stateDeductions == 0:
        if maritalStatus == 'Married Filing Jointly':
            stateDeductions = 10800 + (dependents * 5400)
        else:
            stateDeductions = 5400 + (dependents * 5400)
    agi -= stateDeductions

    taxes = -stateCredits

    stateBracket = .0425
    taxes += agi * stateBracket

    michiganCounties = {"Other":               0,  
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
    
    if resState != 'Michigan':
        localBracket *= .5

    taxes += agi * localBracket
    stateBracket += localBracket