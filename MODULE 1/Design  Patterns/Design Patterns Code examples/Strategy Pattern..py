class UPI:

    def pay(self, amount):
        print("Paid", amount, "using UPI")


class Card:

    def pay(self, amount):
        print("Paid", amount, "using Card")


upi = UPI()
upi.pay(1000)

card = Card()
card.pay(2000)