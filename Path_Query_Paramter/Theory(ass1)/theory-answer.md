# Path Parameters:
## What are path parameters in FastAPI?
- In FastAPI, path parameters are parts of the URL path that can change and are used to capture specific values provided by the client. They are denoted by curly braces `{}` within the route definition. Path parameters allow you to define routes that accept dynamic values, making your API more flexible and powerful.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```

- In this example, `{item_id}` is a path parameter. When a request is made to `/items/123`, FastAPI will capture `123` as the value for `item_id` and pass it to the `read_item` function.

## How are path parameters defined in FastAPI route declarations?
- In FastAPI route declarations, path parameters are defined by including them directly within the URL path as part of the route's endpoint definition. Path parameters are enclosed in curly braces `{}`.

```python
from fastapi import FastAPI

app = FastAPI()

@app.method("/route/{parameter_name}")
async def endpoint_name(parameter_name: parameter_type):
```

## Can path parameters have default values? If yes, how can they be set?
- No, path parameters do not have default values. Path parameters are typically used to capture dynamic values from the URL path, and they must be provided in the request URL.
- However, you can define multiple endpoints with different routes, some including path parameters and others without, to handle different scenarios.

## Provide an example of a FastAPI route with path parameters.
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```

- The route is defined using `@app.get("/items/{item_id}")`.
- `{item_id}` is the path parameter.
- When a request is made to a URL like `/items/123`, FastAPI will capture `123` as the value for `item_id`, convert it to an integer, and pass it to the `read_item` function.

# Query Parameters:
## What are query parameters in FastAPI?
- Query parameters are additional parameters appended to the URL after a question mark `?` and separated by ampersands `&`. They are used to provide optional data to an endpoint and are typically used for filtering, sorting, or providing additional options to the client.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/")
async def read_items(category: str = None, page: int = 1, sort: str = None):
    return {"category": category, "page": page, "sort": sort}
```

- `/items/` is the route for the endpoint.
- `category`, `page`, and `sort` are query parameters.
- Each parameter has a default value specified (`None` for `category` and `sort`, and `1` for `page`).
- FastAPI will automatically parse any query parameters provided in the request URL and pass them to the `read_items` function as arguments. If a query parameter is not provided, it will use the default value specified in the function signature.

## How are query parameters defined in FastAPI route declarations?
- Query parameters are defined as function parameters in the endpoint function signature.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/")
async def read_items(category: str = None, page: int = 1, sort: str = None):
    """
    Endpoint to retrieve items with optional query parameters.
    """
```

- When a request is made to the endpoint `/items/`, FastAPI will automatically parse any query parameters provided in the URL and pass them to the `read_items` function as arguments. If a query parameter is not provided in the request, the default value specified in the function signature will be used.

## What is the difference between path parameters and query parameters?

| Aspect                  | Path Parameters                                         | Query Parameters                                         |
|-------------------------|---------------------------------------------------------|-----------------------------------------------------------|
| Location in URL         | Part of the URL path                                    | Appended to the end of the URL after a `?`                |
| Syntax                  | Enclosed in curly braces `{}` within the URL path        | Key-value pairs separated by `&` after a `?`              |
| Usage                   | Identifies specific resources or endpoints              | Provides additional data for filtering, sorting, etc.     |
| Requirement             | Required in the URL path for endpoint matching           | Optional, can be omitted from the URL                     |
| Example URL             | `/users/{user_id}`                                      | `/search?query=term&page=1`                               |
| Example Usage in Python | ```python                                                | ```python                                                |
|                         | @app.get("/users/{user_id}")                            | @app.get("/search")                                      |
|                         | async def get_user(user_id: int):                       | async def search_items(query: str, page: int = 1):       |

- This table summarizes the key differences between path parameters and query parameters in terms of their location in the URL, syntax, usage, requirement, and provides examples of their usage in FastAPI route declarations.

## Can query parameters have default values? If yes, how can they be set?

- Yes, query parameters in FastAPI can have default values, and they are set by providing default values in the function signature of the endpoint.
- You can set default values for query parameters in FastAPI by simply providing the default value in the function signature, similar to how you set default values for regular function parameters in Python.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/")
async def read_items(category: str = "electronics", page: int = 1, sort: str = "name"):
    """
    Endpoint to retrieve items with optional query
```
## Provide an example of a FastAPI route with query parameters.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/")
async def read_items(category: str = None, page: int = 1, sort: str = None):
    """
    Endpoint to retrieve items with optional query parameters.
    """
    return {"category": category, "page": page, "sort": sort}
```

# Combining Path and Query Parameters:
## Can a FastAPI route have both path parameters and query parameters? If yes, provide an example.


- Yes, a FastAPI route can have both path parameters and query parameters. 

```python 
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int, category: str = None, page: int = 1, sort: str = None):
    """
    Endpoint to retrieve an item with optional query parameters.
    """
    return {"item_id": item_id, "category": category, "page": page, "sort": sort}
```
## What is the order of precedence if a parameter is defined both in the path and as a query parameter?

- FastAPI will prioritize the values provided in the path parameters over those provided as query parameters. The query parameter will be used if no corresponding path parameter is present.

# Data Types and Validation:
## How does FastAPI handle data types and validation for path and query parameters?

- FastAPI provides automatic data type conversion and validation for both path and query parameters.
- Cases when data type does not match or fails validation, FastAPI automatically returns an error response with details about the validation error. The error response includes information about which parameter failed validation, the expected data type, and any additional validation rules that were violated.

## What are some common data types that can be used for path and query parameters?

1. **Path Parameters**: int, float, str

2. **Query Parameters**: int, float, str, bool, datetime, list, set, tuple

## How can you enforce validation rules on path and query parameters in FastAPI?

- Validation rules on path and query parameters can be enforced using Python type hints and Pydantic models. Pydantic is a data validation library that FastAPI integrates with, allowing you to define data structures with validation rules easily. It allows you to specify data types, validation rules, default values, and more for your parameters. FastAPI automatically validates incoming requests against these models and returns appropriate error responses if validation fails.

# Usage and Benefits:
##  In what scenarios would you use path parameters over query parameters, and vice versa?

- Path parameters are used when the parameter is essential for identifying the resource or endpoint and contributes to the URL's hierarchical structure. For instance, /users/{user_id} is a clear indication that the endpoint retrieves a specific user based on their ID.
- Query parameters are used for optional filtering, sorting, or pagination purposes, offering flexibility and convenience without affecting the URL's semantic meaning. For example, /items?category=electronics&page=1 allows users to filter items by category and paginate through the results

## What are the benefits of using path and query parameters in API design?
**Benefits of Path Parameters:**

1. Path parameters are crucial for identifying specific endpoints within the API.

2. Path parameters contribute to a clean and meaningful URL structure, making it easier for users to understand and navigate the API.

3. Path parameters enhance the semantic clarity of the API endpoints by directly incorporating essential parameters into the URL path.

4. Search engines often prioritize URLs that contain meaningful path parameters, leading to potential SEO benefits by improving the discoverability and ranking of API endpoints.

**Benefits of Query Parameters:**

1. Query parameters offer flexibility and customization options by allowing users to pass additional parameters without affecting the URL structure. They enable users to tailor API requests based on their specific requirements.

2. It allows users to include additional information such as filters, sorting criteria, or pagination parameters as needed.

3. Query parameters are easy to use and understand, as they appear after the "?" symbol in the URL and can be appended or modified without impacting the URL hierarchy.

## Can you provide examples of real-world use cases where path and query parameters would be employed effectively?
- Path parameters to retrieve product details in e-commerce. For instance, /products/{product_id} can be used to fetch information about a particular product based on its unique identifier.
- While query parameters can be used to filter search results based on various criteria. For instance, /products?category=electronics&brand=Apple can filter products by category and brand.


# Error Handling
## How does FastAPI handle errors related to missing or invalid path/query parameters
- FastAPI automatically handles errors related to missing or invalid path/query parameters by providing informative error messages and appropriate HTTP status codes.
**Missing Parameters:**
- If a required path parameter is missing from the request URL, FastAPI returns a 422 Unprocessable Entity error response. The response includes details about the missing parameter, making it easy for the client to identify and rectify the issue.
- Similarly, if a required query parameter is missing, FastAPI returns a 422 Unprocessable Entity error response with details about the missing parameter.

**Invalid Parameters:**
- If a path or query parameter fails validation (e.g., due to incorrect data type, etc.), FastAPI automatically returns a 422 Unprocessable Entity error response. The response includes details about the validation error, such as the parameter name, expected data type, and any additional validation rules that were violated.

**Custom Error Handling:**
- FastAPI allows for custom error handling using exception handling mechanisms. You can define custom exception handlers to intercept and handle specific types of errors gracefully, providing custom error responses as needed.

## Can you customize error responses for cases where required parameters are missing or validation fails?
- Yes, you can customize error responses for cases where required parameters are missing or validation fails. This customization can be achieved by defining custom exception handlers to intercept specific types of errors and provide custom error responses.
