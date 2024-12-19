# Incident Management System

A Django-based web application built using Django Rest Framework (DRF) for managing and tracking incidents. This system enables users to report, view, update, and manage incidents. The application ensures secure access by associating incidents with specific users, preventing updates to closed incidents, and providing a unique incident ID generation system.

---

## Features

### Core Features
- **Incident Creation**: Allows users to create incidents with essential details like priority, status, and type (Enterprise or Government).
- **Unique Incident IDs**: Automatically generates a unique Incident ID when creating a new incident. The format is `RMG<random_number><year>`.
- **User-based Access**: Users can only view or edit incidents that they have reported. Closed incidents cannot be modified.
- **Search Functionality**: Users can search incidents by their unique Incident ID.
- **RESTful API**: A well-defined set of endpoints to interact with incidents.
- **Swagger Integration**: Interactive API documentation for easy testing and debugging.

---

## Technologies Used

- **Backend Framework**: Django and Django Rest Framework (DRF)
- **Authentication**: Token-based authentication (JWT)
- **Database**: Mysql
- **API Documentation**: Swagger UI (for interactive testing)
- **Programming Language**: Python 3.8
- **Libraries**:
  - `random` for generating random Incident IDs
  - Django ORM for database interactions
  - `timezone` for handling time-based fields

---

## Installation and Setup

### Prerequisites
1. Python 3.8 or higher installed on your machine.
2. pip (Python package manager) installed.
3. Virtual environment tools like `venv` or `virtualenv`.
4. Mysql database
    sudo apt-get update
    sudo apt-get install mysql-server
    sudo mysql_secure_installation
    Create a Database and User in MySQL
    Open the MySQL command line tool:
    mysql -u root -p
    Create a new database for your Django project:
    CREATE DATABASE incident_management;

# step for the running the code

1. unzip  the file:

   cd incident-management-system
2.
    python -m venv venv
    source venv/bin/activate   # For Linux/Mac
    venv\Scripts\activate

3. Install dependencies:
    pip install -r requirements.txt

4. Apply migrations to set up the database:

    python manage.py makemigrations
    python manage.py migrate
5.  Create a superuser for admin access:

    python manage.py createsuperuser
6. Run the server:


    python manage.py runserver

7. Open the API documentation:
    http://127.0.0.1:8000/swagger/ in your browser.
