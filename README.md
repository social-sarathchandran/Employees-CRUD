# Employees-CRUD

## Introduction
This project provides CRUD (Create, Read, Update, Delete) APIs for managing employees. It allows you to perform various operations such as creating, reading, updating, and deleting employee records.

## Installation
To run this project locally, follow these steps:

1. Clone this repository to your local machine.
2. Create a virtual environment:
    ```bash
    python -m venv venv
    ```
3. Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```
4. Install dependencies from the requirements.txt file:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
You can access the CRUD APIs for employees using the following endpoints:

- **Create**: POST /api/employees/
- **Read**: GET /api/employees/
- **Update**: PUT/PATCH /api/employees/<id>/
- **Delete**: DELETE /api/employees/<id>/

## Swagger Documentation
You can also access the Swagger UI for exploring the APIs:

- [Swagger UI](/swagger/)

## Note
Make sure to create an environment and install the packages in the requirements.txt file before running the project.


