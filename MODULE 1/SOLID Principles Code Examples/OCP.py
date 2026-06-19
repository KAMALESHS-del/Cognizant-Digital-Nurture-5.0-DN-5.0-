class Payment:

    def pay(self, payment_type, amount):

        if payment_type == "UPI":
            print(f"Paid ₹{amount} using UPI")

        elif payment_type == "Card":
            print(f"Paid ₹{amount} using Card")

        elif payment_type == "Wallet":
            print(f"Paid ₹{amount} using Wallet")


payment = Payment()

payment.pay("UPI", 1000)
payment.pay("Card", 2000)
payment.pay("Wallet", 500)