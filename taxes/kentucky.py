'''
KENTUCKY INCOME TAX RATES
https://revenue.ky.gov/News/Pages/DOR-Announces-Updates-to-Individual-Income-Tax-for-2023-Tax-Year.aspx
https://revenue.ky.gov/Individual/Individual-Income-Tax/Pages/default.aspx

DEDUCTIONS
https://revenue.ky.gov/News/Pages/DOR-Announces-Updates-to-Individual-Income-Tax-for-2023-Tax-Year.aspx
MARRIED - $5,960
OTHERWISE - $2,980

CHILD AND DEPENDENT CARE CREDIT (Currently not considering, many states have this)
https://revenue.ky.gov/Individual/Individual-Income-Tax/Pages/default.aspx
20% OF THE FEDERAL CREDIT

LOCAL TAXES (2021)
https://nfc.usda.gov/Publications/HR_Payroll/Taxes/Bulletins/2021/TAXES-21-32.htm?taxmap=true

City                    Rate
Bowling Green          1.85%
Covington               2.45%*
Florence                2.00%**
Frankfort               1.95%
Lexington-Fayette       2.25%
Louisville              1.45%
Owensboro               1.78%
Paducah                 2.00%
Richmond                2.00%


* Maximum withholding wage base of $160,200*** (maximum annual withholding of $3,601.50).
** Maximum withholding wage base of $160,200*** (maximum annual withholding of $2,940.00).
*** Assuming $147,000 limit increased along with the Social Security wage limit

RECIRPOCAL AGREEMENTS
https://revenue.ky.gov/DOR%20Training%20Materials/103%20KAR%2017.140.%20Individual%20income%20tax%20-%20reciprocity%20-%20nonresidents.pdf
Ohio, Illinois, Michigan, Wisconsin, Pennsylvania, Indiana, West Virginia
'''

class Kentucky:
    if resState in ['Ohio', 'Illinois', 'Michigan', 'Wisconsin', 'Pennsylvania', 'Indiana', 'West Virginia']:
            workState = resState

    if stateDeductions == 0:
        if maritalStatus == 'Married':
            stateDeductions = 5960
        else:
            stateDeductions = 2980
    agi -= stateDeductions

    taxes = -stateCredits

    stateBracket = .045
    taxes += agi * stateBracket

    kentuckyCounties = {"Other": 0,
                        "Bowling Green": .0185,
                        "Covington": .0245,
                        "Florence": .0200,
                        "Frankfort": .0195,
                        "Lexington-Fayette": .0225,
                        "Louisville": .0145,
                        "Owensboro": .0178,
                        "Paducah": .0200,
                        "Richmond": .0200}
    
    localBracket = kentuckyCounties[county]
    
    if agi > 160200 and county == "Covington":
            localTaxes = 3601.5
            margin = agi - 160200
            taxes += localTaxes
    elif agi > 160200 and  county == "Florence":
            localTaxes = 2940
            margin = agi - 160200
            taxes += localTaxes
    else:
        stateBracket += localBracket
        taxes += agi * localBracket
