# 📦 Automatic Product Catalog Web Application

> Modern, real-time product catalog management for your business.

![Status](https://img.shields.io/badge/status-completed-brightgreen)

---

## 🎬 Demo

Video Demo: _URL HERE_

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