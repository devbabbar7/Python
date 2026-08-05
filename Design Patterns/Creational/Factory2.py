from __future__ import annotations
from abc import ABC, abstractmethod


# -------------------------------------------------------------------
# 1. ABSTRACT PRODUCT INTERFACE
# -------------------------------------------------------------------
class Notification(ABC):
    """
    The Product interface declares operations that all concrete products
    must implement.
    """
    @abstractmethod
    def send(self, message: str) -> str:
        pass


# -------------------------------------------------------------------
# CONCRETE PRODUCTS
# -------------------------------------------------------------------
class EmailNotification(Notification):
    def send(self, message: str) -> str:
        return f"Sending EMAIL with payload: '{message}'"


class SMSNotification(Notification):
    def send(self, message: str) -> str:
        return f"Sending SMS with payload: '{message}'"


class WhatsAppNotification(Notification):
    def send(self, message: str) -> str:
        return f"Sending WHATSAPP with payload: '{message}'"


# -------------------------------------------------------------------
# 2. ABSTRACT CREATOR CLASS
# -------------------------------------------------------------------
class NotificationSender(ABC):
    """
    The Creator class declares the factory method (create_notification).
    Its primary responsibility is executing core business logic (send_alert)
    that relies on Product objects returned by the factory method.
    """
    @abstractmethod
    def create_notification(self) -> Notification:
        """The Factory Method."""
        pass

    def send_alert(self, message: str) -> str:
        # 1. Call the factory method to create a Product object.
        notification = self.create_notification()

        # 2. Use the product via its abstract interface.
        result = f"NotificationSender Core Logic -> {notification.send(message)}"
        return result


# -------------------------------------------------------------------
# CONCRETE CREATORS
# -------------------------------------------------------------------
class EmailSender(NotificationSender):
    def create_notification(self) -> Notification:
        return EmailNotification()


class SMSSender(NotificationSender):
    def create_notification(self) -> Notification:
        return SMSNotification()


class WhatsAppSender(NotificationSender):
    def create_notification(self) -> Notification:
        return WhatsAppNotification()


# -------------------------------------------------------------------
# 3. CLIENT CODE
# -------------------------------------------------------------------
def client_code(sender: NotificationSender, message: str) -> None:
    """
    The client code works with an instance of a concrete creator via its base
    interface (NotificationSender). 

    The client DOES NOT KNOW which concrete notification type will be created.
    Subclasses alter the product type under the hood.
    """
    print(f"Client: I don't know which sender this is, but it works:\n"
          f"{sender.send_alert(message)}\n")


# -------------------------------------------------------------------
# EXECUTION
# -------------------------------------------------------------------
if __name__ == "__main__":
    print("App: Configured with EmailSender.")
    client_code(EmailSender(), "Your order has shipped!")

    print("App: Configured with SMSSender.")
    client_code(SMSSender(), "Your OTP is 1234")

    print("App: Configured with WhatsAppSender.")
    client_code(WhatsAppSender(), "Your appointment is confirmed.")