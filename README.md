# Tradexa Django Assignment
**Python Development Intern Assignment — Tradexa Technologies**

## Project Overview
A Django multi-database web application with:
- **`users` app** → Users + Posts (uses `users_db.sqlite3`)
- **`products` app** → Products (uses `products_db.sqlite3`)
- Custom User model with session-based authentication
- Post creation form for authenticated users
- All models registered in Django Admin

---

## Tech Stack
- Python 3.x, Django 5.x
- SQLite (two separate databases)
- HTML/CSS (custom dark theme UI)

---

## Setup Instructions

```bash
# 1. Clone the repo
git clone <your-repo-url>
cd tradexa_project

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install django

# 4. Run migrations (BOTH databases)
python manage.py migrate --database=default
python manage.py migrate --database=products_db

# 5. Create Django admin superuser
python manage.py createsuperuser

# 6. Run the development server
python manage.py runserver
```

---

## Key URLs
| URL | Description |
|-----|-------------|
| `/` | Redirects to login |
| `/login/` | Login page |
| `/register/` | Register page |
| `/dashboard/` | Create posts, view all posts |
| `/products/` | View all products |
| `/admin/` | Django admin panel |

---

## Database Architecture

```
users_db.sqlite3          products_db.sqlite3
├── users_user            └── products_product
└── users_post
```

**ForeignKey (Post → User):** Defined at model level with `db_constraint=False` — no actual database-level constraint is created.

---

## Database Router: `tradexa_project/routers.py`
- `users` app → `default` DB (users_db)
- `products` app → `products_db`

---

## Models

### users app
```python
class User(models.Model):
    first_name, last_name, email, password, username

class Post(models.Model):
    user (ForeignKey, db_constraint=False), text, created_at, updated_at
```

### products app
```python
class Product(models.Model):
    name, weight, price, created_at, updated_at
```
