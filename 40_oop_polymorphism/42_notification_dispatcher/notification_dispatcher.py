from abc import ABC, abstractmethod
from datetime import datetime
from typing import Dict, List


class NotificationService(ABC):
    def __init__(self, service_name: str) -> None:
        self.service_name = service_name
        self.sent_count = 0

    @abstractmethod
    def validate_recipient(self, recipient: str) -> bool:
        pass

    @abstractmethod
    def send(self, recipient: str, message: str) -> bool:
        pass

    @abstractmethod
    def get_cost(self) -> float:
        pass

    def log_notification(self, recipient: str, status: str) -> None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {self.service_name}: {recipient} - {status}")
        if status == "SUCCESS":
            self.sent_count += 1


class EmailNotification(NotificationService):
    def __init__(self) -> None:
        super().__init__("Email Service")

    def validate_recipient(self, recipient: str) -> bool:
        return "@" in recipient

    def get_cost(self) -> float:
        return 0.001

    def send(self, recipient: str, message: str) -> bool:
        if not self.validate_recipient(recipient):
            self.log_notification(recipient, "FAILED")
            return False
        print(f"Sending email to {recipient}: {message}")
        self.log_notification(recipient, "SUCCESS")
        return True


class SMSNotification(NotificationService):
    def __init__(self) -> None:
        super().__init__("SMS Service")

    def validate_recipient(self, recipient: str) -> bool:
        return recipient.startswith("+")

    def get_cost(self) -> float:
        return 0.05

    def send(self, recipient: str, message: str) -> bool:
        if not self.validate_recipient(recipient):
            self.log_notification(recipient, "FAILED")
            return False
        print(f"Sending SMS to {recipient}: {message}")
        self.log_notification(recipient, "SUCCESS")
        return True


class PushNotification(NotificationService):
    def __init__(self) -> None:
        super().__init__("Push Notification Service")

    def validate_recipient(self, recipient: str) -> bool:
        return len(recipient) > 5

    def get_cost(self) -> float:
        return 0.01

    def send(self, recipient: str, message: str) -> bool:
        if not self.validate_recipient(recipient):
            self.log_notification(recipient, "FAILED")
            return False
        print(f"Sending push notification to device {recipient}: {message}")
        self.log_notification(recipient, "SUCCESS")
        return True


class NotificationDispatcher:
    def __init__(self, services: List[NotificationService]) -> None:
        self.services = services

    def add_service(self, service: NotificationService) -> None:
        self.services.append(service)

    def remove_service(self, service: NotificationService) -> None:
        if service in self.services:
            self.services.remove(service)

    def broadcast(self, recipients: List[str], message: str) -> None:
        for service in self.services:
            for recipient in recipients:
                service.send(recipient, message)

    def send_to_valid(self, recipients: List[str], message: str) -> None:
        for service in self.services:
            for recipient in recipients:
                if service.validate_recipient(recipient):
                    service.send(recipient, message)

    @property
    def total_sent(self) -> int:
        return sum(service.sent_count for service in self.services)

    @property
    def total_cost(self) -> float:
        return sum(service.sent_count * service.get_cost() for service in self.services)


def send_multi_channel(
    services: List[NotificationService],
    recipient_map: Dict[NotificationService, str],
    message: str,
) -> int:
    success_count = 0
    for service, recipient in recipient_map.items():
        if service.send(recipient, message):
            success_count += 1
    return success_count


def find_cheapest_service(services: List[NotificationService]) -> NotificationService:
    return min(services, key=lambda service: service.get_cost())


def batch_send(
    services: List[NotificationService], recipients: List[str], message: str
) -> Dict[str, int | float]:
    success = 0
    failed = 0
    total_cost = 0.0

    for service in services:
        for recipient in recipients:
            if service.send(recipient, message):
                success += 1
                total_cost += service.get_cost()
            else:
                failed += 1

    return {"success": success, "failed": failed, "total_cost": total_cost}


if __name__ == "__main__":
    email = EmailNotification()
    sms = SMSNotification()
    push = PushNotification()

    dispatcher = NotificationDispatcher([email, sms, push])

    print("=== Broadcasting Message ===")
    dispatcher.broadcast(
        ["user@example.com", "+1234567890", "device_abc123"],
        "Server maintenance scheduled for tonight",
    )

    print(f"\nTotal notifications sent: {dispatcher.total_sent}")
    print(f"Total cost: ${dispatcher.total_cost:.3f}")

    print("\n=== Sending to Valid Recipients ===")
    dispatcher.send_to_valid(
        ["user@example.com", "invalid-email", "+1234567890"],
        "Account verification required",
    )

    cheapest = find_cheapest_service([email, sms, push])
    print(
        f"\n\nCheapest service: {cheapest.service_name} at ${cheapest.get_cost():.3f} per message"
    )

    print("\n=== Batch Send ===")
    results = batch_send(
        [email, sms, push],
        ["test@example.com", "+1111111111", "device_test123"],
        "Batch test message",
    )
    print(f"Batch send results: {results}")
