"""
Tests for Notification Dispatcher - Polymorphism Exercise

Run tests with: pytest test_notification_dispatcher.py -v
"""

import pytest
from abc import ABC, abstractmethod
from datetime import datetime


# Students should implement these classes (or import from abstraction chapter)
class NotificationService(ABC):
    """Abstract base class for all notification services"""

    def __init__(self, service_name):
        self.service_name = service_name
        self.sent_count = 0

    @abstractmethod
    def validate_recipient(self, recipient):
        """Validate recipient format"""
        pass

    @abstractmethod
    def send(self, recipient, message):
        """Send notification"""
        pass

    @abstractmethod
    def get_cost(self):
        """Return cost per notification"""
        pass

    def log_notification(self, recipient, status):
        """Log notification attempt"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {self.service_name}: {recipient} - {status}")
        if status == "SUCCESS":
            self.sent_count += 1


class EmailNotification(NotificationService):
    """Email notification service"""

    def __init__(self):
        super().__init__("Email Service")

    def validate_recipient(self, recipient):
        return "@" in recipient

    def get_cost(self):
        return 0.001

    def send(self, recipient, message):
        if not self.validate_recipient(recipient):
            self.log_notification(recipient, "FAILED")
            return False
        print(f"Sending email to {recipient}: {message}")
        self.log_notification(recipient, "SUCCESS")
        return True


class SMSNotification(NotificationService):
    """SMS notification service"""

    def __init__(self):
        super().__init__("SMS Service")

    def validate_recipient(self, recipient):
        return recipient.startswith("+")

    def get_cost(self):
        return 0.05

    def send(self, recipient, message):
        if not self.validate_recipient(recipient):
            self.log_notification(recipient, "FAILED")
            return False
        print(f"Sending SMS to {recipient}: {message}")
        self.log_notification(recipient, "SUCCESS")
        return True


class PushNotification(NotificationService):
    """Push notification service"""

    def __init__(self):
        super().__init__("Push Notification Service")

    def validate_recipient(self, recipient):
        return len(recipient) > 5

    def get_cost(self):
        return 0.01

    def send(self, recipient, message):
        if not self.validate_recipient(recipient):
            self.log_notification(recipient, "FAILED")
            return False
        print(f"Sending push notification to device {recipient}: {message}")
        self.log_notification(recipient, "SUCCESS")
        return True


# Import student's solution
try:
    from notification_dispatcher import (
        NotificationDispatcher,
        send_multi_channel,
        find_cheapest_service,
        batch_send,
    )
except ImportError:
    # Placeholder if student hasn't implemented yet
    class NotificationDispatcher:
        def __init__(self, services):
            raise NotImplementedError("Implement NotificationDispatcher class")

    def send_multi_channel(services, recipient_map, message):
        raise NotImplementedError("Implement send_multi_channel()")

    def find_cheapest_service(services):
        raise NotImplementedError("Implement find_cheapest_service()")

    def batch_send(services, recipients, message):
        raise NotImplementedError("Implement batch_send()")


@pytest.fixture
def notification_services():
    """Create sample notification services"""
    return [EmailNotification(), SMSNotification(), PushNotification()]


@pytest.fixture
def dispatcher(notification_services):
    """Create dispatcher with sample services"""
    return NotificationDispatcher(notification_services)


class TestNotificationDispatcher:
    """Test NotificationDispatcher class"""

    def test_dispatcher_initialization(self, notification_services):
        dispatcher = NotificationDispatcher(notification_services)
        assert hasattr(dispatcher, "services") or hasattr(dispatcher, "_services")

    def test_add_service(self, dispatcher):
        initial_count = len(dispatcher.services) if hasattr(dispatcher, "services") else 3
        new_service = EmailNotification()
        dispatcher.add_service(new_service)
        # Check service was added (implementation dependent)
        assert hasattr(dispatcher, "add_service")

    def test_remove_service(self, dispatcher, notification_services):
        service_to_remove = notification_services[0]
        dispatcher.remove_service(service_to_remove)
        assert hasattr(dispatcher, "remove_service")

    def test_broadcast_to_all_services(self, dispatcher, capsys):
        recipients = ["user@test.com", "+1234567890", "device_abc123"]
        dispatcher.broadcast(recipients, "Test message")
        captured = capsys.readouterr()
        # Should attempt to send through all services
        assert "email" in captured.out.lower() or "Email" in captured.out

    def test_send_to_valid_only(self, dispatcher):
        # Mix of valid and invalid recipients
        recipients = ["valid@test.com", "invalid-email", "+1234567890", "short"]
        dispatcher.send_to_valid(recipients, "Test message")
        # Should only send to valid recipients for each service

    def test_total_sent_property(self, dispatcher):
        dispatcher.broadcast(
            ["user@test.com", "+1234567890", "device_abc123"], "Test"
        )
        total = dispatcher.total_sent
        assert isinstance(total, int)
        assert total >= 0

    def test_total_cost_property(self, dispatcher):
        dispatcher.broadcast(
            ["user@test.com", "+1234567890", "device_abc123"], "Test"
        )
        total_cost = dispatcher.total_cost
        assert isinstance(total_cost, (int, float))
        assert total_cost >= 0


class TestSendMultiChannel:
    """Test send_multi_channel function"""

    def test_send_to_specific_channels(self, notification_services):
        email, sms, push = notification_services
        recipient_map = {
            email: "admin@test.com",
            sms: "+9876543210",
            push: "device_xyz789",
        }
        success_count = send_multi_channel(
            notification_services, recipient_map, "Alert"
        )
        assert success_count >= 0
        assert isinstance(success_count, int)

    def test_send_with_invalid_recipients(self, notification_services):
        email, sms, push = notification_services
        recipient_map = {
            email: "invalid-email",
            sms: "1234567890",  # missing +
            push: "short",
        }
        success_count = send_multi_channel(
            notification_services, recipient_map, "Test"
        )
        assert success_count == 0

    def test_send_mixed_valid_invalid(self, notification_services):
        email, sms, push = notification_services
        recipient_map = {
            email: "valid@test.com",
            sms: "invalid",
            push: "device_valid123",
        }
        success_count = send_multi_channel(
            notification_services, recipient_map, "Test"
        )
        assert success_count > 0


class TestFindCheapestService:
    """Test find_cheapest_service function"""

    def test_find_cheapest_among_services(self, notification_services):
        cheapest = find_cheapest_service(notification_services)
        assert isinstance(cheapest, NotificationService)
        # Email should be cheapest at 0.001
        assert cheapest.get_cost() == 0.001
        assert isinstance(cheapest, EmailNotification)

    def test_find_cheapest_single_service(self):
        services = [SMSNotification()]
        cheapest = find_cheapest_service(services)
        assert cheapest.get_cost() == 0.05

    def test_find_cheapest_same_cost(self):
        # Create multiple services with same cost
        services = [EmailNotification(), EmailNotification()]
        cheapest = find_cheapest_service(services)
        assert cheapest.get_cost() == 0.001


class TestBatchSend:
    """Test batch_send function"""

    def test_batch_send_all_valid(self, notification_services):
        recipients = ["test@example.com", "+1111111111", "device_test123"]
        results = batch_send(notification_services, recipients, "Batch test")
        assert isinstance(results, dict)
        # Should have some success
        assert "success" in results or results.get("success", 0) >= 0

    def test_batch_send_all_invalid(self, notification_services):
        recipients = ["invalid", "invalid", "inv"]
        results = batch_send(notification_services, recipients, "Test")
        # Most should fail
        if "failed" in results:
            assert results["failed"] >= 0

    def test_batch_send_mixed(self, notification_services):
        recipients = ["valid@test.com", "invalid", "+1234567890"]
        results = batch_send(notification_services, recipients, "Test")
        assert isinstance(results, dict)

    def test_batch_send_includes_cost(self, notification_services):
        recipients = ["test@example.com"]
        results = batch_send(notification_services, recipients, "Test")
        # Should include cost information
        assert "total_cost" in results or "cost" in results


class TestPolymorphism:
    """Test polymorphic behavior"""

    def test_dispatcher_works_with_any_service(self):
        """Dispatcher should work with any NotificationService subclass"""

        class SlackNotification(NotificationService):
            def __init__(self):
                super().__init__("Slack Service")

            def validate_recipient(self, recipient):
                return recipient.startswith("#")

            def get_cost(self):
                return 0.005

            def send(self, recipient, message):
                if not self.validate_recipient(recipient):
                    self.log_notification(recipient, "FAILED")
                    return False
                print(f"Sending Slack message to {recipient}: {message}")
                self.log_notification(recipient, "SUCCESS")
                return True

        services = [EmailNotification(), SlackNotification()]
        dispatcher = NotificationDispatcher(services)
        dispatcher.broadcast(["test@test.com", "#general"], "Test")
        assert dispatcher.total_sent > 0

    def test_no_type_checking_needed(self, notification_services):
        """Functions should work polymorphically without type checks"""
        # All functions should work without knowing specific types
        cheapest = find_cheapest_service(notification_services)
        assert hasattr(cheapest, "send")
        assert hasattr(cheapest, "get_cost")

    def test_extensible_design(self, notification_services):
        """Adding new service types shouldn't break existing code"""

        class CustomNotification(NotificationService):
            def __init__(self):
                super().__init__("Custom Service")

            def validate_recipient(self, recipient):
                return True

            def get_cost(self):
                return 0.02

            def send(self, recipient, message):
                self.log_notification(recipient, "SUCCESS")
                return True

        # Add custom service to existing services
        all_services = notification_services + [CustomNotification()]

        # All existing functions should still work
        dispatcher = NotificationDispatcher(all_services)
        cheapest = find_cheapest_service(all_services)
        results = batch_send(all_services, ["test"], "Message")

        assert isinstance(cheapest, NotificationService)
        assert isinstance(results, dict)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
