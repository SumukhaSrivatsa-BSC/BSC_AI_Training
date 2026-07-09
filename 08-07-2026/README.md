# Python Requests Library - REST API Practice

This project demonstrates how to interact with REST APIs using Python's `requests` library.

The examples cover:

- GET Request
- POST Request
- PUT Request
- PATCH Request
- DELETE Request
- Query Parameters
- Response Handling
- Status Codes
- Headers
- Exception Handling

---

## Prerequisites

Install the required package:

```bash
pip install requests
```

---

## API Used

This project uses the free testing API:

```text
https://jsonplaceholder.typicode.com
```

JSONPlaceholder is a fake online REST API that can be used for testing and learning purposes.

---

## GET Request

Retrieve data from an API endpoint.

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

print(response.json())
```

### Purpose

- Fetch data from the server
- Read existing resources

---

## POST Request

Create a new resource.

```python
data = {
    "i_d": [1, 2],
    "name": ["Raj", "Sham"]
}

response = requests.post(url, json=data)

print(response.json())
```

### Purpose

- Send data to the server
- Create a new record

---

## Reading Response Information

### Status Code

```python
print(response.status_code)
```

Example Output:

```text
200
```

### Headers

```python
print(response.headers)
```

### JSON Data

```python
print(response.json())
```

---

## PUT Request

Replace an existing resource completely.

```python
put_data = {
    "id": 1,
    "title": "Updated Title",
    "body": "Updated Body",
    "userId": 1
}

put_response = requests.put(url, json=put_data)

print(put_response.status_code)
print(put_response.json())
```

### Purpose

- Update the entire resource
- Existing data is replaced

---

## PATCH Request

Update specific fields of an existing resource.

```python
patch_data = {
    "title": "Patched Title"
}

patch_response = requests.patch(url, json=patch_data)

print(patch_response.status_code)
print(patch_response.json())
```

### Purpose

- Partial update
- Modify only selected fields

---

## DELETE Request

Delete a resource.

```python
delete_response = requests.delete(url)

print(delete_response.status_code)
print(delete_response.json())
```

### Purpose

- Remove an existing resource

---

## GET Request with Query Parameters

Retrieve filtered data.

```python
url = "https://jsonplaceholder.typicode.com/comments"

params = {
    "postId": 1,
    "id": 3
}

response = requests.get(url, params=params)

print(response.json())
```

### Generated URL

```text
https://jsonplaceholder.typicode.com/comments?postId=1&id=3
```

---

## Exception Handling

Always handle API failures gracefully.

```python
import requests

url = "https://example.com"

try:
    result = requests.get(url)
    print(result.json())

except requests.exceptions.RequestException as e:
    print("API call failed:", e)
```

### Benefits

- Prevents program crashes
- Handles network errors
- Handles timeout issues
- Handles invalid responses

---

## Common HTTP Methods

| Method | Purpose |
|----------|----------|
| GET | Retrieve Data |
| POST | Create New Data |
| PUT | Replace Existing Data |
| PATCH | Update Partial Data |
| DELETE | Remove Data |

---

## Common Status Codes

| Status Code | Meaning |
|-------------|----------|
| 200 | OK |
| 201 | Created |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 429 | Too Many Requests |
| 500 | Internal Server Error |

---

## Project Learning Outcomes

After completing this project, you will understand:

- How APIs work
- Client-Server communication
- REST API fundamentals
- CRUD operations using HTTP methods
- Sending request data
- Reading responses
- Working with JSON
- Handling API errors
- Using query parameters effectively

---

## Author

Created as part of API Fundamentals and Python Requests Library practice.
