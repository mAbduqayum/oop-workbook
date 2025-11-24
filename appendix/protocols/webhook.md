# Webhooks

## Definition
A webhook is a mechanism that allows one system to send real-time data to another system as soon as a specific event occurs. It is often referred to as a "user-defined HTTP callback".

## How it Works
1. **Setup**: The consumer (receiver) registers a URL (the webhook endpoint) with the provider (sender).
2. **Event**: An event occurs in the provider's system (e.g., a payment is processed, a new user signs up).
3. **Notification**: The provider makes an HTTP POST request to the registered URL with a payload containing details about the event.
4. **Action**: The consumer receives the request and takes appropriate action (e.g., updates a database, sends an email).

## Pros and Cons

| Pros | Cons |
| :--- | :--- |
| **Real-time**: Updates are received immediately. | **Reliability**: If the receiver is down, data might be lost unless the provider has a retry mechanism. |
| **Efficiency**: No need to constantly poll the server, saving resources. | **Security**: Endpoints must be secured to prevent unauthorized requests. |
| **Simplicity**: Easy to set up for specific events. | **Debugging**: Can be harder to debug since it's asynchronous and relies on external triggers. |

## Use Cases
- **Payment Gateways**: Stripe sending a notification when a payment succeeds.
- **CI/CD**: GitHub notifying a build server when code is pushed.
- **Messaging**: Slack receiving a message from a bot.

## Example (Conceptual)

**Scenario**: A user purchases an item on an e-commerce site.

1. **Event**: Purchase confirmed.
2. **Provider (E-commerce)**: Sends a POST request to `https://inventory-system.com/webhooks/order-created`.
3. **Payload**:
   ```json
   {
     "event": "order.created",
     "data": {
       "order_id": "12345",
       "items": [{"id": "abc", "qty": 1}]
     }
   }
   ```
4. **Consumer (Inventory)**: Receives the data and decrements the stock for item "abc".
