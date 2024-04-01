
## Code Writing: Path Parameters

### Description
Write a FastAPI route that accepts a path parameter for user identification (user_id) and returns the user's profile information.

### Implementation
```python
from fastapi import FastAPI

app = FastAPI()
users = {
    1: {"username": "Cozyamy", "email": "cozy@example.com"},
    2: {"username": "Haybee", "email": "haybee@example.com"}
}

@app.get("/users/{user_id}")
async def get_user_profile(user_id: int):
    """
    Retrieve the profile information of a user by user_id.
    """
    if user_id not in users:
        return {"error": "User not found"}
    return users[user_id]
```

## Code Writing: Path Parameters with Error Handling

### Description
Implement error handling for the case when the user_id path parameter is missing.

### Implementation
```python
from fastapi import FastAPI, HTTPException

app = FastAPI()
users = {
    1: {"username": "Cozyamy", "email": "cozy@example.com"},
    2: {"username": "Haybee", "email": "haybee@example.com"}
}

@app.get("/users/{user_id}")
async def get_user_profile(user_id: int):
    """
    Retrieve the profile information of a user by user_id.
    """
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return users[user_id]
```

## Code Writing: Query Parameters

### Description
Create a FastAPI route that accepts query parameters for filtering a list of products by category and price range.

### Implementation
```python
from typing import Annotated
from fastapi import FastAPI, Query 

app = FastAPI()
products_data = [
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 150000},
    {"id": 2, "name": "Phone", "category": "Electronics", "price": 90000}
]

@app.get("/products/")
async def get_products(
    category_filter: Annotated[str | None, Query(description="Filter products by category")] = None,
    price_range_filter: Annotated[str | None, Query(description="Price range (format: 'min-max')")] = None,
):
    """
    Retrieve a list of products filtered by category and price range.
    """
    filtered_products = products_data

    if category_filter:
        filtered_products = [product for product in filtered_products if product["category"] == category_filter]

    if price_range_filter is not None:
        min_price, max_price = map(float, price_range_filter.split('-'))
        filtered_products = [product for product in filtered_products if min_price <= product["price"] <= max_price]

    return filtered_products
```

# FastAPI: Query Parameters with Default Values

## Code Writing: Query Parameters with Default Values

### Description
Implement default values for the query parameters (category defaulting to 'all' and price_range defaulting to a specific range).

### Implementation
```python
from typing import Annotated
from fastapi import FastAPI, Query 

app = FastAPI()
products_data = [
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 1500},
    {"id": 2, "name": "Phone", "category": "Electronics", "price": 900}
]

@app.get("/products/")
async def get_products(
    category: Annotated[str, Query(default='all', description="Filter products by category")] = 'all',
    price_range: Annotated[str, Query(default='0-1000', description="Price range (format: 'min-max')")] = '0-1000',
):
    """
    Retrieve a list of products filtered by category and price range.
    """
    min_price, max_price = map(float, price_range.split('-'))

    filtered_products = [
        product for product in products_data
        if (category == 'all' or product["category"] == category) and min_price <= product["price"] <= max_price
    ]

    return filtered_products
```

## Combining Path and Query Parameters

### Description
Write a FastAPI route that accepts a path parameter for city (city_id) and query parameters for filtering restaurants by cuisine type (cuisine) and rating (min_rating).

### Implementation
```python
from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

restaurants = [
    {"id": 1, "name": "Restaurant A", "city_id": 1, "cuisine": "Italian", "rating": 4.5},
    {"id": 2, "name": "Restaurant B", "city_id": 1, "cuisine": "Mexican", "rating": 4.2}
]

@app.get("/restaurants/{city_id}")
async def get_restaurants(
    city_id: int,
    cuisine: Annotated[str | None, Query(description="Filter restaurants by cuisine type")] = None,
    min_rating: Annotated[float | None, Query(description="Filter restaurants by minimum rating")] = None,
):
    """
    Retrieve a list of restaurants in a city filtered by cuisine type and minimum rating.
    """
    filtered_restaurants = [
        restaurant for restaurant in restaurants
        if restaurant["city_id"] == city_id
        and (cuisine is None or restaurant["cuisine"].lower() == cuisine.lower())
        and (min_rating is None or restaurant["rating"] >= min_rating)
    ]

    return filtered_restaurants
```

## Combining Path and Query Parameters with Default Values

### Description
Ensure that the city ID is a path parameter while cuisine type and minimum rating are query parameters.

### Implementation
```python
from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

restaurants = [
    {"id": 1, "name": "Restaurant A", "city_id": 1, "cuisine": "Italian", "rating": 4.5},
    {"id": 2, "name": "Restaurant B", "city_id": 1, "cuisine": "Mexican", "rating": 4.2}
]

@app.get("/restaurants/{city_id}")
async def get_restaurants(
    city_id: int,
    cuisine: Annotated[str | None, Query(description="Filter restaurants by cuisine type")] = None,
    min_rating: Annotated[float | None, Query(description="Filter restaurants by minimum rating")] = None,
):
    """
    Retrieve a list of restaurants in a city filtered by cuisine type and minimum rating.
    """
    filtered_restaurants = [
        restaurant for restaurant in restaurants
        if restaurant["city_id"] == city_id
        and (cuisine is None or restaurant["cuisine"].lower() == cuisine.lower())
        and (min_rating is None or restaurant["rating"] >= min_rating)
    ]

    return filtered_restaurants
```

# FastAPI: Data Validation and Parameter Usage

## Data Validation

### Description
Modify an existing FastAPI route that accepts a path parameter for user_id to ensure that user_id is an integer and greater than zero.

```python
from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/users/{user_id}")
async def get_user(user_id: int = Path(..., title="The ID of the user to retrieve", gt=0)):
    """
    Retrieve user information by user ID.
    The ... is a placeholder indicating that user_id is required.
    The title parameter provides a description for user_id.
    The gt=0 parameter ensures that user_id is greater than zero. If user_id is not provided or is not an integer greater than zero, FastAPI will return a validation error.
    """
    return {"user_id": user_id}
```

### Add validation to a query parameter start_date to ensure it is a valid date format.

```python
from fastapi import FastAPI, Query
from datetime import datetime

app = FastAPI()

def is_valid_date(date_string):
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False

@app.get("/items/")
async def read_items(start_date: str = Query(..., description="Start date in YYYY-MM-DD format")):
    """
    Retrieve items based on start date.
    """
    if not is_valid_date(start_date):
        raise ValueError("Invalid date format. Please provide the start date in YYYY-MM-DD format.")

    return {"start_date": start_date}
```

## Usage and Benefits

### Description
Analyze a given FastAPI application and identify instances where using path parameters would be more appropriate than query parameters, and vice versa. Discuss the benefits of using path and query parameters in the provided FastAPI application and how it enhances API design.

```python
from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()

products = [
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 1500},
    {"id": 2, "name": "Phone", "category": "Electronics", "price": 900},
]

orders = [
    {"id": 1, "product_id": 1, "quantity": 2, "status": "pending"},
    {"id": 2, "product_id": 2, "quantity": 1, "status": "completed"}
]

@app.get("/products/{product_id}")
async def get_product(product_id: int):
    """
    Retrieve product information by product ID.
    """
    for product in products:
        if product["id"] == product_id:
            return product
    return {"error": "Product not found"}

@app.get("/orders/")
async def get_orders(
    product_id: int,
    status: Annotated[str | None, Query(description="Filter orders by status")] = None
):
    """
    Retrieve orders by a specific product with optional status filter.
    """
    orders_by_product = [order for order in orders if order["product_id"] == product_id]
    if status:
        orders_by_product = [order for order in orders_by_product if order["status"] == status]
    return orders_by_product
```

### Path Parameters vs. Query Parameters

**Path Parameters:**
- **Use:** Path parameters are used in the route "/products/{product_id}" to retrieve product information by a specific product ID.
- **Benefit:** Adding the product_id directly into the URL path identifies the resource (product) requested, ensuring the correct product information is retrieved based on the provided ID.

**Query Parameters:**
- **Use:** Query parameters are used in the route "/orders/" to filter orders by a specific product and an optional status.
- **Benefit:** Query parameters provide a flexible way to modify the results returned by an endpoint without altering the URL structure. Clients can customize the response based on their specific requirements without filling up the URL path.

Using a combination of path and query parameters enhances API design by providing a well-structured, flexible, and intuitive interface for clients to interact with the API.