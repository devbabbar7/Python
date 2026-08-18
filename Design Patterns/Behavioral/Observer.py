from abc import ABC, abstractmethod


# ==========================================
# 1. OBSERVER INTERFACE (Subscriber)
# ==========================================
class Observer(ABC):
    """
    The Observer interface declares the notification method used by subjects.
    """
    @abstractmethod
    def update(self, stock_symbol: str, price: float) -> None:
        pass


# ==========================================
# 2. SUBJECT INTERFACE & CONCRETE SUBJECT (Publisher)
# ==========================================
class Subject(ABC):
    """
    The Subject interface declares methods for managing subscribers.
    """
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class StockTicker(Subject):
    """
    The Concrete Subject tracks state (price) and sends notifications
    to all registered observers whenever state changes.
    """
    def __init__(self, symbol: str):
        self.symbol = symbol
        self._price: float = 0.0
        self._observers: list[Observer] = []

    def attach(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self.symbol, self._price)

    def set_price(self, new_price: float) -> None:
        print(f"\n[Ticker] {self.symbol} price updated to ${new_price:.2f}")
        self._price = new_price
        self.notify()  # Automatically triggers broadcasts


# ==========================================
# 3. CONCRETE OBSERVERS (Subscribers)
# ==========================================
class EmailAlertListener(Observer):
    def __init__(self, email: str):
        self.email = email

    def update(self, stock_symbol: str, price: float) -> None:
        print(f"[Email Alert -> {self.email}] {stock_symbol} is now ${price:.2f}")


class MobileAppDisplay(Observer):
    def __init__(self, user_name: str):
        self.user_name = user_name

    def update(self, stock_symbol: str, price: float) -> None:
        print(f"[Mobile Push -> {self.user_name}] {stock_symbol} updated: ${price:.2f}")


# ==========================================
# 4. CLIENT EXECUTION
# ==========================================
if __name__ == "__main__":
    # Create Publisher
    apple_stock = StockTicker("AAPL")

    # Create Subscribers
    user1_email = EmailAlertListener("alice@example.com")
    user2_phone = MobileAppDisplay("Bob")

    # Attach Subscribers
    apple_stock.attach(user1_email)
    apple_stock.attach(user2_phone)

    # State Change 1: Both subscribers get notified
    apple_stock.set_price(182.50)

    # Unsubscribe Alice
    print("\n--- Alice unsubscribes ---")
    apple_stock.detach(user1_email)

    # State Change 2: Only Bob gets notified
    apple_stock.set_price(185.00)