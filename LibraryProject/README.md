# LibraryProject

This is a Django project for managing library systems.

## Setup

Follow these steps to set up and run the project:

1. **Install Dependencies**:
   - Ensure you have Python and Django installed. Install the required dependencies listed in `requirements.txt` using pip:
     ```bash
     pip install -r requirements.txt
     ```

2. **Apply Migrations**:
   - Set up your database by applying the migrations:
     ```bash
     python manage.py migrate
     ```

3. **Create a Superuser** (Optional):
   - Create an admin user for accessing the Django admin interface:
     ```bash
     python manage.py createsuperuser
     ```

## Running the Development Server

- To start the development server and view the project locally:
  ```bash
  python manage.py runserver
