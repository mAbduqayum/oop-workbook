# Protocol Summary

## Comparison Table

| Protocol | Type | Transport | Key Features | Best For |
| :--- | :--- | :--- | :--- | :--- |
| **Webhook** | Push | HTTP | Event-driven, real-time, server-initiated. | Receiving real-time updates (e.g., payment confirmation). |
| **Short Polling** | Pull | HTTP | Client repeatedly requests data at fixed intervals. | Simple dashboards, low-frequency updates. |
| **Long Polling** | Pull (Delayed) | HTTP | Connection held open until data is available. | Simulating real-time when WebSockets aren't an option. |
| **WebSocket** | Bidirectional | TCP | Full-duplex, persistent connection, low latency. | Chat apps, live gaming, financial tickers. |
| **REST** | Request/Response | HTTP | Stateless, standard methods (GET, POST), resource-based. | Public APIs, CRUD applications, microservices. |
| **GraphQL** | Request/Response | HTTP | Client-specified queries, single endpoint, strongly typed. | Mobile apps, complex data requirements, reducing over-fetching. |
| **gRPC** | RPC | HTTP/2 | Binary serialization (Protobuf), high performance, streaming. | Internal microservices, low-latency communication. |
