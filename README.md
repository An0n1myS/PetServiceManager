# Template_db_ajax_interface
This project created for demonstrate how to communicate with server from pure JS.

A web application to manage a pet service business using Python, Flask, and Pyodbc to interact with an MS SQL Server. This project allows users to manage employees, services, clients, positions, animals, and breeds through a user-friendly web interface.

## Technologies

- Backend: Python and Flask
- Database: MS SQL Server with Pyodbc
- Frontend: JavaScript and jQuery

## Features

- Manage employees, services, clients, positions, animals, and breeds
- User-friendly web interface for adding, updating, and deleting records
- Seamless connection to the MS SQL Server database using Pyodbc
- Smooth user interactions enabled by JavaScript and jQuery

# Installation Process

Follow these steps to set up the PetServiceManager project on your local machine.

## Prerequisites

- Python 3.6 or higher
- Microsoft SQL Server
- ODBC Driver 17 for SQL Server

## Step 1: Clone the Repository

Clone the PetServiceManager repository to your local machine using the following command:

```bash
git clone https://github.com/An0n1myS/PetServiceManager.git
```

##  Step 2: Install Dependencies

Navigate to the project directory and install the required Python packages using pip:

```bash
cd PetServiceManager
pip install -r requirements.txt
```

##  Step 3: Configure Database Connection

Open the Python file containing the connection() function and update the s variable with your SQL Server name and the d variable with your database name:

```python
s = 'YOUR_SERVER_NAME'
d = 'YOUR_DATABASE_NAME'
```

## Step 4: Set up Database Tables

Create the necessary tables in your Microsoft SQL Server database using the provided table structure in the project documentation.

##  Step 5: Run the Application

Start the Flask application by running the following command in the project directory:

```bash
python main.py
```


The application will be accessible at http://127.0.0.1:5000/.

That's it! You've successfully installed and configured the PetServiceManager project on your local machine.
