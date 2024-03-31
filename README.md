# Task Manager

A simple web-based task management application built with Python, Django, and Django REST Framework. It provides a web interface and a RESTful API for managing tasks.

## Features

*   Create, Read, Update, and Delete (CRUD) operations for tasks.
*   RESTful API for programmatic access to task data.
*   Built-in Django admin interface for easy data management.
*   Configuration driven by environment variables for security and flexibility.

## Technologies Used

*   **Backend:** Python, Django
*   **API:** Django REST Framework
*   **Database:** PostgreSQL (configurable for others like SQLite)
*   **Configuration:** `python-dotenv`

## Setup and Installation

Follow these steps to get the project up and running on your local machine.

### 1. Prerequisites

*   Python 3.10+
*   pip (Python package installer)
*   Git
*   A running database instance (e.g., PostgreSQL)

### 2. Clone the Repository

```bash
git clone git@github.com:fahim06/Task-Manager.git
cd Task-Manager
```

### 3. Create and Activate a Virtual Environment

It's highly recommended to use a virtual environment to manage project dependencies.

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

Install all the required packages using the `requirements.txt` file.

```bash
pip install -r requirements.txt
```
*(Note: If a `requirements.txt` file is not present, you can create one with the necessary packages. See the recommendations section below.)*

### 5. Configure Environment Variables

Create a `.env` file in the root directory of the project (`Task-Manager-main/.env`). This file will hold your secret keys and database configuration. Copy the contents of `.env.example` (if present) or use the template below.

```ini
# .env file

# SECURITY WARNING: a new key can be generated with `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`
SECRET_KEY=your_super_secret_key_here

# Set to False in production
DEBUG=True

# Database Configuration (Example for PostgreSQL)
DB_ENGINE=your-db-engine
DB_NAME=your_db
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your-db-host
DB_PORT=your-db-port
```

### 6. Apply Database Migrations

Run the following command to create the database tables based on your Django models.

```bash
python manage.py migrate
```

### 7. Create a Superuser

This will allow you to access the Django admin panel.

```bash
python manage.py createsuperuser
```

### 8. Run the Development Server

```bash
python manage.py runserver
```

The application will be available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Usage

*   **Web Interface:** The main task list is at `http://127.0.0.1:8000/`.
*   **Admin Panel:** Access the Django admin at `http://127.0.0.1:8000/admin/`.
*   **API Endpoints:** The API is available under the `/task/` prefix. You can use tools like Postman or `curl` to interact with it.

