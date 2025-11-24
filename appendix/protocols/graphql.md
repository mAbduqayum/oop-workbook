# GraphQL

## Definition
GraphQL is a query language for APIs and a runtime for fulfilling those queries with your existing data. It provides a complete and understandable description of the data in your API, gives clients the power to ask for exactly what they need and nothing more.

## Key Concepts
1. **Schema**: Defines the types of data that can be queried and the relationships between them.
2. **Query**: A request for specific data (like GET in REST).
3. **Mutation**: A request to modify data (like POST/PUT/DELETE in REST).
4. **Resolver**: Functions that fetch the data for each field in the schema.

## Pros and Cons

| Pros | Cons |
| :--- | :--- |
| **No Over/Under-fetching**: Clients get exactly what they ask for. | **Complexity**: Steeper learning curve than REST. |
| **Single Endpoint**: All requests go to a single URL (usually `/graphql`). | **Caching**: HTTP caching is harder to implement (since everything is POST). |
| **Strongly Typed**: Schema ensures data validity. | **Performance**: Complex queries can overload the server (N+1 problem). |

## Use Cases
- **Mobile Apps**: Where bandwidth is limited and over-fetching is costly.
- **Complex Systems**: Where data is distributed across multiple sources but needs to be accessed via a single API.
- **Rapid Iteration**: Frontend developers can change queries without waiting for backend changes.

## Example

**Query**:
```graphql
query {
  user(id: "123") {
    name
    email
    posts {
      title
    }
  }
}
```

**Response**:
```json
{
  "data": {
    "user": {
      "name": "John Doe",
      "email": "john@example.com",
      "posts": [
        { "title": "Hello World" }
      ]
    }
  }
}
```
