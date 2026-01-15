# Little Lemon Restaurant API (Django + DRF)

A backend REST API for a restaurant system that supports **menu management**, **table bookings**, and **order workflows** with authentication and role-based access control. Built with **Django** and **Django REST Framework** to demonstrate production-style API design, permissions, and relational data modeling.

> Portfolio project focused on backend engineering fundamentals: authentication, permissions, clean endpoints, and maintainable structure.

---

## 🚀 Features

- RESTful endpoints for **menu items** and **categories**
- **Table booking / reservation** endpoints
- **Order workflow** endpoints (create, view, manage)
- Authentication + protected routes (role-based access)
- Permissions enforcing allowed actions by user role (customer/manager/delivery)
- Admin support via Django admin
- Clear documentation and repeatable setup

---

## 🧱 Tech Stack

- **Python 3**
- **Django**
- **Django REST Framework**
- **Database:** SQLite (dev) / MySQL (optional)
- **Tools:** Git, GitHub, Postman/Insomnia, Django Admin

---

## 🔐 Roles & Permissions (Summary)

This project follows a typical restaurant API permission model:

- **Public users**
  - Can view menu and categories (read-only)

- **Authenticated customers**
  - Can create bookings (if enabled)
  - Can create/manage their own orders (if enabled)

- **Managers (admin/manager group)**
  - Can create/update/delete menu items & categories
  - Can manage orders and assign delivery (if enabled)

- **Delivery crew**
  - Can view assigned orders and update delivery status (if enabled)

> Note: Exact behavior depends on implementation. See endpoints below.

---

## 📡 API Endpoints (Examples)

> Replace these with your actual routes if yours differ.

### Authentication
- `POST /auth/users/` (register) *(if using Djoser)*
- `POST /auth/jwt/create/` *(JWT login, if using Djoser/SimpleJWT)*
- `POST /api/token/` *(JWT login, if using SimpleJWT directly)*

### Menu & Categories
- `GET /api/categories/`
- `POST /api/categories/` *(manager only)*
- `GET /api/menu-items/`
- `POST /api/menu-items/` *(manager only)*
- `GET /api/menu-items/{id}/`
- `PUT/PATCH/DELETE /api/menu-items/{id}/` *(manager only)*

### Bookings / Reservations
- `GET /api/bookings/`
- `POST /api/bookings/` *(authenticated)*
- `GET /api/bookings/{id}/`
- `DELETE /api/bookings/{id}/` *(owner/manager rules)*

### Orders (Optional, if implemented)
- `GET /api/orders/` *(role-specific visibility)*
- `POST /api/orders/` *(authenticated)*
- `GET /api/orders/{id}/`
- `PUT/PATCH /api/orders/{id}/` *(manager or delivery rules)*

---

## 🗂️ Database Models (High Level)

> Replace/adjust based on your actual models.

- **Category**
  - `title`

- **MenuItem**
  - `title`, `price`, `featured`, `category (FK)`

- **Booking**
  - `user (FK)`, `date`, `time`, `guest_count` *(example fields)*

- **Order** *(optional)*
  - `user (FK)`, `status`, `total`, `created_at`

---

## ⚙️ Setup Instructions

### 1) Clone and enter the project
```bash
git clone <<YOUR_REPO_URL>>
cd <<YOUR_PROJECT_FOLDER>>
