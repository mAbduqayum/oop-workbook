# REST (Representational State Transfer)

## Definition
REST is an architectural style for providing standards between computer systems on the web, making it easier for systems to communicate with each other. REST-compliant systems, often called RESTful systems, are characterized by how they are stateless and separate the concerns of client and server.

## Key Principles
1. **Client-Server**: Separation of concerns.
2. **Stateless**: Each request from client to server must contain all the information needed to understand and process the request.
3. **Cacheable**: Responses must define themselves as cacheable or not.
4. **Uniform Interface**: Simplifies and decouples the architecture (e.g., using standard HTTP methods).
5. **Layered System**: A client cannot ordinarily tell whether it is connected directly to the end server or to an intermediary along the way.

## HTTP Methods
- **GET**: Retrieve a resource.
- **POST**: Create a new resource.
- **PUT**: Update an existing resource (replace).
- **PATCH**: Update an existing resource (partial).
- **DELETE**: Remove a resource.

## Pros and Cons

| Pros | Cons |
| :--- | :--- |
| **Scalability**: Statelessness allows for easy scaling. | **Over-fetching**: May return more data than needed. |
| **Simplicity**: Uses standard HTTP methods and status codes. | **Under-fetching**: May require multiple requests to get related data. |
| **Flexibility**: Can return different data formats (JSON, XML, etc.). | **Versioning**: Managing API versions can be challenging. |

## Use Cases
- **Public APIs**: Most public web APIs (Twitter, GitHub) use REST.
- **Microservices**: Communication between internal services.
- **Web Applications**: Backend for Single Page Applications (SPAs).

## Example

**Request**:
`GET /users/123`

**Response**:
```json
{
  "id": 123,
  "name": "John Doe",
  "email": "john@example.com"
}
```
