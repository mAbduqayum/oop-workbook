# Python OOP Practice - Abstraction: Notification System

## Exercise: Abstract Notification Service

Create an abstract `NotificationService` class with concrete implementations for different notification types (Email, SMS) that demonstrate abstraction in a real-world scenario.

**Instructions:**
Implement a notification service system using Abstract Base Classes to ensure all notification types implement required methods for validation, sending, and cost calculation.

This exercise demonstrates how abstraction helps create flexible systems that can be extended with new notification types without changing existing code.

**Your Complete Task:**
1. Create an abstract `NotificationService` class that inherits from `ABC`
2. Add constructor with `service_name` parameter (string)
3. Add instance attribute `sent_count` initialized to 0
4. Add abstract method `validate_recipient(recipient)` that returns bool
5. Add abstract method `send(recipient, message)` that returns bool
6. Add abstract method `get_cost()` that returns float (cost per notification)
7. Add concrete method `log_notification(recipient, status)`:
   - Print log message with timestamp, service name, recipient, and status
   - Increment `sent_count` if status is "SUCCESS"
8. Create `EmailNotification` class:
   - Service name: "Email Service"
   - Validate: recipient must contain '@'
   - Cost: 0.001 per email
   - Send: validate, print "Sending email to {recipient}: {message}", log
9. Create `SMSNotification` class:
   - Service name: "SMS Service"
   - Validate: recipient must start with '+'
   - Cost: 0.05 per SMS
   - Send: validate, print "Sending SMS to {recipient}: {message}", log

**What You'll Learn:**
- **Abstract and Concrete Methods:** Mixing required and shared functionality
- **Service Interfaces:** Creating consistent APIs across different services
- **Template Pattern:** Abstract class defines workflow, children implement details
- **Extensibility:** Easy to add new notification types (Push, Slack, etc.)

**Example Usage:**
```python
from abc import ABC, abstractmethod
from datetime import datetime

# This should fail - cannot instantiate abstract class
try:
    service = NotificationService("Generic")
except TypeError as e:
    print(f"Error: {e}")

# Create concrete services
email = EmailNotification()
sms = SMSNotification()

# Send notifications
email.send("user@example.com", "Hello!")
# Output: Sending email to user@example.com: Hello!
#         [2025-10-02 07:50:00] Email Service: user@example.com - SUCCESS

sms.send("+1234567890", "Verification code: 123456")
# Output: Sending SMS to +1234567890: Verification code: 123456
#         [2025-10-02 07:50:00] SMS Service: +1234567890 - SUCCESS

# Invalid recipients
email.send("invalid-email", "Test")
# Output: [2025-10-02 07:50:00] Email Service: invalid-email - FAILED

sms.send("1234567890", "Test")  # Missing +
# Output: [2025-10-02 07:50:00] SMS Service: 1234567890 - FAILED

# Check costs
print(f"Email cost: ${email.get_cost():.3f}")  # $0.001
print(f"SMS cost: ${sms.get_cost():.3f}")      # $0.050

# Track sent count
print(f"Emails sent: {email.sent_count}")  # 1
print(f"SMS sent: {sms.sent_count}")       # 1

# Function that works with ANY notification service
def send_batch(service: NotificationService, recipients, message):
    for recipient in recipients:
        service.send(recipient, message)
    total_cost = service.sent_count * service.get_cost()
    print(f"Total sent: {service.sent_count}, Total cost: ${total_cost:.2f}")

# Works with any service
send_batch(email, ["alice@test.com", "bob@test.com"], "Batch message")
send_batch(sms, ["+1111111111", "+2222222222"], "Batch SMS")
```

**Key Abstraction Concepts:**
- **Mixed methods** - Abstract methods for variable behavior, concrete for shared logic
- **Service contract** - All notification services must implement the same interface
- **Extensible design** - Add PushNotification, SlackNotification without changing existing code
- **Encapsulation** - `log_notification()` handles logging details, children just call it

**Bonus Challenge:**
Add a third notification type `PushNotification`:
- Service name: "Push Notification Service"
- Validate: recipient (device ID) must be longer than 5 characters
- Cost: 0.01 per push
- Same send pattern as others
