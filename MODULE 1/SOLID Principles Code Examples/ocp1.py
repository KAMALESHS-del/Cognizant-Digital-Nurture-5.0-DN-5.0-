from abc import ABC, abstractmethod
# Abstract Class
class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# UPI Payment
class UPIPayment(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


# Card Payment
class CardPayment(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Card")


# Wallet Payment
class WalletPayment(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Wallet")
# Create Objects
upi = UPIPayment()
card = CardPayment()
wallet = WalletPayment()

# Make Payments
upi.pay(1000)
card.pay(2000)
wallet.pay(500)