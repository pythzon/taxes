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
def getEitc(agi, maritalStatus, dependents, maxContributions):
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
