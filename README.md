# Django Application

A simple Django application for test task.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/talhajubair100/test-task
    cd test-task
    ```

2. **Setup virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Run migrations**:
    ```sh
    python manage.py migrate
    ```

5. **Create a superuser**:
    ```sh
    python manage.py createsuperuser
    ```

## Usage

1. **Run the development server**:
    ```sh
    python manage.py runserver
    ```

2. **Access the app**:
    Open `http://127.0.0.1:8000` in your browser.
