# WhiteHub CLI

WhiteHub CLI is a simple Python terminal project that combines multiple small systems into one organized command-line app.

## Features

- User registration
- User login
- Password hashing using bcrypt
- JSON-based data storage
- Hospital patient management system
- Store and cart system

## Project Structure

```text
WhiteHub CLI/
│
├── main.py
│
├── auth/
│   ├── __init__.py
│   ├── login.py
│   └── security.py
│
├── data/
│   ├── users.json
│   ├── patients.json
│   ├── products.json
│   └── carts.json
│
├── systems/
│   ├── __init__.py
│   ├── hospital.py
│   └── store.py
│
└── utils/
    ├── __init__.py
    └── json_utils.py
```

## How It Works

The program starts from `main.py`.

The user can register or login.  
After logging in, the user can access the dashboard and choose between:

1. Hospital System
2. Store System
3. Logout

## Hospital System

The hospital system allows the user to:

- Add a patient
- Show all patients
- Search for a patient

Patient data is stored in:

```text
data/patients.json
```

## Store System

The store system allows the user to:

- Show products
- Search products
- Add products to cart
- Show cart
- Clear cart

Product data is stored in:

```text
data/products.json
```

Cart data is stored in:

```text
data/carts.json
```

## Technologies Used

- Python
- JSON
- bcrypt
- Git
- GitHub

## Installation

Install the required package:

```bash
pip install bcrypt
```

Or:

```bash
python -m pip install bcrypt
```

## Run the Project

Run this command inside the project folder:

```bash
python main.py
```

Or:

```bash
py main.py
```

## Notes

This project was built as a practice project to improve Python fundamentals, file organization, JSON handling, authentication, and command-line application structure.

## Future Improvements

- Add admin role
- Add patient delete/update feature
- Add cart checkout
- Improve error handling
- Add database support instead of JSON
- Add a GUI or web version
