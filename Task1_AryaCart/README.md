# 🛒 AryaCart — Full Stack E-Commerce Store

**Developer:** Aman Gupta  
**Internship:** CodeAlpha — Full Stack Development, Task 1

---

## ✨ Features

| Feature            | Description                                               |
| ------------------ | --------------------------------------------------------- |
| 🏠 Home Page       | Featured products, latest arrivals, category showcase     |
| 📦 Product Catalog | Browse, filter by category/price, sort by price/name/date |
| 🔍 Search          | Search products by name or description                    |
| 🛒 Shopping Cart   | Add/remove products, update quantities                    |
| 📝 User Accounts   | Register, login, logout, profile management               |
| 📦 Orders          | Checkout, order placement, order history, order tracking  |
| 👁️ Watch History   | Track recently viewed products                            |
| 📂 Categories      | Organized product categories with images                  |
| 🖼️ Product Gallery | Multiple images per product                               |
| 🔐 Admin Panel     | Full Django admin for managing store data                 |

---

## 🛠️ Tech Stack

| Technology | Usage              |
| ---------- | ------------------ |
| Python     | Backend language   |
| Django     | Web framework      |
| SQLite     | Database (default) |
| HTML/CSS   | Frontend templates |
| Bootstrap  | Responsive UI      |
| Pillow     | Image handling     |

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/aryacart.git
cd aryacart
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate       # Windows
# source venv/bin/activate  # macOS/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📁 Folder Structure

```
aryacart/
├── aryacart/          # Project settings & root URL config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── store/              # Product catalog, categories, search
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── context_processors.py
├── accounts/           # User registration, login, profiles
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── signals.py
│   └── admin.py
├── cart/               # Shopping cart functionality
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── orders/             # Checkout, order management
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── admin.py
├── pages/              # Static pages (about, contact)
│   ├── views.py
│   └── urls.py
├── templates/          # HTML templates
├── static/             # Static files (CSS, JS, images)
├── media/              # User-uploaded files
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🔑 Admin Panel

Access the Django admin at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) to manage:

- Categories & Products
- Users & Profiles
- Orders & Order Items
- Cart data
- Watch History

---

> Made with ❤️ by **Aman Gupta** | **CodeAlpha Internship**
