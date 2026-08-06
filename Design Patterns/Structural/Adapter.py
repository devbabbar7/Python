from abc import ABC, abstractmethod

# 1. Target Interface
class PaymentProcessor(ABC):
    """
    The Target defines the domain-specific interface used by the client code.
    """
    @abstractmethod
    def process_payment(self, amount_in_dollars: float) -> None:
        pass


# Standard implementation matching our Target interface
class StripeProcessor(PaymentProcessor):
    def process_payment(self, amount_in_dollars: float) -> None:
        print(f"[Stripe] Charged ${amount_in_dollars:.2f} successfully.")


# 2. Adaptee
class LegacyPayPalAPI:
    """
    The Adaptee contains useful behavior, but its interface is incompatible
    with existing client code (uses cents and a different method name).
    """
    def make_transaction(self, amount_in_cents: int) -> None:
        print(f"[Legacy PayPal API] Transaction processed for {amount_in_cents} cents.")


# 3. Adapter
class PayPalAdapter(PaymentProcessor):
    """
    The Adapter makes the Adaptee's interface compatible with the Target's interface.
    """
    def __init__(self, legacy_paypal: LegacyPayPalAPI):
        self._legacy_paypal = legacy_paypal

    def process_payment(self, amount_in_dollars: float) -> None:
        # 1. Convert dollars to cents (Unit adaptation)
        amount_in_cents = int(amount_in_dollars * 100)
        # 2. Call the incompatible method (Method adaptation)
        self._legacy_paypal.make_transaction(amount_in_cents)


# --- Client Code ---
if __name__ == "__main__":
    def checkout(processor: PaymentProcessor, amount: float):
        # Client code interacts strictly with PaymentProcessor
        processor.process_payment(amount)

    # 1. Regular processor (no adapter needed)
    stripe = StripeProcessor()
    checkout(stripe, 25.50)
    # Output: [Stripe] Charged $25.50 successfully.

    # 2. Incompatible processor (wrapped in Adapter)
    legacy_paypal = LegacyPayPalAPI()
    adapted_paypal = PayPalAdapter(legacy_paypal)
    checkout(adapted_paypal, 25.50)
    # Output: [Legacy PayPal API] Transaction processed for 2550 cents.