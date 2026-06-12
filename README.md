# Tradexa Django Assignment

> A Django multi-database web application built as part of the **Python Development Intern Assignment** for Tradexa Technologies.

---

## Project Overview

This project demonstrates a clean Django architecture with two separate SQLite databases, session-based authentication, custom user models, and a fully functional admin panel.

The application is divided into two Django apps:

| App | Responsibility | Database |
|---|---|---|
| `users` | Custom User model + Post creation | `users_db.sqlite3` |
| `products` | Product catalog management | `products_db.sqlite3` |

---

## Features

- **Custom User Authentication** — Register, login, and logout with session-based auth (no Django's built-in `AbstractUser`)
- **Post Management** — Authenticated users can create and view posts via the dashboard
- **Product Listing** — Browse all products stored in a separate database
- **Multi-Database Architecture** — Two isolated SQLite databases with a custom database router
- **Django Admin Integration** — All models registered and accessible via `/admin/`
- **Dark Theme UI** — Custom HTML/CSS frontend with a clean dark aesthetic

---

## Tech Stack

- **Backend:** Python 3.x, Django 5.x
- **Database:** SQLite (two separate instances)
- **Frontend:** HTML5, CSS3 (custom dark theme), JavaScript
- **Tools:** Django ORM, Django Admin, Session Middleware

---


## Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Manojg14/tradexa_assignment.git
cd tradexa_assignment
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv


# On Windows
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install django
```

### 4. Run Migrations for Both Databases

```bash
python manage.py migrate --database=default
python manage.py migrate --database=products_db
```

### 5. Create a Superuser (for Admin Panel)

```bash
python manage.py createsuperuser
```

### 6. Start the Development Server

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000]

---

## URL Reference

| URL | Description |
|---|---|
| `/` | Redirects to login page |
| `/login/` | User login |
| `/register/` | New user registration |
| `/dashboard/` | Create posts & view all posts |
| `/products/` | View all products |
| `/admin/` | Django admin panel |

---

## Database Architecture

```
users_db.sqlite3              products_db.sqlite3
├── users_user                └── products_product
└── users_post
```

The `Post` model has a `ForeignKey` to `User`, but since they reside in the same database (`users_db`), the relationship is seamless. The key is set with `db_constraint=False` to keep it clean across the multi-database setup.

### Database Router (`tradexa_assignment/routers.py`)

| App | Routed To |
|---|---|
| `users` | `default` → `users_db.sqlite3` |
| `products` | `products_db` → `products_db.sqlite3` |

---

## Data Models

### `users` App

```python
class User(models.Model):
    first_name  = models.CharField(...)
    last_name   = models.CharField(...)
    email       = models.EmailField(unique=True)
    username    = models.CharField(unique=True)
    password    = models.CharField(...)  # hashed

class Post(models.Model):
    user        = models.ForeignKey(User, db_constraint=False, ...)
    text        = models.TextField()
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
```

### `products` App

```python
class Product(models.Model):
    name        = models.CharField(...)
    weight      = models.FloatField()
    price       = models.DecimalField(...)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
```

---

## Author

**Manoj G**

### GitHub : [GitHub](https://github.com/Manojg14)

---

