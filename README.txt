# Heart Monitor Backend (Django REST API)

## Requirements
To set up and run this project, install the following dependencies:

### Required Installations
- Python (3.8+ recommended)
- Django
- Django REST Framework
- drf-yasg (for API documentation)
- SQLite (default database, can be changed)

### Installation Commands
```sh
git clone <your-github-repo-url>
cd heart_monitor_backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install django djangorestframework drf-yasg
```

### Running Migrations
```sh
python manage.py makemigrations
python manage.py migrate
```

### Running the Server
```sh
python manage.py runserver
```

### API Documentation
Swagger UI: `http://127.0.0.1:8000/swagger/`

