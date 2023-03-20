'''
COLORADO INCOME TAX
https://leg.colorado.gov/agencies/legislative-council-staff/individual-income-tax%C2%A0
FLAT RATE -> 4.55%

NO STANDARD OR DEPENDENT DEDUCTIONS (Additions/Subtractions section)
https://leg.colorado.gov/agencies/legislative-council-staff/individual-income-tax%C2%A0

LOCAL INCOME TAXES
https://www.auroragov.org/business_services/taxes/occupational_privilege_tax
Aurora ->$2 per month

https://www.denvergov.org/Government/Agencies-Departments-Offices/Agencies-Departments-Offices-Directory/Department-of-Finance/Our-Divisions/Treasury/Business-Tax-Information#:~:text=Occupational%20privilege%20tax,-%28show%20below%29&text=Each%20taxable%20employee%20is%20liable,month%20for%20each%20taxable%20employee.
Denver -> $5.75 per month

https://www.glendale.co.us/355/Occupational-Privilege-Tax
Glendale -> $5 per month    

https://www.greenwoodvillage.com/1220/Occupational-Privilege-Tax-OPT
Greenwood Village -> $2 per month

https://ci.sheridan.co.us/288/Occupational-Privilege-Tax
Sheridan -> $3 per month
'''
class Colorado:
    taxes -= stateCredits
    agi -= stateDeductions

    stateBracket = .0455

    taxes += agi * stateBracket
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