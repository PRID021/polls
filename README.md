# POLLS STRUCTURE

```sh
    myproject/
    │
    ├── manage.py
    ├── README.md
    ├── requirements.txt
    ├── tests/
    │   └── test_integration.py
    │
    ├── myproject/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings/
    │   │   ├── __init__.py
    │   │   ├── base.py
    │   │   ├── dev.py
    │   │   ├── test.py
    │   │   ├── prod.py
    │   │   ├── db_router.py
    │   ├── urls.py
    │   ├── wsgi.py
    │
    └── app_name/
        ├── migrations/
        ├── admin.py
        ├── apps.py
        ├── models.py
        ├── views.py
        ├── forms.py
        ├── urls.py
        ├── tests/
        │   ├── test_models.py
        │   ├── test_views.py
        │   ├── test_forms.py
        │   └── factories.py
        ├── templates/app_name/
        └── static/app_name/
```

# Project Setup and Usage Guide

## Prerequisites

Before running this project, ensure you have the following installed:

- **Python** (version 3.8+ recommended)
- **Poetry** for dependency management ([Poetry installation guide](https://python-poetry.org/docs/#installation))
- **Make** (to run the commands in this guide)

## Environment Variables

This project defines an environment variable for the Django environment (`DJANGO_ENV`). It is set to `dev` by default, but you can override it when running commands.

```bash
DJANGO_ENV=prod make runserver  # Example of running the server in production mode
```

## Installation

Before running any commands, make sure to install the dependencies:

```bash
make install
```

This will install the Python dependencies specified in the `pyproject.toml` file using Poetry.

## Common Commands

### Running the Development Server

To start the Django development server:

```bash
make runserver
```

The server will run on `localhost:8000` by default.

### Applying Database Migrations

To apply database migrations:

```bash
make migrate
```

This command runs migrations on the database associated with the `polls` app.

### Creating New Migrations

To create new migration files based on changes in your models:

```bash
make migrations
```

This will generate migration files for the `polls` app.

### Running Tests

You can run tests for the `polls` app by using:

```bash
make test
```

### Creating a Superuser

To create a Django superuser for the admin interface:

```bash
make createsuperuser
```

Follow the prompts to define the superuser credentials.

### Collecting Static Files

To collect all static files into a single directory (needed for production):

```bash
make collectstatic
```

This is usually necessary when deploying the project to a production environment.

### Cleaning Up `.pyc` Files

To remove Python cache files (`*.pyc`):

```bash
make clean
```

### Starting a Jupyter Notebook for Django Shell

To start a Jupyter Notebook with Django's `shell_plus` loaded (for convenient testing and development):

```bash
make jupyter
```

### Enter the Poetry Shell

If you need to enter the Poetry shell to run manual commands:

```bash
make shell
```

This opens an interactive shell where you can use all the Poetry-installed dependencies.

## Additional Commands

### Running the Server with Environment Variables

To run the server with environment variables (such as `DJANGO_ENV`):

```bash
make serve
```

You can pass an environment variable like this:

```bash
DJANGO_ENV=production make serve
```

### Viewing the Django Template Directory

To print the Django template directory path (for debugging or locating where Django is installed):

```bash
make where_template
```

This will output the location of the Django installation on your system.

## Troubleshooting

If you encounter any issues, ensure the following:

1. **Dependencies are installed**: Run `make install` to ensure Poetry installs all the dependencies.
2. **Correct environment variables**: If you're working in different environments (e.g., development vs. production), ensure you're setting `DJANGO_ENV` correctly.
3. **Permissions**: Ensure that you have the correct permissions for running `make` and managing Python dependencies.

## Notes

- **Poetry** is used for managing dependencies. Ensure you're using Poetry to install packages and manage the virtual environment.
- **Makefile** simplifies running common Django tasks. Feel free to modify the `Makefile` to add more commands specific to your project needs.
