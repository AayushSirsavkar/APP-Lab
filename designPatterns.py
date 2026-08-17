# Payment Strategy Interface
class PaymentStrategy:
    def pay(self, amount):
        pass


# Credit Card Payment Strategy
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")


# PayPal Payment Strategy
class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using PayPal.")


# Bitcoin Payment Strategy
class BitcoinPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Bitcoin.")


# Payment Processor
class PaymentProcessor:
    def __init__(self, strategy):
        self.strategy = strategy

    # Switch strategy at runtime
    def set_strategy(self, strategy):
        self.strategy = strategy

    # Process payment
    def process_payment(self, amount):
        self.strategy.pay(amount)


# Main Program
def main():

    # Start with Credit Card
    processor = PaymentProcessor(CreditCardPayment())
    processor.process_payment(1000)

    # Switch to PayPal
    processor.set_strategy(PayPalPayment())
    processor.process_payment(2000)

    # Switch to Bitcoin
    processor.set_strategy(BitcoinPayment())
    processor.process_payment(3000)


if __name__ == "__main__":
    main()
