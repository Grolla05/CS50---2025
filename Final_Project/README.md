# 📦 Inventory Management System with WEB aplication

> Modern, real-time product catalog management for your business.

![Status](https://img.shields.io/badge/status-completed-brightgreen)

---

## 🎬 Demo
Link video - www.youtube.com/watch?v=Cu3hcLSsHNk&feature=youtu.be

---

## 📝 What is this project?

**Automatic Product Catalog Web Application** is a complete solution for managing and viewing product catalogs.
It was developed as a final project for CS50x and allows users to add, edit, remove and list products in an SQLite database through a desktop interface (app) developed in Python, as well as view the catalog in real time through a modern web interface.

---

## 🌍 Application in the Real World

**Use Cases:**  
This project is ideal for e-commerce businesses or entrepreneurs who need an efficient way to manage and display their product catalogs on the web, without relying on complex infrastructure. By combining a simple desktop management tool with a real-time web interface, it streamlines inventory updates and provides customers or employees with instant access to the latest product information. The solution is easy to deploy and maintain, making it accessible even to users with minimal technical knowledge.

---

## 🚀 Highlights

- **Web Frontend:**  
  Built with HTML, Tailwind CSS, and JavaScript for a clean, responsive, and interactive user experience.

- **Backend:**  
  Powered by Flask and Flask-SQLAlchemy (Python) for robust data serving and page rendering.

- **Database:**  
  Uses SQLite for simple, file-based data storage.

- **Desktop Management:**  
  A Python script (`main.py`) for managing products directly in the database (add, edit, remove, list).

- **Live Catalog:**  
  The `/catalog` page displays all products currently in the database, with filtering and sorting features.

---

## 🗂️ Project Structure

```
Grolla05/
├── Software/
│   ├── main.py         # CLI tool for managing the database
│   └── database.db     # SQLite database file
├── WEB/
│   ├── app.py          # Flask web server
│   ├── requirements.txt# Python dependencies
│   ├── static/
│   │   ├── script.js   # JS for frontend interactivity
│   │   └── filtro.js   # JS for catalog filtering/sorting
│   └── templates/
│       ├── layout.html # Base HTML template
│       ├── index.html  # Home page
│       └── catalog.html# Product catalog page
```

---

## 🛠️ How the Project Works: Step by Step

This section provides a detailed explanation of how the project operates, from desktop product management to real-time web catalog viewing.

### 1. **Project Structure**

- **Software/**: Contains the desktop application (`main.py`) and the SQLite database (`database.db`).
- **WEB/**: Contains the Flask web server (`app.py`), dependency files, HTML templates, and static assets (JS/CSS).

### 2. **Product Management via Desktop (`Software/main.py`)**

- The `main.py` script uses the `customtkinter` library to deliver a modern, user-friendly graphical interface.
- Users can:
  - **Add products**: Entering name, quantity, and value.
  - **Remove products**: By specifying the product ID.
  - **Edit products**: Update the name, quantity, or value of existing products.
  - **List products**: View all registered products, with filtering and pagination.
- All operations interact directly with the `database.db` file located in the `Software/` folder.
- The database uses a single table, `products`, with the fields: `Id`, `Name`, `Quantity`, and `Value`.

### 3. **Shared Database**

- The `database.db` file acts as the bridge between the desktop app and the web application.
- Any changes made via the desktop app (add, remove, edit) are instantly reflected on the web, since both access the same database file.

### 4. **Real-Time Web Visualization (`WEB/app.py`)**

- The `app.py` file runs a Flask server that:
  - Connects to the same SQLite database (`../Software/database.db`).
  - Defines a data model (`Item`) matching the `products` table.
  - Provides routes:
    - `/` – Home page, displaying products as cards/carousels.
    - `/catalog` – Full catalog with tables, filters, and sorting.
    - `/api/items` – API endpoint returning all products as JSON.
- HTML templates use Tailwind CSS for a modern, responsive look.
- JavaScript files enable dynamic sorting and navigation of products.

### 5. **Update Flow**

1. The user manages products through the desktop app.
2. Changes are saved to the SQLite database.
3. When the website is accessed, Flask reads the latest data from the database and displays it in real time.
4. There’s no need to restart the server or manually refresh the database—everything stays in sync automatically.

### 6. **Visual Summary**

```
[User] ⇄ [main.py (Desktop)] ⇄ [database.db (SQLite)] ⇄ [app.py (Flask Web)] ⇄ [Browser]
```

---

With this workflow, the project ensures seamless product management and visualization, integrating desktop and web in a simple and efficient way.

---
## ✨ Features

- 📋 **Add, edit, remove, and list products** via the desktop interface.
- 🌐 **Real-time catalog visualization** in the browser.
- 🔎 **Filter and sort products** by value and quantity.
- 💻 **Modern, responsive UI** with Tailwind CSS.
- 🗃️ **Simple deployment** using Python and SQLite.

---

## 👤 Authors

Developed by:

- **Felipe Grolla Freitas** – Control and Automation Engineering Student (PUC-Campinas)

> *"Organize your products, simplify your business."*