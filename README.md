# Fizz-Buzz REST Server

## Overview

This is a production-ready Fizz-Buzz REST Server implemented in Python using the Flask framework. The server follows the classic Fizz-Buzz logic and includes a statistical endpoint.

## Special Build Instructions

1. Ensure that Python is installed on your system.
2. Install the required dependencies using the following command:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the server using the following command:

    ```bash
    python main.py
    ```

The server will be accessible at `http://127.0.0.1:5000/`.

## Third-Party Libraries

- **Flask**: Used as the web framework to handle HTTP requests and responses.

## API Documentation

The API documentation, generated using Swagger, is available at [API Documentation](<https://pypi.org/project/flask-swagger/>).

## Endpoints

### Fizz-Buzz Endpoint

**Request:**

- `GET /fizzbuzz?int1={int1}&int2={int2}&limit={limit}&str1={str1}&str2={str2}`

**Response:**

```json
{
  "result": ["1", "2", "fizz", "4", "buzz", "fizz", "7", "8", "fizz", "buzz", "11", "fizz", "13", "14", "fizzbuzz", ...]
}
