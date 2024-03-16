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
