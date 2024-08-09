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
    git clone https://github.com/JessieXu959/EventManagerAPI.git
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    or
    py -m venv venv
    or
    py3 -m venv venv
    ```
3.**Active a virtualenv**
   ```bash
   Windows users from CMD run this command:
  .\venv\Scripts\activate.bat

   Windows users from PowerShell run this command:
  .\venv\Scripts\Activate.ps1

   Linux or Mac users run this command:
   source venv/bin/activate
   ```
4. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application**:
    ```bash
    py app/main.py
    ```

5. **Access the API documentation**:
    Open your browser and go to `http://127.0.0.1:8000/docs` to see the interactive API documentation.
