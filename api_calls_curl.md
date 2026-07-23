`curl` is a command-line tool used to send HTTP requests to APIs. It's one of the easiest ways to test APIs without writing code.

## Basic Syntax

```bash
curl [options] URL
```

Example:

```bash
curl https://api.example.com/users
```

This sends a **GET** request by default.

---

## 1. GET Request (Fetch Data)

```bash
curl https://api.example.com/users
```

Response:

```json
[
  {
    "id": 1,
    "name": "Alice"
  }
]
```

---

## 2. POST Request (Create Data)

Use `-X POST` and `-d` to send data.

```bash
curl -X POST https://api.example.com/users \
  -H "Content-Type: application/json" \
  -d '{"name":"John","email":"john@example.com"}'
```

Explanation:

* `-X POST` → HTTP method
* `-H` → Add a header
* `-d` → Send request body

---

## 3. PUT Request (Update Data)

```bash
curl -X PUT https://api.example.com/users/1 \
  -H "Content-Type: application/json" \
  -d '{"name":"John Doe"}'
```

---

## 4. PATCH Request (Partial Update)

```bash
curl -X PATCH https://api.example.com/users/1 \
  -H "Content-Type: application/json" \
  -d '{"email":"new@example.com"}'
```

---

## 5. DELETE Request

```bash
curl -X DELETE https://api.example.com/users/1
```

---

## 6. Add Authentication

### Bearer Token

```bash
curl https://api.example.com/users \
  -H "Authorization: Bearer YOUR_TOKEN"
```

### API Key

```bash
curl https://api.example.com/users \
  -H "X-API-Key: YOUR_API_KEY"
```

---

## 7. Multiple Headers

```bash
curl https://api.example.com/users \
  -H "Authorization: Bearer TOKEN" \
  -H "Accept: application/json" \
  -H "Content-Type: application/json"
```

---

## 8. Query Parameters

Instead of a request body, append parameters to the URL:

```bash
curl "https://api.example.com/users?page=2&limit=10"
```

---

## 9. Pretty Print JSON (Linux/macOS)

```bash
curl https://api.example.com/users | jq
```

`jq` formats JSON to make it easier to read.

---

## Common `curl` Options

| Option    | Purpose                                           |
| --------- | ------------------------------------------------- |
| `-X`      | Specify HTTP method (GET, POST, PUT, etc.)        |
| `-H`      | Add request headers                               |
| `-d`      | Send request body (data)                          |
| `-i`      | Show response headers along with the body         |
| `-v`      | Verbose mode (shows request and response details) |
| `-o file` | Save response to a file                           |
| `-L`      | Follow redirects                                  |

---

## Example: Complete API Call

Suppose an API requires:

* POST request
* Bearer token
* JSON body

```bash
curl -X POST https://api.example.com/orders \
  -H "Authorization: Bearer abc123token" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -d '{
    "productId": 101,
    "quantity": 2
  }'
```

Here's what's happening:

* `POST` → Create a new order.
* `Authorization` → Proves who you are.
* `Content-Type` → Says the body is JSON.
* `Accept` → Requests a JSON response.
* `-d` → Sends the order details.

## Quick Cheat Sheet

```bash
# GET
curl https://api.example.com/users

# POST
curl -X POST URL \
  -H "Content-Type: application/json" \
  -d '{"name":"John"}'

# PUT
curl -X PUT URL \
  -H "Content-Type: application/json" \
  -d '{"name":"John Doe"}'

# DELETE
curl -X DELETE URL

# Bearer Token
curl URL \
  -H "Authorization: Bearer TOKEN"

# API Key
curl URL \
  -H "X-API-Key: API_KEY"
```

Once you're comfortable with `curl`, you'll find that most API examples in documentation (such as REST APIs from GitHub, Stripe, OpenAI, or AWS) become much easier to understand and translate into code in Python, JavaScript, Java, or other languages.
