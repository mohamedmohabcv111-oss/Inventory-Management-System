<div align="center">
  <h1>Inventory Management System (OOP - Python)</h1>
  <p><i>A command-line Inventory Management System built in Python to demonstrate a full, practical application of Object-Oriented Programming principles.</i></p>

  ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
  ![OOP](https://img.shields.io/badge/Object--Oriented_Programming-239120?style=for-the-badge)
  ![CLI](https://img.shields.io/badge/CLI-Command_Line_Interface-4D4D4D?style=for-the-badge&logo=gnu-bash&logoColor=white)

</div>

---

This project was built as a hands-on learning exercise to strengthen core OOP concepts through a real-world style system rather than isolated examples.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [OOP Concepts Demonstrated](#oop-concepts-demonstrated)
- [Project Structure](#project-structure)
- [Class Breakdown](#class-breakdown)
- [How the Program Works](#how-the-program-works)
- [Getting Started](#getting-started)
- [Example Usage Flow](#example-usage-flow)
- [Possible Future Improvements](#possible-future-improvements)
- [Author](#author)

---

## Overview
This system simulates the core operations of a small inventory-based business: employees can log in, register suppliers, add products across multiple categories, apply discounts, and view inventory data. Guests can browse public inventory and supplier information without needing an account.

The project is intentionally structured to mirror a real system's architecture — separating concerns across dedicated classes, protecting sensitive data through encapsulation, and using abstraction and inheritance to keep the codebase scalable and DRY.

---

## Features
- **Employee account creation and authentication** (login/logout)
- **Role-gated actions** — certain operations are only available to logged-in employees
- **Guest mode** with restricted, public-only access
- **Support for three product categories:** Food, Electronic, and Clothing
- **Supplier registration and management**, with public and private information views
- **Discount system** applied per product
- **Increase product quantity** directly from the employee menu
- **Product search** by category and name
- **Full inventory view** (employee-only) vs. **public inventory view** (guest-accessible)
- **Custom exception handling** for invalid input and unauthorized access

---

## OOP Concepts Demonstrated

| Concept | Where It's Used |
|---------|-----------------|
| **Classes & Objects** | `Employee`, `Product`, `Supplier`, `Inventory`, and all product subclasses. |
| **Encapsulation** | Private attributes (e.g. `__password`, `__price`, `__quantity`, `__supplierid`) accessed only through controlled methods. |
| **Abstraction** | `Product` is an abstract base class defining a shared contract via `@abstractmethod`. |
| **Inheritance** | `FoodProduct`, `ElectronicProduct`, and `ClothingProduct` all inherit from `Product`. |
| **Polymorphism** | Each product subclass overrides `get_public_info()` and `settinginfo()` differently, called uniformly through the `Inventory` class. |
| **Interfaces** | A Discount interface (`IDiscountable`) is implemented by all product classes, requiring an `Add_Discount()` method. |
| **Constructors** | Every class uses `__init__` for setup, with subclasses using explicit parent constructor calls. |
| **Exception Handling** | Custom validation using `ValueError` and `PermissionError` for invalid input and unauthorized access attempts. |

---

## Project Structure

```text
Inventory-Management-System/
│
├── classes/
│   ├── Product.py               # Abstract base class for all products
│   ├── FoodProduct.py           # Food category product
│   ├── ElectronicProduct.py     # Electronic category product
│   ├── ClothingProduct.py       # Clothing category product
│   ├── Employee.py              # Employee accounts, login/logout, authentication
│   ├── Supplier.py              # Supplier registration and info management
│   ├── Inventory.py             # Central inventory management logic
│   ├── Customer.py              # Customer records
│   └── Order.py                 # Order handling logic
│
├── Interfaces/
│   └── IDiscountable.py         # Discount interface implemented by all products
│
├── main.py                      # Program entry point and menu-driven interface
└── README.md
```

---

## Class Breakdown

### `Product` (Abstract Base Class)
Defines the shared blueprint for every item in the inventory: ID, name, price, quantity, and linked supplier. Encapsulates sensitive fields and declares abstract methods (`settinginfo`, `get_public_info`) that every subclass must implement.

### `FoodProduct`, `ElectronicProduct`, `ClothingProduct`
Each inherits from `Product` and implements category-specific fields (e.g. expiration date and storage temperature for food; warranty and power rating for electronics; size, color, and material for clothing). Each also implements the `Discount` interface.

### `Employee`
Handles account creation, login/logout, and authentication state. Employee credentials are private and only exposed through controlled, validated methods.

### `Supplier`
Stores supplier information with separate public and private data views, gated by employee authentication.

### `Inventory`
The central manager for all product categories. Handles adding products, searching, and viewing inventory — with permission checks enforced before any employee-only action executes.

### `IDiscountable` (Interface)
A pure interface defining the `Add_Discount()` contract that all product classes must implement, independent of the `Product` inheritance chain.

---

## How the Program Works
The system runs as a menu-driven command-line application with three entry points:
1. **Create Employee Account** — registers a new employee and immediately logs them in
2. **Login** — authenticates an existing employee by name and password
3. **Continue as Guest** — grants limited, read-only access to public data

Once authenticated, employees unlock a full menu of actions: viewing their profile, registering suppliers, adding new products, applying discounts, viewing full inventory details, and searching for products. Guests are restricted to public inventory browsing and supplier lookups.

All sensitive actions are protected with `try/except` blocks that catch `PermissionError` (unauthorized access) and `ValueError` (invalid input), ensuring the program handles bad input and unauthorized attempts gracefully instead of crashing.

---

## Getting Started

### Requirements
- **Python 3.8 or higher** (no external dependencies required)

### Running the Project
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd Inventory-Management-System
   ```
3. Run the application:
   ```bash
   python main.py
   ```

Follow the on-screen menu prompts to create an account, log in, or continue as a guest.

---

## Example Usage Flow
1. Run `main.py`.
2. Choose **Create Your Employee Account**.
3. Enter a name and password.
4. From the employee menu, choose **Add New Product**.
5. Register supplier details, then select a product category and enter its details.
6. Choose **View All The Inventory** to confirm the product was added successfully.
7. Log out, or continue exploring other options.

---

## Possible Future Improvements
- [ ] **Persistent storage** (saving data to a file or database instead of in-memory lists).
- [ ] **Password hashing** for stronger security.
- [ ] **Graphical or web-based interface** to replace the CLI.
- [ ] **Unit tests** for each class.
- [ ] **Order and customer management** fully integrated into the main menu flow.

---

## Author
Built as a personal learning project to strengthen my understanding of Object-Oriented Programming in Python through practical application rather than isolated exercises.
