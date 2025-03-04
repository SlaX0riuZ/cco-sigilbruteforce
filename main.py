import dictkeep

# Required Variables:
'''Base (Non-Col):

-> Base Price
-> Tally Cap (set to -1 if it doesn't exist)
-> Prefix Array (set to [-1] if there aren't prefixes)
-> B-Side Boolean to mark if cube is b-side (use True/False)
-> Number of base materials
-> Number of sigil slots
-> Cube's rarity

'''

class createBaseCube():
    def __init__(self, baseprice, tallycap, prefixarray, materialcount, sigilslots, rarity, bsidebool):
        self.baseprice = baseprice
        self.tallycap = tallycap
        self.prefixarray = prefixarray
        self.materialcount = materialcount
        self.sigilslots = sigilslots
        self.rarity = rarity
        self.bsidebool = bsidebool
        
        if self.bsidebool:
            self.tallymultiplier = 24
        else:
            self.tallymultiplier = 6
