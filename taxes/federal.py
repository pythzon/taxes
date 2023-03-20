class Federal: 
    # def __init__(self, agi, dependents, maritalStatus, federalDeductions=0):
    #     self.agi = agi
    #     self.dependents = dependents
    #     self.maritalStatus = maritalStatus
    #     self.federalDeductions = federalDeductions
    #     self.taxes = 0
    #     self.margin = 0
    #     self.federalBracket = 0

    def tax(salary, maritalStatus, resState="Alaska", workState="Alaska", federalDeductions=0, stateDeductions=0, federalCredits=0, stateCredits=0, longTermCapitalGains=0, shortTermCapitalGains=0, capitalLosses=0, dependents=0, resCounty=None, age=0):
        '''
        ALL OF THE FOLLOWING IS UPDATED FOR THE 2023 TAX YEAR
        STANDARD DEDUCTIONS FOR THOSE UNDER AGE 65 -> https://www.irs.gov/newsroom/irs-provides-tax-inflation-adjustments-for-tax-year-2023
        MARRIED FILING JOINTLY -> $27,700
        HEAD OF HOUSEHOLD -> $20,800
        SINGLE OR MARRIED FILING SEPERATELY -> $13,850

        FOR THOSE AGE 65 AND OLDER -> https://www.irs.gov/taxtopics/tc551
        TABLE 7 
        MARRIED FILING JOINTLY -> $30,700
        Head of Household -> $23,650
        SINGLE -> $15,700
        MARRIED FILING SEPERATELY -> $15,350

        FICA TAX RATES -> https://www.ssa.gov/oact/cola/cbb.html
        SOCIAL SECURITY -> 6.2% of gross salary up to $160,200
        MEDICARE -> 1.45% of gross salary 

        ADDITIONAL .9% MEDICARE TAX THRESHOLDS -> https://www.irs.gov/taxtopics/tc560#:~:text=A%200.9%25%20Additional%20Medicare%20Tax,%24200%2C000%20for%20all%20other%20taxpayers.
        MARRIED FILING JOINTLY -> $200,000
        MARRIED FILING SEPERATELY -> $125,000
        ALL OTHERS -> $200,000
        '''
        import numpy as np
        # TODO implememnt the following
        resCounty = False
        stateCredits = 0
        dependents = 0 
        # Up to $3000 from capital losses
        # maxCapitalLosses = 0

        if maritalStatus == "Married":
            if federalDeductions == 0:
                if age < 65:
                    federalDeductions = 27700
                else:
                    federalDeductions = 30700
            upperRoth, lowerRoth, upperTradIra, lowerTradIra, medicareThreshold = 228000, 218000, 136000, 116000, 250000
        else:
            if federalDeductions == 0:
                if maritalStatus == "Single":
                    if age < 65:
                        federalDeductions = 13850
                    else:
                        federalDeductions = 15700
                # Head of household standard deduction
                else:
                    if age < 65:
                        federalDeductions = 20800
                    else:
                        federalDeductions = 23000
            upperRoth, lowerRoth, upperTradIra, lowerTradIra, medicareThreshold = 153000, 138000, 83000, 73000, 200000
            if maritalStatus == "Married Filing Separately":
                medicareThreshold = 125000

        # Social Security Tax is set to the max ($160,200 * 6.2% ) and then reduced if lower than the max
        socialSecurityTax = 9932.4
        # The following are for the additional medicare tax for high earners
        if salary < medicareThreshold:
            if salary < 160200:
                socialSecurityTax = salary * .062
            medicareTax = salary * .0145
        else:
            medicareTax = (medicareThreshold - salary) * .0145 + (salary - medicareThreshold) * .009
        # AGI is used as an argument for federal and state functions
        agi = salary - federalDeductions

        # First calculates federal income taxes since this information is used for some state taxes as a deduction
        federalTaxes, federalBracket, federalMargin = federalIncomeTaxes(agi, maritalStatus)

        # Determines the jurisdictions in which state taxes are paid, 17 states only look at the state of residence, while
        # the others have you pay the total amount of whichever state is higher
        resState, workState = statereciprocity(resState, workState)
        # If different, then the higher tax is used per the tax standard of paying the lower amount plus the difference
        if resState != workState:
            resStateTaxes, resStateBracket, resStateMargin = statetaxes(resState, resCounty, agi, maritalStatus, federalTaxes, stateDeductions, stateCredits, dependents)
            # The second case is for the workState
            stateTaxes, stateBracket, stateMargin = statetaxes(workState, resCounty, agi, maritalStatus, federalTaxes, stateDeductions, stateCredits, dependents)
            # If resState is greater than the state amount used is the resState, so stateTaxes is updated
            if resStateTaxes > stateTaxes:
                stateTaxes, stateBracket, stateMargin = resStateTaxes, resStateBracket, resStateMargin
                # TODO: Sets it to the workstate for margin purposes, could possibly switch back?
                resState = workState
        # If the previous condition wasn't met, the individual works and resides in the same state
        else:
                stateTaxes, stateBracket, stateMargin = statetaxes(resState, resCounty, agi, maritalStatus, federalTaxes, stateDeductions, stateCredits, dependents)
        # Local bracket included in stateTaxes and hence stateBracket, does not include Social Secuirty and Medicare taxes as those are witheld from salary
        # TODO: PV of annuitized payments, or a quarterly tax discount form investing before paying quarterly taxes
        # fedAndStateTaxes = (federalTaxes + stateTaxes) * (4 / (((1 + apyTod) ** 4 - 1) / (apyTod ** .25)))
        fedAndStateTaxes = federalTaxes + stateTaxes
        # Receives credits on Jan 1st (filing as soon as possible),
        payAfterTaxes = salary - socialSecurityTax - medicareTax - fedAndStateTaxes + federalCredits + stateCredits
        bracket = np.array([1 - (federalBracket + stateBracket)])
        return payAfterTaxes, federalTaxes, stateTaxes, bracket, federalMargin, stateMargin, resState, workState, socialSecurityTax, medicareTax, fedAndStateTaxes, savings

    # ENTIRE TAX BOUND ARRAYS ARE USED FOR TRADITIONAL 401(K) AND IRA WITHDRAWALS
    def taxBounds(maritalStatus):
        import numpy as np
        # 2023 TAX YEAR
        brackets = np.array([0, .1, .12, .22, .24, .32, .35, .37])
        thresholds = {"Married":np.array([0, 22000, 89450, 190750, 364200, 462500, 693750, float('inf')]),
                        "Single": np.array([0, 11000, 44725, 95375, 182100, 231250, 578125, float('inf')]),
                        "Head of Household": np.array([0, 15700, 59850, 95350, 182100, 231250, 578100, float('inf')])}
        return thresholds[maritalStatus], brackets

    # Calculates AGI to determine taxes and tax bracket initially and for subsequent calculations
    def federalIncomeTaxes(agi, maritalStatus):
        #Margin set to a high number so it doesnt affect the lowest earners who can't cross tax brackets
        margin = 999999
        thresholds, brackets = taxBounds(maritalStatus)
        taxes = 0
        for i in range(1, 8):
            bracket = brackets[i]
            if agi < thresholds[i]:
                # In these cases the margin is changed, otherwise the user cant go to a lower tax bracket
                if i >= 2:
                    margin = agi - thresholds[i-1]
                    taxes += margin * bracket
                # In inital case, the margin is unchanged and agi is used to calculate taxes
                # TODO: Verify change
                else:
                    taxes += agi * bracket
                return taxes, bracket, margin
            else:
                taxes += (thresholds[i] - thresholds[i-1]) * brackets[i]
        return taxes, bracket, margin

    '''
    Only applies to TOD

    Capital Gains -> https://www.irs.gov/taxtopics/tc409
    Rate      Married Filing Jointly    Single                    Head of Household 
    0%        Up to $83,350             Up to $41,675             Up to $55,800
    15%       $83,350 - $517,200        $41,675 - $459,750        $55,800 - $488,500
    20%       In excess of $517,200     In excess of $459,750     In excess of $488,500

    Net Investment Income Tax (NIIT) -> https://www.irs.gov/taxtopics/tc559
    3.8% additional tax on net investment income for taxpayers with modified adjusted gross income (MAGI) above the following thresholds:
            Married Filing Jointly     Single or Head of Household     Married Filing Separately
    Thresholds  $250,000                   $200,000                        $125,000
    '''

    # !Calc long term probabilities of being in various thresholds
    def investmenttaxes(agi, longCapitalGains, shortCapitalGains, maritalStatus, state):
        import numpy as np
        taxes, niitTax, margin = 0, .038, 9999999
        niitThresholds = {'Married': 250000, 'Head of Household': 200000, 'Single': 200000, 'Married Filing Separately': 125000}
        highestGainsThresholds = {'Married': 517200, 'Head of Household': 488500, 'Single': 459750}
        lowestGainsThresholds = {'Married': 83350, 'Head of Household': 55800, 'Single': 41675}

        investmentBounds = np.array([lowestGainsThresholds[maritalStatus], niitThresholds[maritalStatus], highestGainsThresholds[maritalStatus], float('inf')])
        investmentBrackets = np.array([0, .15, .188, .238])

        # Incorporate short TERM capital gains
        # first checks niit threshold
        if agi + longCapitalGains > niitThresholds[maritalStatus]:
            # then checks capital gains threshold
            if longCapitalGains > highestGainsThresholds[maritalStatus]:
                # next check if only investment income or the difference is taxable for niit
                if agi > niitThresholds[maritalStatus]:
                    # 3.8% of the total plus capital gains rate plus capital gains brackets
                    margin = agi - niitThresholds[maritalStatus]
                    taxes = niitTax * longCapitalGains + (highestGainsThresholds[maritalStatus] - lowestGainsThresholds[maritalStatus] * .15) + margin * .2
                else:
                    taxes = ((longCapitalGains + agi - niitThresholds[maritalStatus]) * niitTax) + (longCapitalGains * .2)
            elif longCapitalGains > lowestGainsThresholds[maritalStatus]:
                if agi > niitThresholds[maritalStatus]:
                    # 15% + 3.8% for this case
                    taxes = niitTax * longCapitalGains + (agi - niitThresholds[maritalStatus])
                else:
                    taxes = ((longCapitalGains + agi - niitThresholds[maritalStatus]) * niitTax) + (longCapitalGains * .15)
            else:
                if agi > niitThresholds[maritalStatus]:
                    # only niit tax for this case
                    taxes = niitTax * longCapitalGains
                else:
                    taxes = ((longCapitalGains + agi - niitThresholds[maritalStatus]) * niitTax)
        # No NIIT in this case
        else:
            # No taxes if this condition is not met
            if longCapitalGains > lowestGainsThresholds[maritalStatus]:
                margin = longCapitalGains - lowestGainsThresholds[maritalStatus]
                taxes = margin * .15

    # Contributions for all tax-advantaged accounts (401k, IRA). Checks if possible given maximum allocations
    def getSavers(agi, maritalStatus, maxContributions, contributions):
        import numpy as np
        margin = 999999
        brackets = np.array([.1, .2, .5])
        # $4000 is max matched contributions and is used for married couples
        if maritalStatus == 'Married':
            maxMatched = 4000
            thresholds = np.array([73000, 54750, 43500])
        # $2000 is max for non-married couples
        else:
            maxMatched = 2000
            if maritalStatus == 'Head of Household':
                thresholds = np.array([54750, 35625, 32625])
            # marital status Single
            else:
                thresholds = np.array([36500, 23750, 21750])
        if agi - maxContributions > thresholds[0]:
            # Returns 0 since savers cannot be considered
            return 0, False
        
        # Savers is possible but currently above max threshold
        elif agi > thresholds[0]:
            thresholds = agi - thresholds
            return True, thresholds
            
        # Sets the bracket for calculations
        elif agi < thresholds[2]:
            bracket = brackets[2]
            thresholds = agi - thresholds[1:]

        elif agi < thresholds[1]:
            bracket = brackets[1]
            thresholds = agi - thresholds[2]

        else:
            bracket = brackets[0]
            thresholds = False

        if contributions > maxMatched:
            # Max bonus category, no further checking
            saversBonus = maxMatched * bracket
        else:
            saversBonus = contributions * bracket

        return saversBonus, thresholds

    # Calculates current bonus amount and the distance to the bonus threshold
    def getEic(agi, maritalStatus, dependents, maxContributions):
        maxAgiMarried = [24210, 53120, 59478, 63698]
        maxAgi = [17640, 46560, 52918, 56838]
        credits = [600, 3995, 6604, 7430]
        if dependents > 3:
            dependents = 3
        if maritalStatus == 'Married':
            # Cannot be reached
            if agi - maxContributions > maxAgiMarried[dependents]:
                return 0, False
            # Returns margin
            elif agi > maxAgiMarried[dependents]:
                return 0, agi - maxAgiMarried[dependents]
        # Single or HoH for this case
        else:
            # Cannot be reached
            if agi - maxContributions > maxAgi[dependents]:
                return 0, False
            # Returns margin
            elif agi > maxAgi[dependents]:
                return 0, agi - maxAgi[dependents]
        # If none of the disqualifying conditions are met, the credit is given and never changes so margin is set to max
        return credits[dependents], 999999
