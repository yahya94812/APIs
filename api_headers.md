API headers are **key-value pairs** sent along with an HTTP request or response. They provide **metadata** about the request/response, such as authentication details, content type, caching rules, and client information.

### Common Types of API Headers

1. **Authorization Header**

   * Used to authenticate the client.
   * Example:

     ```
     Authorization: Bearer eyJhbGciOiJIUzI1Ni...
     ```
   * Other formats include Basic Auth and API Keys.

2. **Content-Type Header**

   * Specifies the format of the request body.
   * Example:

     ```
     Content-Type: application/json
     ```
   * Common values:

     * `application/json`
     * `application/xml`
     * `multipart/form-data`

3. **Accept Header**

   * Tells the server what response format the client expects.
   * Example:

     ```
     Accept: application/json
     ```

4. **User-Agent Header**

   * Identifies the client making the request.
   * Example:

     ```
     User-Agent: Mozilla/5.0
     ```

5. **API Key Header**

   * Sends an API key for authentication.
   * Example:

     ```
     X-API-Key: your_api_key
     ```

6. **Host Header**

   * Specifies the target server.
   * Example:

     ```
     Host: api.example.com
     ```

7. **Accept-Language Header**

   * Indicates the preferred language for the response.
   * Example:

     ```
     Accept-Language: en-US
     ```

8. **Cache-Control Header**

   * Controls how responses are cached.
   * Example:

     ```
     Cache-Control: no-cache
     ```

9. **Cookie Header**

   * Sends cookies stored by the client.
   * Example:

     ```
     Cookie: sessionId=abc123
     ```

10. **Custom Headers**

    * Application-specific headers, often prefixed with `X-` (though modern APIs may use custom names without `X-`).
    * Example:

      ```
      X-Request-ID: 12345
      ```

### Example API Request

```http
POST /users HTTP/1.1
Host: api.example.com
Authorization: Bearer your_token
Content-Type: application/json
Accept: application/json
X-API-Key: abc123

{
  "name": "John",
  "email": "john@example.com"
}
```

### Summary

| Header            | Purpose                               |
| ----------------- | ------------------------------------- |
| `Authorization`   | Authenticates the client              |
| `Content-Type`    | Specifies the request body format     |
| `Accept`          | Specifies the desired response format |
| `User-Agent`      | Identifies the client                 |
| `X-API-Key`       | Provides an API key                   |
| `Host`            | Identifies the destination server     |
| `Accept-Language` | Specifies the preferred language      |
| `Cache-Control`   | Controls caching behavior             |
| `Cookie`          | Sends session or user cookies         |
| Custom Headers    | Carries application-specific metadata |

In short, **headers don't contain the main data** (that's usually in the request body); instead, they tell the server **how to process the request** and **how to format the response**.
