# Django Mini Project

This is a mini project Django-based web application about shipment .

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Env variables](#envvariables)
- [Screenshots](#screehot)
---

## Requirements

Before setting up the project, make sure your system meets the following requirements:

- **Python**: 3.11
- **Django**: 5.1
- **MySQL**:  8.0

---

## Installation

Follow the steps below to set up the project on your local machine.

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Devajayantha/shipment_django.git
    ```

2. **Navigate into the project directory**:
    ```bash
    cd shipment_django
    ```

3. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
4. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Copy the `.env.example` file to `.env`**:
    ```bash
    cp .env.example .env
    ```

6. **Set up the database**:
    - Configure your database connection in the `.env` file.
    - Run migrations to create the necessary tables:
      ```bash
      python manage.py migrate
      ```

7. **Run project on deplopment mode**:
      ```bash
      python manage.py runserver
      ```

## Env Variables

        DEBUG=true
        SECRET_KEY=

        DB_HOST=127.0.0.1
        DB_PORT=3306
        DB_DATABASE=
        DB_USERNAME=
        DB_PASSWORD=
        
## Screenshoot

Here’s some screenshoot from my work.

![Screenshot](https://devajayantha.github.io/assets/image-sm/image1.png)

![Screenshot](https://devajayantha.github.io/assets/image-sm/image2.png)

![Screenshot](https://devajayantha.github.io/assets/image-sm/image3.png)

### Thank You
