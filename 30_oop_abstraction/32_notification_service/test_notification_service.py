import pytest
from notification_service import (
    EmailNotification,
    NotificationService,
    PushNotification,
    SMSNotification,
)


class TestNotificationService:
    def test_cannot_instantiate_abstract_service(self):
        with pytest.raises(TypeError):
            NotificationService("Generic Service")


class TestEmailNotification:
    def test_email_creation(self):
        email = EmailNotification()
        assert email.service_name == "Email Service"
        assert email.sent_count == 0

    def test_email_validate_valid(self):
        email = EmailNotification()
        assert email.validate_recipient("user@example.com") is True
        assert email.validate_recipient("test@test.co.uk") is True

    def test_email_validate_invalid(self):
        email = EmailNotification()
        assert email.validate_recipient("invalid-email") is False
        assert email.validate_recipient("no-at-sign.com") is False

    def test_email_send_success(self, capsys):
        email = EmailNotification()
        result = email.send("user@example.com", "Test message")
        assert result is True
        assert email.sent_count == 1

        captured = capsys.readouterr()
        assert "Sending email to user@example.com: Test message" in captured.out
        assert "SUCCESS" in captured.out

    def test_email_send_failure(self, capsys):
        email = EmailNotification()
        result = email.send("invalid-email", "Test message")
        assert result is False
        assert email.sent_count == 0

        captured = capsys.readouterr()
        assert "FAILED" in captured.out

    def test_email_cost(self):
        email = EmailNotification()
        assert email.get_cost() == 0.001

    def test_email_is_notification_service(self):
        email = EmailNotification()
        assert isinstance(email, NotificationService)


class TestSMSNotification:
    def test_sms_creation(self):
        sms = SMSNotification()
        assert sms.service_name == "SMS Service"
        assert sms.sent_count == 0

    def test_sms_validate_valid(self):
        sms = SMSNotification()
        assert sms.validate_recipient("+1234567890") is True
        assert sms.validate_recipient("+44123456789") is True

    def test_sms_validate_invalid(self):
        sms = SMSNotification()
        assert sms.validate_recipient("1234567890") is False
        assert sms.validate_recipient("no-plus-sign") is False

    def test_sms_send_success(self, capsys):
        sms = SMSNotification()
        result = sms.send("+1234567890", "Test SMS")
        assert result is True
        assert sms.sent_count == 1

        captured = capsys.readouterr()
        assert "Sending SMS to +1234567890: Test SMS" in captured.out
        assert "SUCCESS" in captured.out

    def test_sms_send_failure(self, capsys):
        sms = SMSNotification()
        result = sms.send("1234567890", "Test SMS")
        assert result is False
        assert sms.sent_count == 0

        captured = capsys.readouterr()
        assert "FAILED" in captured.out

    def test_sms_cost(self):
        sms = SMSNotification()
        assert sms.get_cost() == 0.05

    def test_sms_is_notification_service(self):
        sms = SMSNotification()
        assert isinstance(sms, NotificationService)


class TestPushNotification:
    def test_push_creation(self):
        push = PushNotification()
        assert push.service_name == "Push Notification Service"
        assert push.sent_count == 0

    def test_push_validate_valid(self):
        push = PushNotification()
        assert push.validate_recipient("device_abc123") is True
        assert push.validate_recipient("device_xyz789") is True

    def test_push_validate_invalid(self):
        push = PushNotification()
        assert push.validate_recipient("dev1") is False
        assert push.validate_recipient("12345") is False

    def test_push_send_success(self, capsys):
        push = PushNotification()
        result = push.send("device_abc123", "Test push")
        assert result is True
        assert push.sent_count == 1

        captured = capsys.readouterr()
        assert (
            "Sending push notification to device device_abc123: Test push"
            in captured.out
        )
        assert "SUCCESS" in captured.out

    def test_push_send_failure(self, capsys):
        push = PushNotification()
        result = push.send("dev1", "Test push")
        assert result is False
        assert push.sent_count == 0

        captured = capsys.readouterr()
        assert "FAILED" in captured.out

    def test_push_cost(self):
        push = PushNotification()
        assert push.get_cost() == 0.01

    def test_push_is_notification_service(self):
        push = PushNotification()
        assert isinstance(push, NotificationService)


class TestPolymorphism:
    def test_all_services_have_required_methods(self):
        services = [
            EmailNotification(),
            SMSNotification(),
            PushNotification(),
        ]

        for service in services:
            assert hasattr(service, "validate_recipient")
            assert hasattr(service, "send")
            assert hasattr(service, "get_cost")
            assert callable(service.validate_recipient)
            assert callable(service.send)
            assert callable(service.get_cost)

    def test_polymorphic_function(self):
        def get_total_cost(
            service: NotificationService, num_notifications: int
        ) -> float:
            return service.get_cost() * num_notifications

        email = EmailNotification()
        sms = SMSNotification()
        push = PushNotification()

        assert get_total_cost(email, 1000) == 1.0
        assert get_total_cost(sms, 100) == 5.0
        assert get_total_cost(push, 500) == 5.0

    def test_sent_count_tracking(self):
        services = [
            EmailNotification(),
            SMSNotification(),
            PushNotification(),
        ]

        recipients = [
            "user@example.com",
            "+1234567890",
            "device_abc123",
        ]

        for service, recipient in zip(services, recipients, strict=False):
            assert service.sent_count == 0
            service.send(recipient, "Test")
            assert service.sent_count == 1
            service.send(recipient, "Test 2")
            assert service.sent_count == 2


class TestLogNotification:
    def test_log_increments_count_on_success(self):
        email = EmailNotification()
        assert email.sent_count == 0

        email.log_notification("user@example.com", "SUCCESS")
        assert email.sent_count == 1

        email.log_notification("user2@example.com", "SUCCESS")
        assert email.sent_count == 2

    def test_log_does_not_increment_on_failure(self):
        email = EmailNotification()
        assert email.sent_count == 0

        email.log_notification("invalid", "FAILED")
        assert email.sent_count == 0

        email.log_notification("invalid2", "FAILED")
        assert email.sent_count == 0

    def test_log_prints_message(self, capsys):
        email = EmailNotification()
        email.log_notification("user@example.com", "SUCCESS")

        captured = capsys.readouterr()
        assert "Email Service" in captured.out
        assert "user@example.com" in captured.out
        assert "SUCCESS" in captured.out
