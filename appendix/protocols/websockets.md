# WebSockets

## Definition
WebSocket is a computer communications protocol, providing full-duplex communication channels over a single TCP connection. It enables interaction between a web browser (or other client application) and a web server with lower overhead than half-duplex alternatives such as HTTP polling, facilitating real-time data transfer from and to the server.

## How it Works
1. **Handshake**: The client sends a standard HTTP request to the server with an `Upgrade` header, asking to switch to the WebSocket protocol.
2. **Connection**: If the server supports it, it responds with a `101 Switching Protocols` status code.
3. **Data Transfer**: Once the connection is established, data can be sent back and forth as "frames" at any time by either party.
4. **Close**: Either side can close the connection.

## Pros and Cons

| Pros | Cons |
| :--- | :--- |
| **Real-time**: True full-duplex communication. | **Complexity**: More complex to implement and scale than HTTP. |
| **Low Overhead**: Less data overhead per message compared to HTTP headers. | **Stateful**: The server must maintain the state of each connection, which can consume resources. |
| **Efficiency**: Ideal for high-frequency updates. | **Firewalls**: Some corporate firewalls may block WebSocket connections. |

## Use Cases
- **Chat Applications**: Real-time messaging.
- **Live Gaming**: Multiplayer game state synchronization.
- **Collaborative Editing**: Google Docs-style real-time editing.
- **Financial Tickers**: Live stock price updates.

## Example (Conceptual)

**Client (JavaScript)**:
```javascript
const socket = new WebSocket('ws://example.com/socket');

socket.onopen = function(event) {
  socket.send('Hello Server!');
};

socket.onmessage = function(event) {
  console.log('Message from server ', event.data);
};
```

**Server (Python/FastAPI)**:
```python
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")
```
