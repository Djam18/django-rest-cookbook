# Django REST Cookbook - learning DRF

learning django rest framework

## Setup

```
pip install -r requirements.txt
cd core
python manage.py migrate
python manage.py runserver
```

## API Endpoints

### Products

- GET /api/products/ - list all products
- POST /api/products/ - create product (admin only)
- GET /api/products/{id}/ - get one product
- PUT /api/products/{id}/ - update product (admin only)
- DELETE /api/products/{id}/ - delete product (admin only)

### Auth

- POST /api/token/ - get auth token
  - body: {"username": "...", "password": "..."}
  - returns: {"token": "..."}

## Usage

Get token:
```
curl -X POST http://localhost:8000/api/token/ -d "username=admin&password=admin"
```

Use token:
```
curl http://localhost:8000/api/products/ -H "Authorization: Token <your_token>"
```

## Notes

- uses sqlite3 for dev
- token auth only, no session auth on the API
- admin users can write, everyone can read
