# Polling

## Definition
Polling is a technique where a client repeatedly requests data from a server at regular intervals to check for updates. It is a way to simulate real-time communication when true push mechanisms (like webhooks or websockets) are not available or feasible.

## Types of Polling

### 1. Short Polling
The client sends a request to the server at fixed intervals (e.g., every 5 seconds). The server responds immediately, either with new data or an empty response if nothing has changed.

### 2. Long Polling
The client sends a request, and the server holds the connection open until new data is available or a timeout occurs. Once the client receives a response, it immediately sends a new request.

## Pros and Cons

| Feature | Short Polling | Long Polling |
| :--- | :--- | :--- |
| **Real-time** | Low (depends on interval) | High (near real-time) |
| **Server Load** | High (many empty requests) | Medium (fewer requests, but open connections) |
| **Complexity** | Low (easy to implement) | Medium (requires server support for holding connections) |
| **Resource Usage** | Wastes bandwidth on empty checks | More efficient than short polling |

## Use Cases
- **Dashboards**: Updating status indicators every minute (Short Polling).
- **Chat Applications**: Checking for new messages (Long Polling is better here, though WebSockets are preferred).
- **Job Status**: Checking if a long-running background task has completed.

## Example (Conceptual: Short Polling)

**Scenario**: A user is waiting for a file export to finish.

1. **Client**: Sends GET request to `/export/status`.
2. **Server**: Responds `{ "status": "processing" }`.
3. **Client**: Waits 5 seconds.
4. **Client**: Sends GET request to `/export/status`.
5. **Server**: Responds `{ "status": "processing" }`.
6. **Client**: Waits 5 seconds.
7. **Client**: Sends GET request to `/export/status`.
8. **Server**: Responds `{ "status": "completed", "url": "..." }`.
9. **Client**: Stops polling and downloads the file.
