# 🛒 AryaCart — Full Stack E-Commerce Store

**Developer:** Aman Gupta  
**Internship:** CodeAlpha — Full Stack Development, Task 1  

---

## ⚡ Quick Start: Run Locally

To run the e-commerce store locally on your PC, follow these simple steps:

### Option A: Go Live Folder (Recommended & Fastest) 🚀
1. Open the **`Go_Live`** folder manually, or double-click the **`Open_Go_Live_Folder.bat`** script in this folder.
2. Inside that folder, double-click **`Go_Live.bat`** (or open **`Go_Live.html`**).
3. The launcher will automatically ensure the local Django server is running and instantly redirect you to the website in your default browser.

### Option B: Automatic Launcher
1. Double-click the **`Run_And_Open_AryaCart.bat`** file in this folder.
2. The launcher will automatically start the backend server in the background and open the website in your default browser.

### Option C: Manual Command Line
1. Open PowerShell or Command Prompt in this folder.
2. Run the development server:
   ```bash
   python manage.py runserver
   ```
3. Keep the command window open and use the local links in the directory below.

---

## 📂 Page Directory (Local vs Live)

Once the local server is running (using Option A or B above), you can use the links below to access all different pages of **AryaCart** either locally or via the live deployed link.

| Page Name | Local Access Link | Live Online Link |
|---|---|---|
| 🏠 **Home Page** | [http://127.0.0.1:8000/](http://127.0.0.1:8000/) | [https://aryaaman577.pythonanywhere.com/](https://aryaaman577.pythonanywhere.com/) |
| 📦 **Shop Catalog** | [http://127.0.0.1:8000/products/](http://127.0.0.1:8000/products/) | [https://aryaaman577.pythonanywhere.com/products/](https://aryaaman577.pythonanywhere.com/products/) |
| 💻 **Product Details** | [http://127.0.0.1:8000/product/macbook-pro-m3/](http://127.0.0.1:8000/product/macbook-pro-m3/) | [https://aryaaman577.pythonanywhere.com/product/macbook-pro-m3/](https://aryaaman577.pythonanywhere.com/product/macbook-pro-m3/) |
| 🛒 **Shopping Cart** | [http://127.0.0.1:8000/cart/](http://127.0.0.1:8000/cart/) | [https://aryaaman577.pythonanywhere.com/cart/](https://aryaaman577.pythonanywhere.com/cart/) |
| 👤 **User Profile** | [http://127.0.0.1:8000/accounts/profile/](http://127.0.0.1:8000/accounts/profile/) | [https://aryaaman577.pythonanywhere.com/accounts/profile/](https://aryaaman577.pythonanywhere.com/accounts/profile/) |
| 🔑 **Login Page** | [http://127.0.0.1:8000/accounts/login/](http://127.0.0.1:8000/accounts/login/) | [https://aryaaman577.pythonanywhere.com/accounts/login/](https://aryaaman577.pythonanywhere.com/accounts/login/) |
| 📝 **Register Page** | [http://127.0.0.1:8000/accounts/register/](http://127.0.0.1:8000/accounts/register/) | [https://aryaaman577.pythonanywhere.com/accounts/register/](https://aryaaman577.pythonanywhere.com/accounts/register/) |
| ℹ️ **About Page** | [http://127.0.0.1:8000/pages/about/](http://127.0.0.1:8000/pages/about/) | [https://aryaaman577.pythonanywhere.com/pages/about/](https://aryaaman577.pythonanywhere.com/pages/about/) |
| 📞 **Contact Page** | [http://127.0.0.1:8000/pages/contact/](http://127.0.0.1:8000/pages/contact/) | [https://aryaaman577.pythonanywhere.com/pages/contact/](https://aryaaman577.pythonanywhere.com/pages/contact/) |
| 🔐 **Admin Panel** | [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) | [https://aryaaman577.pythonanywhere.com/admin/](https://aryaaman577.pythonanywhere.com/admin/) |

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
