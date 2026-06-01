# 🛒 AryaCart — Full Stack E-Commerce Store

<div align="center">

![Django](https://img.shields.io/badge/Django-4.2+-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

**A premium, fully-functional e-commerce web application built with Django.**

[Live Demo](https://aryaaman577.pythonanywhere.com) · [Report Bug](https://github.com/aryaaman577/codealpha_tasks/issues) · [Request Feature](https://github.com/aryaaman577/codealpha_tasks/issues)

</div>

---

## 📖 Project Introduction

**AryaCart** is a complete e-commerce platform developed as **Task 1** of the **CodeAlpha Full Stack Web Development Internship**. It demonstrates proficiency in Django, Python, HTML/CSS, JavaScript, and database management by implementing a real-world online shopping experience from scratch.

The application features a stunning dark-themed UI with gold accents, smooth animations, and a responsive design that works seamlessly across desktop and mobile devices.

**Developer:** Aman Gupta | 📞 +91 9936281054 | [GitHub](https://github.com/aryaaman577)

---

## ✨ Features

### Core E-Commerce Features
- ✅ **Product Listings** — 40 products across 8 categories with unique images
- ✅ **Product Details Page** — Full description, price, stock, reviews, related products
- ✅ **Shopping Cart** — Add/remove items, update quantities, apply coupons
- ✅ **User Registration** — Email-based signup with automatic profile creation
- ✅ **User Login/Logout** — Secure session-based authentication
- ✅ **Order Processing** — Complete checkout with address, payment, and confirmation
- ✅ **Database** — SQLite with models for Products, Users, Orders, Cart, Reviews

### Additional Features
- ⭐ **Product Reviews** — 1-5 star rating system with text reviews
- ❤️ **Wishlist** — Save products for later
- 👁️ **Watch History** — Track recently viewed products
- 💳 **Payment Simulation** — Realistic Credit Card, UPI, and Net Banking UI
- 💰 **Coupon System** — Discount codes with percentage-based discounts
- 📧 **Email Notifications** — Order confirmation emails (console-simulated)
- 📱 **Responsive Design** — Mobile-friendly across all pages
- 🎨 **Premium Dark Theme** — Glassmorphism, micro-animations, gold accents
- 🔐 **Admin Panel** — Full Django admin for managing all store data

---

## 🛠️ Installation Steps

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)
- Git

### Setup

```bash
# 1. Clone the repository
git clone https://github.com/aryaaman577/codealpha_tasks.git
cd codealpha_tasks/Task1_AryaCart

# 2. Create a virtual environment
python -m venv venv

# 3. Activate the virtual environment
venv\Scripts\activate         # Windows
# source venv/bin/activate    # macOS/Linux

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run database migrations
python manage.py migrate

# 6. Create an admin account
python manage.py createsuperuser

# 7. Start the development server
python manage.py runserver
```

### Access the Application
| URL | Purpose |
|---|---|
| http://127.0.0.1:8000 | Main website |
| http://127.0.0.1:8000/admin | Admin panel |
| http://127.0.0.1:8000/accounts/register | User registration |
| http://127.0.0.1:8000/accounts/login | User login |

---

## 📁 Project Structure

```
Task1_AryaCart/
├── manage.py                    # Django management script
├── requirements.txt             # Python dependencies
├── Procfile                     # Gunicorn process file
├── render.yaml                  # Render deployment config
├── build.sh                     # Build script
│
├── novacart/                    # Project Configuration
│   ├── settings.py              # Django settings (dev + production)
│   ├── urls.py                  # Root URL configuration
│   ├── wsgi.py                  # WSGI entry point
│   └── asgi.py                  # ASGI entry point
│
├── store/                       # Store App
│   ├── models.py                # Product, Category, Review, Wishlist, WatchHistory
│   ├── views.py                 # Product listing, detail, search, wishlist, reviews
│   ├── urls.py                  # Store URL patterns
│   ├── admin.py                 # Admin configuration
│   └── context_processors.py    # Category context for all templates
│
├── accounts/                    # Accounts App
│   ├── models.py                # UserProfile model
│   ├── views.py                 # Register, login, logout, profile
│   ├── forms.py                 # User registration and profile forms
│   └── signals.py               # Auto-create profile on user creation
│
├── cart/                        # Cart App
│   ├── models.py                # Cart, CartItem, Coupon models
│   ├── views.py                 # Add/remove/update cart, apply coupon
│   └── context_processors.py    # Cart count for navbar badge
│
├── orders/                      # Orders App
│   ├── models.py                # Order, OrderItem models
│   ├── views.py                 # Checkout, payment, order history
│   └── forms.py                 # Checkout form
│
├── pages/                       # Pages App
│   ├── views.py                 # About and Contact pages
│   └── urls.py                  # Pages URL patterns
│
├── templates/                   # HTML Templates
│   ├── base.html                # Base template with navbar and footer
│   ├── store/                   # Store templates (home, product list, detail, etc.)
│   ├── accounts/                # Auth templates (login, register, profile)
│   ├── cart/                    # Cart template
│   ├── orders/                  # Order templates (checkout, payment, history)
│   └── pages/                   # Static pages (about, contact)
│
├── static/                      # Static Assets
│   ├── css/main.css             # Main stylesheet (53KB)
│   ├── css/style.css            # Additional styles
│   └── js/main.js               # JavaScript (toasts, animations, cart AJAX)
│
└── media/                       # Media Files
    └── products/                # 40 unique product images
```

---

## 🗄️ Database Information

**Engine:** SQLite3 (development) / PostgreSQL (production)

### Models Overview

| Model | App | Key Fields | Relationships |
|---|---|---|---|
| `Category` | store | name, slug, image, description | → Products |
| `Product` | store | name, slug, price, description, image, stock, category | → Category, → Reviews |
| `Review` | store | rating (1-5), comment, created_at | → User, → Product |
| `Wishlist` | store | added_at | → User, → Product |
| `WatchHistory` | store | viewed_at | → User, → Product |
| `ProductVariant` | store | size, color, stock | → Product |
| `UserProfile` | accounts | phone, address, city, state, pincode, avatar | → User |
| `Cart` | cart | created_at, coupon | → User, → Coupon |
| `CartItem` | cart | quantity | → Cart, → Product |
| `Coupon` | cart | code, discount_percentage, valid_from, valid_to | — |
| `Order` | orders | total, status, payment_method, address, coupon_code | → User |
| `OrderItem` | orders | quantity, price, variant_details | → Order, → Product |

---

## 📸 Screenshots

> Screenshots of the application can be found by visiting the live demo:
> **[https://aryaaman577.pythonanywhere.com](https://aryaaman577.pythonanywhere.com)**

| Page | Description |
|---|---|
| 🏠 **Home** | Hero section, featured products, category carousel |
| 📦 **Shop** | Product grid with sidebar filters (category, price, sort) |
| 🔍 **Product Detail** | Image, description, reviews, add-to-cart, wishlist |
| 🛒 **Cart** | Item list, quantity controls, coupon input, order summary |
| 💳 **Payment** | Simulated payment with Card/UPI/Net Banking options |
| 📝 **Order History** | Past orders with status badges |
| 👤 **Profile** | User details, edit profile, account management |
| 📋 **About** | Developer information and tech stack |
| 📞 **Contact** | Contact form and developer contact details |
| 🔐 **Admin** | Django admin for managing all data |

---

## 🔮 Future Enhancements

- [ ] Real payment gateway integration (Razorpay/Stripe)
- [ ] Email notifications via SMTP (Gmail)
- [ ] Product image zoom on hover
- [ ] Multi-image product gallery
- [ ] Inventory management with low-stock alerts
- [ ] Customer support chat system
- [ ] Social login (Google, GitHub)
- [ ] PDF invoice generation
- [ ] Advanced search with autocomplete
- [ ] Product comparison feature

---

## 📄 License

This project was developed as part of the **CodeAlpha Full Stack Web Development Internship**.

---

<div align="center">

Made with ❤️ by **Aman Gupta**

📞 +91 9936281054 | 🐙 [GitHub](https://github.com/aryaaman577)

**CodeAlpha Internship — June 2026**

</div>
