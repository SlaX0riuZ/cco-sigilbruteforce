import dictkeep

class createCube:
    def __init__(self, initialprice, tallycap, prefixarray, sigilslots, divbaseincrease, divpricemultiplier, coldivpricemultiplier, coldivpriceaddition): # assume cube ALWAYS has maximum tallies
        # Initialize variables that are force-filled on creation
        self.initialprice = initialprice
        self.tallycap = tallycap
        self.prefixarray = prefixarray
        self.sigilslots = sigilslots
        self.divbaseincrease = divbaseincrease
        self.divpricemultiplier = divpricemultiplier
        self.coldivpricemultiplier = coldivpricemultiplier
        self.coldivpriceaddition = coldivpriceaddition
        # Initialize cube's base sigil array
        self.sigilarray=[]
        for i in range(sigilslots):
            self.sigilarray.append('empty')
    
    def __str__(self):
        pass # fill later