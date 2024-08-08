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
- **Deta**: A cloud platform for deploying the FastAPI application.

## Installation and Setup

### Prerequisites

- Python 3.7+
- pip (Python package installer)
- Deta CLI (for deployment)
- Vercel account (for front-end deployment)

### Local Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/JessieXu959/EventManagerAPI.git
    cd EventManagerAPI
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application**:
    ```bash
    uvicorn app.main:app --reload
    ```

5. **Access the API documentation**:
    Open your browser and go to `http://127.0.0.1:8000/docs` to see the interactive API documentation.
