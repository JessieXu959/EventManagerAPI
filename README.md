<<<<<<< HEAD
# EventManagerAPI
EventManagerAPI is a backend server built with FastAPI for managing event data. This project includes various endpoints for creating, reading, updating, and deleting events, as well as filtering and analyzing event data.

## Features

- **CRUD Operations**: Create, read, update, and delete events.
- **Filtering**: Filter events based on date, organizer, status, and event type.
- **Analysis**: Identify participants who have attended multiple events.
- **File-based Storage**: Uses JSON files for data storage instead of traditional databases.

## Technologies Used

- **FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python 3.7+.
- **Python**: The programming language used for developing the backend.
- **Uvicorn**: A lightning-fast ASGI server for serving FastAPI applications.

## Installation and Setup

### Prerequisites

- Python 3.7+
- pip (Python package installer)

### Local Setup

1. **Clone the repository**:
    ```bash
    git clone git@github.com:JessieXu959/EventManagerAPI.git
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    ```
   
3. **Activate the virtual environment**:
   - Windows CMD:
     ```bash
     .\venv\Scripts\activate.bat
     ```
   - Windows PowerShell:
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Run the application**:
    ```bash
    uvicorn app.src.app:app --reload
    ```

6. **Access the API documentation**:
    Open your browser and go to `http://127.0.0.1:8000/docs` to see the interactive API documentation.
=======

# FastAPI Project

This is a FastAPI project designed for Assignment 1.

## Installation

To run this project locally, you need to have Python and pip installed on your machine.

1. Clone this repository:
```bash
  git clone https://github.com/frdayvz85/assignment1.git
  or
  git@github.com:frdayvz85/assignment1.git
```   
2. Navigate into the project directory:
```bash
  cd assignment1
```   
3. Create a virtual enviroment:
```bash
  python -m venv venv
  or
  py -m venv venv
  or
  py3 -m venv venv
```
4. Active a virtualenv
```bash
  Windows users from CMD run this command:
  .\venv\Scripts\activate.bat

  Windows users from PowerShell run this command:
  .\venv\Scripts\Activate.ps1

  Linux or Mac users run this command:
  source venv/bin/activate
```  
5. Install the requirements in the current environment:
```bash
  pip install -r requirements.txt
```  
6. Last step run the following command:
```bash
  py app/main.py
```  


### Testing APIs 🚀:
FastAPI documentation is automatically generated and interactive, meaning you can explore and test your API endpoints directly from a web browser. This documentation is generated based on the endpoint functions you define in your FastAPI application, along with their type hints, docstrings, and other metadata.

Accessing interface use following link:
```bash
  http://127.0.0.1:8000/docs
```  

There is 1 testing Endpoint which it is for testing.
You can check `Root` section and test it.

![image](https://github.com/frdayvz85/python/assets/55210294/825dfd00-706b-436c-b2fe-8ab2b7349eae)

You can check Event APIs from ``Event`` section and test it:

![image](https://github.com/frdayvz85/python/assets/55210294/7609d150-8dfc-4547-8126-184d8ea03129)




```bash
  Good Luck 🚀
```  

>>>>>>> eb406bf (README.md added)
