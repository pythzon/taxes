'''
WASHINGTON CAPITAL GAINS TAXES
https://dor.wa.gov/taxes-rates/other-taxes/capital-gains-tax
7% of net capital gains over $250,000
'''

class Washington:
    if netCapitalGains > 250000:
        taxes = (netCapitalGains - 250000) * .07