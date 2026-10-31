# TaskFlow API

A progressively developed Task Management REST API built using **Python and FastAPI**, demonstrating the evolution of backend development from in-memory storage to ORM-based database management and PostgreSQL integration.

## About the Project

TaskFlow is a task management backend designed to understand and implement backend development concepts step by step.

The project follows a progressive development approach, where each stage introduces a new concept and improves the application's architecture.

Instead of directly starting with a database, the application was initially developed using Python lists and dictionaries. It was then upgraded to SQLAlchemy ORM with SQLite, with PostgreSQL integration planned as the next stage.

## Development Journey

### Stage 1: In-Memory Storage (Python Lists & Dictionaries) — Completed

- Initially implemented task management using Python lists and dictionaries.
- Developed basic CRUD operations:
  - Create tasks
  - Retrieve tasks
  - Update tasks
  - Delete tasks
- Implemented API endpoints using FastAPI.
- Understood HTTP methods, routing, request handling and status codes.
- Data was stored temporarily in application memory and did not persist after restarting the application.

### Stage 2: Database Integration (SQLAlchemy ORM + SQLite) — Implemented

- Replaced in-memory list-based storage with database-backed operations.
- Integrated SQLAlchemy ORM for database interaction.
- Created database models to represent application entities.
- Configured SQLite database connectivity using SQLAlchemy Engine.
- Implemented database session management using `sessionmaker`.
- Used FastAPI dependency injection to manage database sessions.
- Implemented CRUD operations using SQLAlchemy queries.
- Used database transactions with `commit()`, `rollback()` and `refresh()`.

**Key Improvement:** Unlike the initial list-based implementation, tasks are now stored persistently in SQLite and remain available even after restarting the application.

### Stage 3: PostgreSQL Migration — Planned

- Migrate the existing SQLite implementation to PostgreSQL.
- Configure PostgreSQL database connectivity.
- Understand PostgreSQL database configuration and management.
- Explore database migrations and schema management.
- Improve database architecture and prepare the application for production-oriented deployment.

## Technology Stack

| Category | Technology |
|---|---|
| Programming Language | Python |
| Backend Framework | FastAPI |
| ORM | SQLAlchemy |
| Previous Storage | Python Lists & Dictionaries |
| Current Database | SQLite |
| Planned Database | PostgreSQL |
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
├── requirements.txt
├── .gitignore
├── README.md
└── taskflow.db  # Local database (not tracked by Git)
```

*The project structure may evolve as new development stages are implemented.*

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

### 5. Run the application

```bash
uvicorn app.main:app --reload
```

### 6. Explore API documentation

Open the following URL in your browser:

http://127.0.0.1:8000/docs

## Learning Objectives

- Understand REST API development using FastAPI.
- Implement CRUD operations.
- Understand the difference between in-memory storage and persistent storage.
- Learn SQLAlchemy ORM and database session management.
- Understand database transactions and dependency injection.
- Work with SQLite and PostgreSQL.
- Understand Git version control and incremental project development.

## Project Status

**Current Stage: Stage 2 — SQLAlchemy ORM with SQLite**

Stage 1 (In-Memory Storage) has been completed, and Stage 2 (Database Integration) has been implemented.

Stage 3 (PostgreSQL Migration) is planned as the next development milestone.

This project is actively evolving, with each development stage introducing new backend concepts and architectural improvements.