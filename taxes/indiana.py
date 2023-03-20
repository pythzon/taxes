'''
INDIANA INCOME TAXES
https://www.in.gov/dor/tax-forms/2022-individual-income-tax-forms/ (IT-40PNR Booklet)
3.23% on all income

LOCAL INCOME TAXES
https://www.in.gov/dor/files/2022-county-tax-rates-and-codes.pdf
COUNTIES LISTED IN CODE

DEDUCTIONS
https://www.nfc.usda.gov/Publications/HR_Payroll/Taxes/Bulletins/2022/TAXES-22-32.htm
$1,000 per spouse, person over 65, and minimum for all dependents
$1,500 per qualifying dependent

RECRIPROCAL AGREEMENTS
Kentucky, Michigan, Ohio, Pennsylvania, Wisconsin
'''
class Indiana:
    if resState in ['Kentucky', 'Michigan', 'Ohio', 'Pennsylvania', 'Wisconsin']:
            workState = resState
    # TODO verify $1000-1500 dependent deduction but 1500 in nearly all cases (19 or younger or in college)
    if stateDeductions == 0:
        if maritalStatus == 'Married Filing Jointly':
            stateDeductions = (2 + numOver65) * 1000 + (dependents * 1500)
        else:
            stateDeductions = (1 + numOver65) * 1000+ (dependents * 1500)
    agi -= stateDeductions

    taxes = -stateCredits

    stateBracket = .0323
    taxes += agi * stateBracket

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
