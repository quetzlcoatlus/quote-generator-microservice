# Citation
Code source: adapted from @LastGregStanding's unit converter microservice
Date: 02/14/2026
URL: https://github.com/LastGregStanding/unit-conversion-microservice

# Quote Generator Microservice

## Supported Categories
- motivational: random motivational quote
- health: random health fact
- video_game: random video game quote

## Setup
1. Install Flask
   ```
   pip install flask
   ```
2. Run the microservice (it will start on localhost:5004)
   ```
   python main.py
   ```

## How to Use

Example using category as motivational.

### Request:
```
{
  "category": "motivation",
}
```
### Success Response (200):
```
{
  "quote": random_quote: str,
  "source": associated_source: str
}
```

### Error Response (400):
```
{
  "error": "Category not supported"
}
```

### Python Code Example:
```
import requests

PORT=5004
DOMAIN='http://localhost:5004/quote'

# category domain:
# 'motivational', 'health', and 'video_game'

result = requests.post(
    DOMAIN,
    json={'category': 'motivational'}
)

quote = result.json()
print(quote) # Output will be a JSON random quote and source
```

### Notes:
- Set of 5 quotes (as of writing) for each category
