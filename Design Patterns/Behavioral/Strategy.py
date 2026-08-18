from __future__ import annotations
from abc import ABC, abstractmethod


# ==========================================
# 1. STRATEGY INTERFACE
# ==========================================
class PaymentStrategy(ABC):
    """
    The Strategy interface declares operations common to all supported
    versions of the algorithm.
    """
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass


# ==========================================
# 2. CONCRETE STRATEGIES
# ==========================================
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number: str, cvv: str):
        self.card_number = card_number
        self.cvv = cvv

    def pay(self, amount: float) -> None:
        masked = self.card_number[-4:]
        print(f"[Credit Card] Paid ${amount:.2f} using card ending in **{masked}")


class PayPalPayment(PaymentStrategy):
    def __init__(self, email: str):
        self.email = email

    def pay(self, amount: float) -> None:
        print(f"[PayPal] Paid ${amount:.2f} via PayPal account: {self.email}")


class CryptoPayment(PaymentStrategy):
    def __init__(self, wallet_address: str):
        self.wallet_address = wallet_address

    def pay(self, amount: float) -> None:
        print(f"[Crypto] Paid ${amount:.2f} to Wallet: {self.wallet_address[:6]}...{self.wallet_address[-4:]}")


# ==========================================
# 3. CONTEXT
# ==========================================
class ShoppingCart:
    """
    The Context maintains a reference to one of the Strategy objects
    and communicates with it solely through the Strategy interface.
    """
    def __init__(self) -> None:
        self._items: list[tuple[str, float]] = []
        self._payment_strategy: PaymentStrategy | None = None

    def add_item(self, item_name: str, price: float) -> None:
        self._items.append((item_name, price))
        print(f"Added '{item_name}' (${price:.2f}) to cart.")

    def set_payment_strategy(self, strategy: PaymentStrategy) -> None:
        self._payment_strategy = strategy

    def checkout(self) -> None:
        if not self._payment_strategy:
            raise ValueError("Please select a payment method before checkout.")

        total = sum(price for _, price in self._items)
        print(f"\n--- Processing Order: Total ${total:.2f} ---")
        self._payment_strategy.pay(total)
        self._items.clear()  # Empty cart after checkout


# ==========================================
# 4. CLIENT EXECUTION
# ==========================================
if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("Mechanical Keyboard", 120.00)
    cart.add_item("Gaming Mouse", 60.00)

    # 1. Pay with Credit Card
    cart.set_payment_strategy(CreditCardPayment("1234-5678-9876-5432", "123"))
    cart.checkout()

    # 2. Add another item and switch payment strategy dynamically at runtime
    cart.add_item("USB-C Hub", 35.00)
    cart.set_payment_strategy(PayPalPayment("alex@example.com"))
    cart.checkout()