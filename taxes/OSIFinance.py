# TODO Would it be best to execute this code before stateTaxes?
# Fix Kansas
# Massachusetts taxes long term gains as income and has a higher tax for short term capital gains
# if state == ('Alabama' or 'Arizona' or 'California' or 'Colorado' or 'Delaware' or 'Georgia' or 'Idaho' or
#                 'Illinois' or 'Indiana' or 'Iowa' or 'Kansas' or 'Kentucky' or 'Louisiana' or 'Maine' or 'Maryland' or
#                 'Michigan' or 'Minnesota' or 'Mississippi' or 'Missouri' or
#                 'Montana' or 'Nebraska' or 'New Jersey' or 'New York' or 'New Mexico' or 'North Carolina' or
#                 'North Dakota' or 'Ohio' or 'Oklahoma' or 'Oregon' or 'Pennsylvania' or 'Rhode Island' or 'Utah' or
#                 'Virginia' or 'West Virginia' or 'Wisconsin' or 'District of Columbia'):
#     pass

class OSIFinance():

    def __init__(self, agi=0, maritalStatus=0, dependents=0, federalDeductions=0, resState='None', workState='None', stateDeductions=0, shortCapitalGains=0, longCapitalGains=0, socialSecurityBenefits=0, socialSecurityElectionAge=0, age=0):
        self.agi = agi
        self.maritalStatus = maritalStatus
        self.dependents = dependents
        self.federalDeductions = federalDeductions
        self.resState = resState
        self.workState = workState
        self.stateDeductions = stateDeductions
        self.shortCapitalGains = shortCapitalGains
        self.longCapitalGains = longCapitalGains
        self.socialSecurityBenefits = socialSecurityBenefits
        self.socialSecurityElectionAge = socialSecurityElectionAge
        self.age = age

    def federalTaxes():
        pass

    # @staticmethod
    # def getState(state):
    #     return globals()[state]()    

    def stateTaxes(agi, resState):
        __import__(resState)
        print(resState)
        print(agi)
        # resState = __import__(resState)

        print(resState())

    def capitalGainsTaxes():
        pass

    def socialSecurityTaxes():
        pass


# OSIFinance.stateTaxes()
# OSIFinance.stateTaxes(agi=10000, resState='illinois')
print(OSIFinance.stateTaxes(agi=10000, resState='illinois'))
    