# Projects the SSI benefits for a given salary and retirement age
def ssibenefits(salary, benefitsElection):
    '''
    Average Wage Indexing (AWI) Series
    https://www.ssa.gov/oact/cola/awiseries.html
    
    The folloeing is the code for determining the maximum SSI benefits or can be adapted for historical salaries.
    AWI and Max Earnings go back to 1966 for most users
    awi = np.array([4983.36, 5213.44, 5571.76, 5893.76, 6186.24, 6497.08, 7133.8, 7580.16, 8030.76, 8630.92, 9226.48,
                     9779.44, 10556.03, 11479.46, 12513.46, 13773.1, 14531.34, 15239.24, 16135.07, 16822.51, 17321.82,
                     18426.59, 19334.55, 20099.55, 21027.98, 21811.60, 22935.42, 23132.67, 23753.53, 24705.66, 25913.90,
                     27426.00, 28861.44, 30469.84, 32154.82, 32921.92, 33252.09, 34064.95, 35648.55, 36952.94, 38651.41,
                     40405.48, 41334.97, 41673.83, 42979.61, 44321.67, 44888.16, 46481.52, 48098.63, 48642.15, 50321.89,
                     52145.80, 54099.99, 55628.6, 60,575.07, 60,575.07])
    factors = np.array([0.0000000000000] * len(awi))
    for i in range(len(awi)):
        factors[i] = awi[-1] / awi[i]

    Contribution and benefit base (CBB) Series Since 1968
    https://www.ssa.gov/oact/cola/cbb.html

    maxEarnings = np.array([7800, 7800, 7800, 7800, 9000, 10800, 13200, 14100, 15300, 16500, 17700, 22900,
                             25900, 29700, 32400, 35700, 37800, 39600, 42000, 43800, 45000, 48000, 51300, 53400, 55500,
                             57600, 60600, 61200, 62700, 65400, 68400, 72600, 76200, 80400, 84900, 87000, 87900, 90000,
                             94200, 97500, 102000, 106800, 106800, 106800, 110100, 113700, 117000, 118500, 118500,
                             127200, 128400, 132900, 137700, 142800, 147000, 160,200])
    total = 0
    for i in range(1, 36):
        newAmount = (awi[-1] / awi[-i]) * maxEarnings[-i]
            if newAmount > maxEarnings[-i]:
            newAmount = maxEarnings[-i]
        total += newAmount
    '''
    # The following assumes the salary is the same all 35 years of consideration for social security consideration
    pia = 0
    aime = (162200 if salary > 162200 else salary) / 12

    '''
    Primary Insurance Amount (PIA) Formula
    https://www.ssa.gov/oact/COLA/piaformula.html
    '''
    
    # Top threshold of .15
    if aime > 6172:
        aime -= 6172
        pia += (2568 + aime * .15)
    # Middle threshold of .32
    elif aime > 1024:
        aime -= 1024
        pia += (921.6 + aime * .32)
    # Bottom threshold of .9
    else:
        pia += (aime * .9)
    return pia * 12 * ssifactor(benefitsElection)

'''
Benefit factor for early or delayed retirement
https://www.ssa.gov/oact/ProgData/ar_drc.html
'''
def ssifactor(benefitsElection):
    # Calculated in months, 804 = 12 * 67 or full retirement age where benefits are 100%
    # Difference is the number of months from the full returment age to the elected retirement age
    retirementDiff = (benefitsElection - 67) * 12
    factor = 1

    # Early retirement
    if retirementDiff < 0:
        if retirementDiff < -36:
            # First 36 months is at 5/9% per month so 36 months = -.2
            retirementDiff += 36
            factor -= .2

            # Second 24 months is at 5/12% per month so 24 months = -.1
            # Minimum factor of .7
            factor += (retirementDiff * 5 / 1200)
        else:
            factor += (retirementDiff * 5 / 900)

    # Delayed retirement
    elif retirementDiff > 0:
        # Delayed retirement is at 2/3% per month so 36 months = .24
        factor += retirementDiff * 2 / 300
    return factor

'''
Cost of Living Adjustments (COLA)

Yearly inflation adjustments based on CPI-W 
historicalColas = {1975 : 8.0, 1976	: 6.4, 1977	: 5.9, 1978	: 6.5, 1979 : 9.9, 1980	: 14.3, 1981 : 11.2, 1982 : 7.4,
                   1983	: 3.5, 1984	: 3.5, 1985	: 3.1, 1986	: 1.3, 1987	: 4.2, 1988	: 4.0, 1989	: 4.7, 1990 : 5.4,
                   1991	: 3.7, 1992	: 3.0, 1993 : 2.6, 1994	: 2.8, 1995	: 2.6, 1996	: 2.9, 1997	: 2.1, 1998	: 1.3,
                   1999   : 2.5, 2000 : 3.5, 2001	: 2.6, 2002	: 1.4, 2003	: 2.1, 2004	: 2.7, 2005	: 4.1, 2006	: 3.3,
                   2007	: 2.3, 2008	: 5.8, 2009	: 0.0, 2010	: 0.0, 2011	: 3.6, 2012	: 1.7, 2013	: 1.5, 2014	: 1.7,
                   2015	: 0.0, 2016	: 0.3, 2017	: 2.0, 2018	: 2.8, 2019	: 1.6, 2020	: 1.3, 2021	: 5.9}
totalCola = 0
for cola in historicalColas:
    totalCola += historicalColas[cola]
print(totalCola/len(historicalColas))
Assume COLA of 2.5% per year (historical average) ^ 8 = 1.218 factor of age 62 vs 70 * 1.24/.7 = 1.77 * 1.218 = 2.158 factor
'''