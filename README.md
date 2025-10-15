[//]: # (# FastAPI + SQLAlchemy Sample Project)

A learning-focused sample application demonstrating REST API using FastAPI with SQLAlchemy ORM and MySQL database.

## Project Overview

This project showcases a complete CRUD application with user management and item tracking features. It's designed as a hands-on example to learn key concepts including:

- **FastAPI** framework for building modern APIs
- **SQLAlchemy 2.0** ORM for database operations
- **MySQL 8.4** as the relational database
- **Pydantic** for data validation and serialization
- **Alembic** for database migrations
- **Docker Compose** for containerized development environment

## Features

- User registration with secure password hashing (bcrypt)
- CRUD operations for users and items
- One-to-many relationship (User → Items)
- Database connection pooling and health checks
- Automatic API documentation (Swagger UI)
- Environment-based configuration
- Database schema auto-creation on startup

## Tech Stack

- **FastAPI** - Modern, fast web framework for building APIs
- **SQLAlchemy 2.0** - SQL toolkit and ORM
- **Pydantic** - Data validation using Python type annotations
- **MySQL 8.4** - Relational database
- **PyMySQL** - Pure Python MySQL driver
- **Bcrypt** - Password hashing
- **Uvicorn** - ASGI server
- **Docker & Docker Compose** - Containerization

## Project Structure

```
.
├── main.py            # FastAPI application and route definitions
├── models.py          # SQLAlchemy database models
├── schemas.py         # Pydantic schemas for request/response validation
├── crud.py            # Database operations (Create, Read, Update, Delete)
├── database.py        # Database connection and session management
├── config.py          # Application settings and configuration
├── docker-compose.yml # Docker services (MySQL, phpMyAdmin)
├── .env               # Environment variables
├── Pipfile            # Python dependencies
└── alembic/           # Database migration scripts
```

## Getting Started

### Prerequisites

- Python 3.11+
- Docker and Docker Compose
- Pipenv (or pip)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd fast-api-sqlalchemy-sample-project
   ```

2. **Install dependencies**
   ```bash
   pipenv install
   ```

3. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

4. **Start MySQL database**
   ```bash
   docker-compose up -d mysql
   ```

5. **Run the application**
   ```bash
   pipenv run dev
   ```

The API will be available at `http://localhost:8000`

## API Endpoints

### Health Check
- `GET /` - Welcome message
- `GET /health` - Health check with database connection status

### Users
- `POST /users/` - Create a new user
- `GET /users/` - List all users (with pagination)
- `GET /users/{user_id}` - Get user by ID

### Items
- `POST /users/{user_id}/items/` - Create item for a user
- `GET /items/` - List all items (with pagination)

## API Documentation

FastAPI automatically generates interactive API documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Example Usage

### Create a User
```bash
curl -X POST http://localhost:8000/users/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user_1@example.com",
    "username": "johndoe",
    "password": "secure_password_123"
  }'
```

### Create an Item
```bash
curl -X POST http://localhost:8000/users/1/items/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My 1st Item",
    "description": "This is a test item"
  }'
```

### Get All Users
```bash
curl http://localhost:8000/users/
```

## Database Management

### phpMyAdmin
Access phpMyAdmin at `http://localhost:8080` for visual database management.

### Database Migrations
```bash
# Create a new migration
pipenv run alembic revision --autogenerate -m "description"

# Apply migrations
pipenv run migrate
```

## Development Scripts

```bash
pipenv run dev          # Start development server with auto-reload
pipenv run start        # Start production server
pipenv run test         # Run tests
pipenv run format       # Format code with Black
pipenv run lint         # Lint code with Flake8
pipenv run type-check   # Type check with mypy
```

## Key Learning Points

### 1. Database Models (SQLAlchemy)
- Defining tables using declarative base
- Column types and constraints
- Relationships (one-to-many)
- Cascade delete operations

### 2. Pydantic Schemas
- Request/response validation
- Data serialization
- Type hints and validation rules
- Separating create/read schemas

### 3. Database Sessions
- Connection pooling
- Session management with dependency injection
- Transaction handling
- Connection health checks

### 4. Password Security
- Bcrypt hashing
- Secure password storage
- Never storing plain text passwords

### 5. API Design
- RESTful endpoint structure
- HTTP status codes
- Error handling
- Request/response models

## Configuration

The application uses environment variables for configuration:

```env
# Database
DB_USER=
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=3306
DB_NAME=fastapi_db

# Application
APP_NAME='FastAPI MySQL App'
DEBUG=True

# Security
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## Troubleshooting

### Database Connection Issues
- Ensure MySQL container is running: `docker ps`
- Check database credentials in `.env`
- Verify port 3306 is not in use

### Password Special Characters
The application handles special characters in database passwords by URL encoding them automatically.

## License
MIT License - feel free to use this project for learning purposes.

