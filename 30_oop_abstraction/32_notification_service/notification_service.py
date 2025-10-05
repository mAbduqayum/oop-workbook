from abc import ABC, abstractmethod
from datetime import datetime


class NotificationService(ABC):
    def __init__(self, service_name) -> None:
        self.service_name = service_name
        self.sent_count = 0

    @abstractmethod
    def validate_recipient(self, recipient):
        pass

    @abstractmethod
    def send(self, recipient, message):
        pass

    @abstractmethod
    def get_cost(self):
        pass

    def log_notification(self, recipient, status):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {self.service_name}: {recipient} - {status}")
        if status == "SUCCESS":
            self.sent_count += 1


class EmailNotification(NotificationService):
    def __init__(self) -> None:
        super().__init__("Email Service")

    def validate_recipient(self, recipient):
        return "@" in recipient

    def send(self, recipient, message):
        if not self.validate_recipient(recipient):
            self.log_notification(recipient, "FAILED")
            return False

        print(f"Sending email to {recipient}: {message}")
        self.log_notification(recipient, "SUCCESS")
        return True

    def get_cost(self):
        return 0.001


class SMSNotification(NotificationService):
    def __init__(self) -> None:
        super().__init__("SMS Service")

    def validate_recipient(self, recipient):
        return recipient.startswith("+")

    def send(self, recipient, message):
        if not self.validate_recipient(recipient):
            self.log_notification(recipient, "FAILED")
            return False

        print(f"Sending SMS to {recipient}: {message}")
        self.log_notification(recipient, "SUCCESS")
        return True

    def get_cost(self):
        return 0.05


class PushNotification(NotificationService):
    def __init__(self) -> None:
        super().__init__("Push Notification Service")

    def validate_recipient(self, recipient):
        return len(recipient) > 5

    def send(self, recipient, message):
        if not self.validate_recipient(recipient):
            self.log_notification(recipient, "FAILED")
            return False

        print(f"Sending push notification to device {recipient}: {message}")
        self.log_notification(recipient, "SUCCESS")
        return True

    def get_cost(self):
        return 0.01


if __name__ == "__main__":
    print("Attempting to create abstract NotificationService:")
    try:
        service = NotificationService("Generic")
        print("This shouldn't work!")
    except TypeError as e:
        print(f"Error: {e}")
        print("✓ Cannot instantiate abstract class - as expected!\n")

    print("=" * 70)
    print("Creating concrete notification services")
    print("=" * 70)
    print()

    email = EmailNotification()
    sms = SMSNotification()
    push = PushNotification()

    print("--- Email Notifications ---")
    email.send("user@example.com", "Hello from email!")
    email.send("invalid-email", "This should fail")
    print()

    print("--- SMS Notifications ---")
    sms.send("+1234567890", "Hello from SMS!")
    sms.send("1234567890", "This should fail (missing +)")
    print()

    print("--- Push Notifications ---")
    push.send("device_abc123", "Hello from push!")
    push.send("dev1", "This should fail (too short)")
    print()

    print("=" * 70)
    print("Cost Information")
    print("=" * 70)
    print(f"Email cost per notification: ${email.get_cost():.3f}")
    print(f"SMS cost per notification: ${sms.get_cost():.3f}")
    print(f"Push cost per notification: ${push.get_cost():.3f}")
    print()

    print("=" * 70)
    print("Statistics")
    print("=" * 70)
    print(f"Emails sent: {email.sent_count}")
    print(f"SMS sent: {sms.sent_count}")
    print(f"Push notifications sent: {push.sent_count}")
    print()

    print("=" * 70)
    print("Polymorphic Batch Sending")
    print("=" * 70)

    def send_batch(service: NotificationService, recipients, message):
        print(f"\nUsing: {service.service_name}")
        for recipient in recipients:
            service.send(recipient, message)
        total_cost = service.sent_count * service.get_cost()
        print(f"Total sent: {service.sent_count}, Total cost: ${total_cost:.2f}\n")

    email2 = EmailNotification()
    send_batch(email2, ["alice@test.com", "bob@test.com"], "Batch email")

    sms2 = SMSNotification()
    send_batch(sms2, ["+1111111111", "+2222222222"], "Batch SMS")

    push2 = PushNotification()
    send_batch(push2, ["device_xyz789", "device_abc456"], "Batch push")
