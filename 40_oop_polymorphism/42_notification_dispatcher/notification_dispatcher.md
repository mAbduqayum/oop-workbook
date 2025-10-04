# Python OOP Practice - Polymorphism: Notification Dispatcher

## Exercise: Polymorphic Notification System

Build upon the abstract `NotificationService` classes from the abstraction chapter to create a dispatcher that sends notifications through multiple channels polymorphically.

**Instructions:**
Reuse the abstract `NotificationService` and concrete implementations (EmailNotification, SMSNotification, PushNotification) from `30_oop_abstraction/32_notification_service/`. Create a dispatcher system that broadcasts messages to multiple notification services simultaneously.

This exercise demonstrates how polymorphism enables flexible, channel-agnostic messaging systems.

**Your Complete Task:**
1. Import or recreate `NotificationService` and its subclasses from the abstraction chapter
2. Create a `NotificationDispatcher` class with:
   - Constructor that accepts a list of notification services
   - Method `add_service(service)` to register new notification channels
   - Method `remove_service(service)` to unregister channels
   - Method `broadcast(recipients, message)` that sends to all services
   - Method `send_to_valid(recipients, message)` that only sends if recipient is valid
   - Property `total_sent` that sums sent_count from all services
   - Property `total_cost` that calculates total cost across all services
3. Create a function `send_multi_channel(services, recipient_map, message)` that:
   - Takes a dictionary mapping service types to recipients
   - Sends the message through appropriate channels
   - Returns success count
4. Create a function `find_cheapest_service(services)` that:
   - Returns the service with lowest cost per notification
5. Create a function `batch_send(services, recipients, message)` that:
   - Attempts to send through each service
   - Collects results from all services
   - Returns summary statistics

**What You'll Learn:**
- **Polymorphic collections:** Working with lists of different notification types
- **Interface uniformity:** All services have the same methods
- **Flexible architecture:** Add new notification types without changing dispatcher
- **Real-world design:** Multi-channel notification systems

**Example Usage:**
```python
from abc import ABC, abstractmethod
from datetime import datetime

# Create multiple notification services
email = EmailNotification()
sms = SMSNotification()
push = PushNotification()

# Create dispatcher with multiple channels
dispatcher = NotificationDispatcher([email, sms, push])

# Broadcast to all channels polymorphically
recipients = {
    "email": "user@example.com",
    "sms": "+1234567890",
    "push": "device_abc123"
}

print("=== Broadcasting Message ===")
dispatcher.broadcast(
    ["user@example.com", "+1234567890", "device_abc123"],
    "Server maintenance scheduled for tonight"
)
# Output:
# Sending email to user@example.com: Server maintenance scheduled for tonight
# [2025-10-04 22:45:00] Email Service: user@example.com - SUCCESS
# Sending SMS to +1234567890: Server maintenance scheduled for tonight
# [2025-10-04 22:45:00] SMS Service: +1234567890 - SUCCESS
# Sending push notification to device device_abc123: Server maintenance scheduled for tonight
# [2025-10-04 22:45:00] Push Notification Service: device_abc123 - SUCCESS

# Check total notifications sent
print(f"\nTotal notifications sent: {dispatcher.total_sent}")
# Output: Total notifications sent: 3

# Check total cost
print(f"Total cost: ${dispatcher.total_cost:.3f}")
# Output: Total cost: $0.061

# Add a new service dynamically
slack = SlackNotification()  # If you implement this
dispatcher.add_service(slack)

# Send only to valid recipients
print("\n=== Sending to Valid Recipients ===")
dispatcher.send_to_valid(
    ["user@example.com", "invalid-email", "+1234567890"],
    "Account verification required"
)
# Output: Only sends to valid recipients

# Multi-channel targeting
recipient_map = {
    email: "admin@company.com",
    sms: "+9876543210",
    push: "device_xyz789"
}
success_count = send_multi_channel([email, sms, push], recipient_map, "Alert!")
print(f"\nSuccessfully sent to {success_count} channels")

# Find cheapest service
cheapest = find_cheapest_service([email, sms, push])
print(f"\nCheapest service: {cheapest.service_name} at ${cheapest.get_cost():.3f} per message")
# Output: Cheapest service: Email Service at $0.001 per message

# Batch send with statistics
results = batch_send(
    [email, sms, push],
    ["test@example.com", "+1111111111", "device_test123"],
    "Batch test message"
)
print(f"\nBatch send results: {results}")
# Output: Batch send results: {'success': 3, 'failed': 0, 'total_cost': 0.061}
```

**Key Polymorphism Concepts:**
- **Uniform interface:** All services implement `send()`, `validate_recipient()`, `get_cost()`
- **Transparent operation:** Dispatcher doesn't care about service types
- **Dynamic composition:** Add/remove services at runtime
- **Aggregation:** Combine results from multiple polymorphic objects
- **Extensibility:** New notification types integrate seamlessly

**Challenge Extensions:**
- Implement priority-based sending (try expensive services only if cheap ones fail)
- Add `send_with_fallback(recipients, message)` that tries services in cost order
- Create `NotificationLogger` that tracks all messages across services
- Implement rate limiting per service
- Add `send_scheduled(recipients, message, delay)` for delayed notifications
- Create filtering by service type: `get_services_by_type(type_name)`
