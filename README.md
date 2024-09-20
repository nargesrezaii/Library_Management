# Online Library Management System

Welcome to the Online Library Management System! This is a Django-based library management system that allows users to add, view, search for, edit, remove, and filter books by price or publication date. Moreover, the system enables librarians to manage books and authors.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributors](#contributors)
- [Acknowledgments](#acknowledgments)


## Project Overview

## Features

- User registration and login
- Book and author management system
- Book search and borrowing system
- Book return tracking
- Admin panel for managing books, authors, and users
- Book borrowing history for users

## Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite, PostgreSQL
- **Version Control**: Git, Gitlab
- **Containerization**: Docker

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed on your machine:

- Python 3.11
- Django
- pip
- Git
- Docker

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/nargesrezaii/Library_Management
   cd Library_Management
   ```

2. **Set up a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**:

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (for admin access):

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:

   ```bash
   python manage.py runserver
   ```

   Navigate to `http://127.0.0.1:8000` in your web browser to see the application in action.

## Usage


## Contributors

- [Narges Rezaei](https://github.com/nargesrezaii) - Developer.

## Acknowledgments

