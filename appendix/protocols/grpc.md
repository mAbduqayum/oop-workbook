# gRPC

## Definition
gRPC is a high-performance, open-source universal RPC (Remote Procedure Call) framework. It uses HTTP/2 for transport, Protocol Buffers as the interface description language, and provides features such as authentication, load balancing, and more.

## Key Concepts
1. **Protocol Buffers (Protobuf)**: A language-neutral, platform-neutral mechanism for serializing structured data. It is smaller and faster than XML or JSON.
2. **Service Definition**: You define your service and the methods it exposes in a `.proto` file.
3. **Code Generation**: Tools generate client and server code from the `.proto` file in various languages.
4. **Streaming**: Supports unary, server streaming, client streaming, and bidirectional streaming.

## Pros and Cons

| Pros | Cons |
| :--- | :--- |
| **Performance**: Binary serialization and HTTP/2 make it very fast. | **Browser Support**: Limited browser support (requires gRPC-Web). |
| **Strong Typing**: Protobuf ensures strict contracts between client and server. | **Debuggability**: Binary data is not human-readable like JSON. |
| **Polyglot**: Supports many languages (Go, Java, Python, etc.). | **Learning Curve**: Requires understanding Protobuf and RPC concepts. |

## Use Cases
- **Microservices**: Low-latency communication between internal services.
- **Mobile Clients**: Efficient data transmission for mobile devices.
- **Real-time Streaming**: Bi-directional streaming for real-time updates.

## Example

**Proto Definition (`service.proto`)**:
```protobuf
service Greeter {
  rpc SayHello (HelloRequest) returns (HelloReply) {}
}

message HelloRequest {
  string name = 1;
}

message HelloReply {
  string message = 1;
}
```
