'''
PENNSYLVANIA INCOME TAXES
https://www.revenue.pa.gov/Tax%20Rates/Pages/default.aspx
3.07%

LOCAL TAXES (Published July 25, 2022)
https://www.nfc.usda.gov/Publications/HR_Payroll/Taxes/Bulletins/2022/TAXES-22-25.htm
    
City                    Resident Percentage     Nonresident Percentage
Bethlehem               1.0000                  1.0000
Bradford                1.0000                  1.0000
Caln Township           1.0000                  1.0000
Camp Hill               2.0000                  1.0000
Carlisle                1.6000                  1.0000
Erie                    1.6500                  1.6500
Fairview Township       1.0000                  1.0000
Greene Township         1.7000                  1.0000
Gregg Township          1.8000                  1.0000
Hanover                 1.0000                  1.0000
Harrisburg              2.0000                  1.0000
Horsham Township        1.0000                  1.0000
Kelly Township          2.0000                  1.0000
Lancaster               1.1000                  1.0000
Monroeville             1.5000                  1.0000
Philadelphia            3.7900                  3.4400
Pittsburgh              3.0000                  1.0000
Plains Township         1.000                   1.0000
Reading                 3.6000                  1.0000
Scranton                3.4000                  1.0000
South Lebanon Township  1.0000                  0.0000
South Park Township     1.0000                  1.0000
Susquehanna Township    1.0000                  1.0000
Tinicum Township        1.0000                  1.0000
Tredyffrin Township     0.0000                  0.0000
Warminster Township     1.0000                  1.0000
Wilkes-Barre            3.0000                  1.0000
York Township           1.0000                  1.0000

NO DEDUCTIONS
https://www.revenue.pa.gov/FormsandPublications/FormsforIndividuals/PIT/Documents/2022/2022_pa-40in.pdf (P. 9)

RECIRPOCAL AGREEMENTS
https://www.revenue.pa.gov/FormsandPublications/FormsforBusinesses/EmployerWithholding/Documents/rev-419.pdf
Indiana, New Jersey, Maryland, Ohio, and West Virginia

CAPITAL GAINS
https://www.revenue.pa.gov/FormsandPublications/FormsforIndividuals/PIT/Documents/2022/2022_pa-40in.pdf (P. 15)
Treated as ordinary income
'''

class Pennsylvania:
    if resState == ['Indiana', 'New Jersey', 'Maryland', 'Ohio', 'West Virginia']:
            workState = resState

    agi -= stateDeductions
    taxes = -stateCredits

    stateBracket = .0307
    taxes += agi * stateBracket

    pennsylvania = {"Other": [0.0000, 0.0000],
                    "Bethlehem": [1.0000, 1.0000],
                    "Bradford": [1.0000, 1.0000],
                    "Caln Township": [1.0000, 1.0000],
                    "Camp Hill": [2.0000, 1.0000],
                    "Carlisle": [1.6000, 1.0000],
                    "Erie": [1.6500, 1.6500],
                    "Fairview Township": [1.0000, 1.0000],
                    "Greene Township": [1.7000, 1.0000],
                    "Gregg Township": [1.8000, 1.0000],
                    "Hanover": [1.0000, 1.0000],
                    "Harrisburg": [2.0000, 1.0000],
                    "Horsham Township": [1.0000, 1.0000],
                    "Kelly Township": [2.0000, 1.0000],
                    "Lancaster": [1.1000, 1.0000],
                    "Monroeville": [1.5000, 1.0000],
                    "Philadelphia": [3.7900, 3.4400],
                    "Pittsburgh": [3.0000,1.0000],
                    "Plains Township": [1.000, 1.0000],
                    "Reading": [3.6000, 1.0000],
                    "Scranton": [3.4000, 1.0000],
                    "South Lebanon Township": [1.0000, 0.0000],
                    "South Park Township": [1.0000, 1.0000],
                    "Susquehanna Township": [1.0000, 1.0000],
                    "Tinicum Township": [1.0000, 1.0000],
                    "Tredyffrin Township": [0.0000, 0.0000],
                    "Warminster Township": [1.0000, 1.0000],
                    "Wilkes-Barre": [3.0000, 1.0000],
                    "York Township": [1.0000, 1.0000]}
    
    if resState == 'Pennsylvania':
        localBracket = pennsylvania[county][0]
    
    elif workState == 'Pennsylvania':
        localBracket = pennsylvania[county][1]

    stateBracket += localBracket
    taxes += agi * localBracket