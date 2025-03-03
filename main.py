import dictkeep

class createCube:
    def __init__(self, initialprice, tallycap, prefixarray, rarity, sigilslots): # assume cube ALWAYS has maximum tallies
        self.initialprice = initialprice
        self.tallycap = tallycap
        self.prefixarray = prefixarray
        self.rarity = rarity
        self.sigilslots = sigilslots
        self.sigilarray=[]
        for i in range(sigilslots):
            self.sigilarray.append('empty')
    
    def __str__(self):
        return f'Base Price: {self.initialprice}, Tally Cap: {self.tallycap}, Prefix Array: {self.prefixarray}\nRarity: {self.rarity}, Sigil Slots: {self.sigilarray}'
    
    

testcube1 = createCube(65000, 15000, [45], "relic", 5) # example of tallying relic cube, 1x prefixes
testcube2 = createCube(139222, -1, [79, 13], "cubic", 5) # example of cubic cube, 2x prefixes
testcube3 = createCube(1290284, 250000, [-1], "gold", 5) # example of tallying gold cube, 0x prefixes

print(testcube1)