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
        self.baseprice, self.tallycap, self.prefixarray = baseprice, tallycap, prefixarray
        self.materialcount, self.sigilslots, self.rarity, self.bsidebool = materialcount, sigilslots, rarity, bsidebool

        self.sigilarray=[]
        for i in range(self.sigilslots):
            self.sigilarray.append('empty')
            
        self.tallymultiplier = 24 if self.bsidebool else 6 # Sets tally multi to 24 if it's b-side; else default to 6
        self.bsidepricemult = 16 if self.bsidebool else 1 # Sets the b-side price mult to 16 if it's b-side, else makes it 1 (does nothing)
    
    def __repr__(self):
        return f'Base Price: {self.baseprice}, Tally Cap: {self.tallycap}, Sigil List: {self.sigilarray}'
    
    def addSigil(self, sigilname, sigiltier):
        for i in range(len(self.sigilarray)):
            if self.sigilarray[i] == 'empty':
                self.sigilarray[i] = [sigilname,sigiltier]
                break



# Test Cube 1: Tallying Glitchy Hypnotic Emburdening Parfait Cube
testcube1 = createBaseCube(7099605, 999999999, [76,8,122], 13, 3, 'crafted', 0)

# Test Cube 2: Tallying B-Side Crust Cube
testcube2 = createBaseCube(139222, 150000, [-1], 2, 7, 'cubic', 1)

# Test Cube 3: XX - The Sun
testcube3 = createBaseCube(250000, -1, [-1], 2, 5, 'cubic', 0)

print(testcube1)
testcube1.addSigil('dice',4)
print(testcube1)


