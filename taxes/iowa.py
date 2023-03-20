'''
IOWA INCOME TAXES (2023-2026)
https://tax.iowa.gov/2023-changes-iowa-individual-income-tax#:~:text=Individual%20Income%20Tax%20Rates%20(HF%202317)&text=Beginning%20in%20tax%20year%202026,who%20file%20a%20joint%20return.

Income Tax Brackets	Rates (Brackets double for married filing jointly)
Lower Limit	    Upper Limit	    TY 2023	    TY 2024 	TY 2025	    TY 2026
$0	            $6,000	        4.40%	    4.40%   	4.40%   	3.90%
$6,001	        $30,000	        4.82%   	4.82%   	4.82%   	3.90%
$30,001	        $75,000	        5.70%	    5.70%	    4.82%   	3.90%
$75,001	And over            	6.00%	    5.70%   	4.82%   	3.90%

DEDUCTIONS
Same as federal Per 2023 changes?

LOCAL INCOME TAXES
www.freetaxusa.com/FreeTaxUSA/formdownload?form=ia_school_dist.pdf
COUNTIES LISTED BELOW

RETIREMENT INCOME EXCLUSION
https://tax.iowa.gov/2023-changes-iowa-individual-income-tax#:~:text=Individual%20Income%20Tax%20Rates%20(HF%202317)&text=Beginning%20in%20tax%20year%202026,who%20file%20a%20joint%20return.
ALLOWS FOR FREE TRADITIONAL IRA TO ROTH IRA CONVERSION!?

RECIPROCITY AGREEMENTS
https://tax.iowa.gov/iowa-illinois-reciprocal-agreement
Illinois 

CAPITAL GAINS
Taxed as ordinary income
'''

class Iowa:
    if resState == 'Illinois':
            workState = resState

    if stateDeductions == 0:
        stateDeductions = federalDeductions 
    agi -= stateDeductions
    
    # $40 credit per dependent
    if stateCredits == 0:
        taxes = -dependents * -40
    else:
        taxes = -stateCredits

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
    
    if county == 'Appanoose County':
        localBracket = .01
        taxes += agi * localBracket
        stateBracket += localBracket
    # Levies taxes as a percentage of state taxes
    else:
        iowaCounties = {
                'Other': 0,
                'AGWSR SD': 0.08,
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
