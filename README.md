# TaskFlow API

A progressively developed Task Management REST API built using **Python and FastAPI**, demonstrating the evolution of backend development from in-memory storage to SQLAlchemy ORM, SQLite, and PostgreSQL.

## About the Project

TaskFlow is a task management backend developed to understand and implement backend development concepts through progressive stages.

Rather than starting with a fully developed database architecture, the project began with basic Python data structures and gradually evolved into a database-backed application.

The development journey covers three major stages:

1. In-memory storage using Python lists and dictionaries.
2. Database integration using SQLAlchemy ORM and SQLite.
3. PostgreSQL integration and database migration.

Each stage introduces new backend concepts and improves the application's architecture, persistence, and database management.

## Development Journey

### Stage 1: In-Memory Storage (Python Lists & Dictionaries) — Completed

- Initially implemented task management using Python lists and dictionaries.
- Developed basic CRUD operations:
  - Create tasks
  - Retrieve tasks
  - Update tasks
  - Delete tasks
- Implemented REST API endpoints using FastAPI.
- Understood HTTP methods, routing, request handling, and status codes.
- Managed application data in memory without persistent database storage.
- Understood the limitations of in-memory storage, including data loss when the application restarts.

### Stage 2: Database Integration (SQLAlchemy ORM + SQLite) — Completed

- Replaced in-memory list-based storage with database-backed operations.
- Integrated SQLAlchemy ORM for database interaction.
- Created database models to represent application entities.
- Configured SQLite database connectivity using SQLAlchemy Engine.
- Implemented database session management using `sessionmaker`.
- Used FastAPI dependency injection to manage database sessions.
- Implemented CRUD operations using SQLAlchemy queries.
- Managed database transactions using `commit()`, `rollback()`, and `refresh()`.
- Achieved persistent data storage using SQLite.

**Key Improvement:** Application data became persistent and remained available even after restarting the application.

### Stage 3: PostgreSQL Integration — Completed

- Migrated database operations from SQLite to PostgreSQL.
- Configured PostgreSQL database connectivity with SQLAlchemy.
- Adapted the application to work with PostgreSQL as its relational database.
- Configured database schema management and migration workflows.
- Worked with Alembic for database schema migrations and version control.
- Understood the process of managing database schema changes through migrations.
- Established PostgreSQL as the current database backend.

**Key Improvement:** The application progressed from local SQLite storage to PostgreSQL, providing experience with a dedicated relational database management system and structured schema migration.

### Stage 4: Backend Architecture & Project Structure — In Progress

**Currently Under Development**

- Refactoring the existing application into a modular and maintainable backend architecture.
- Organizing application components into clearly defined modules.
- Separating API routes, database operations, business logic, and data validation.
- Improving separation of concerns and code reusability.
- Establishing a structured approach to dependency management.
- Improving maintainability, scalability, and extensibility of the application.

**Objective:** Transition from a functional backend implementation to a well-structured application architecture that is easier to maintain, test, and extend.

## Current Development Focus

**Stage 4: Backend Architecture & Project Structure**

The current focus is on improving the internal organization of TaskFlow, establishing clear responsibilities for different application layers, and preparing the backend for future feature development.

## Technology Stack

| Category | Technology |
|---|---|
| Programming Language | Python |
| Backend Framework | FastAPI |
| ORM | SQLAlchemy |
| Database (Stage 1) | In-Memory Lists & Dictionaries |
| Database (Stage 2) | SQLite |
| Database (Stage 3) | PostgreSQL |
| Database Migration | Alembic |
| API Testing | Postman |
| Version Control | Git & GitHub |

## Project Structure

```text
taskflow-api/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   └── schemas.py
│
├── alembic/
│   └── versions/
│
├── alembic.ini
├── requirements.txt
├── .gitignore
├── README.md
└── taskflow.db
```

*The project structure represents the main application components. Additional files and modules may be present as the implementation evolves.*

**Note:** `taskflow.db` represents the local SQLite database used during Stage 2. The actual local database file is excluded from GitHub through `.gitignore`. PostgreSQL is hosted and managed separately.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/taskflow-api.git
cd taskflow-api
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Configure the required database connection settings in your local `.env` file.

Do not commit database credentials, passwords, or secret keys to GitHub.

### 6. Run database migrations

If using Alembic:

```bash
alembic upgrade head
```

### 7. Run the application

```bash
uvicorn app.main:app --reload
```

### 8. Explore API documentation

Open the following URL in your browser:

http://127.0.0.1:8000/docs

## Learning Objectives

- Understand REST API development using FastAPI.
- Implement CRUD operations using Python data structures.
- Understand the difference between in-memory storage and persistent storage.
- Learn SQLAlchemy ORM and database session management.
- Understand database engines, connections, sessions, and transactions.
- Work with SQLite and PostgreSQL.
- Understand relational database management.
- Implement database schema migrations using Alembic.
- Understand Git version control and incremental backend development.

## Project Status

**Current Status: All Three Development Stages Completed**

- Stage 1: In-Memory Storage — Completed.
- Stage 2: SQLAlchemy ORM with SQLite — Completed.
- Stage 3: PostgreSQL Integration — Completed.

TaskFlow demonstrates the progressive development of a backend application, from basic in-memory data handling to ORM-based database operations and PostgreSQL integration.

## Project Status

**Development Progress:**

- Stage 1: In-Memory Storage — Completed.
- Stage 2: SQLAlchemy ORM with SQLite — Completed.
- Stage 3: PostgreSQL Integration — Completed.
- Stage 4: Backend Architecture & Project Structure — In Progress.

TaskFlow is evolving from a basic CRUD application into a modular, maintainable, and scalable backend system.