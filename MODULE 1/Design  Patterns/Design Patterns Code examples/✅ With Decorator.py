class cofee():
    def cost(self):
        return 50
class milkcofee():
    def __init__(self,cofee):
        self.cofee=cofee
    def milk(self):
        return self.cofee.cost()+20
cof=cofee()
milk=milkcofee(cof)
milk=(milk.milk())
print("milkcofeeprice:",milk)     
            