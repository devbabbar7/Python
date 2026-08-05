from abc import ABC, abstractmethod

'''
Step 0: Create Product interface abstract class
'''

# 1. Abstract Product Interface
class Notification(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        """Every notification channel MUST implement this method."""
        pass

'''
Step 1: Create your products
These are the actual objects you want to use.
'''

class EmailNotification(Notification):
    def send(self, message: str):
        print(f"Sending EMAIL: {message}")

class SMSNotification(Notification):
    def send(self, message: str):
        print(f"Sending SMS: {message}")

'''
Step 2: Create a Base Creator Class
This class has two main parts:

The Factory Method (create_notification): An empty method that subclasses must override.

The Business Logic (send_alert): The actual work that uses the created object.
'''

class NotificationSender(ABC):
    
    @abstractmethod
    def create_notification(self):
        pass

    def send_alert(self, message: str):
        # 1. Call the factory method to get the object
        notification = self.create_notification()
        
        # 2. Use the object
        notification.send(message)

'''
Step 3: Create Subclasses that implement the Factory Method
Each subclass overrides create_notification to return its specific object.
'''

class EmailSender(NotificationSender):
    def create_notification(self):
        # Subclass decides to make an EmailNotification
        return EmailNotification()

class SMSSender(NotificationSender):
    def create_notification(self):
        # Subclass decides to make an SMSNotification
        return SMSNotification()


'''
Why go through all this trouble?
Imagine next month we are told: "Add WhatsApp notifications!"

Without Factory Method: You would have to open your core NotificationManager file, risk breaking old code, and edit if channel == "whatsapp": ....

With Factory Method: You don't touch ANY existing code. You just add two new classes:
'''

# 1. New product
class WhatsAppNotification(Notification):
    def send(self, message: str):
        print(f"Sending WHATSAPP: {message}")

# 2. New creator
class WhatsAppSender(NotificationSender):
    def create_notification(self):
        return WhatsAppNotification()

'''
Step 4: Use it in your app
Now, your main application doesn't care how a notification is created or what specific class it is—it just calls send_alert().
'''
if __name__ == "__main__":
    # Want to send an email? Use the EmailSender creator:
    sender = EmailSender()
    sender.send_alert("Your order has shipped!")
    # Output: Sending EMAIL: Your order has shipped!

    # Want to send an SMS? Just swap the sender:
    sender = SMSSender()
    sender.send_alert("Your OTP is 1234")
    # Output: Sending SMS: Your OTP is 1234

    # New addition to code
    sender = WhatsAppSender()
    sender.send_alert("Your OTP is 1234")