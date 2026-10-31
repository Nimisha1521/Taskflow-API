# TaskFlow API

A progressively developed Task Management REST API built using **Python and FastAPI**, demonstrating the evolution of backend development from in-memory storage to ORM-based database management and PostgreSQL integration.

## About the Project

TaskFlow is a task management backend designed to understand and implement backend development concepts step by step.

The project follows a progressive development approach, where each stage introduces a new concept and improves the application's architecture.

Instead of directly starting with a database, the application was initially developed using Python lists and dictionaries. It is then upgraded to use SQLAlchemy ORM and subsequently migrated to PostgreSQL.

## Development Journey

### Stage 1: In-Memory Storage (Python Lists & Dictionaries)

- Initially implemented task management using Python lists and dictionaries.
- Developed basic CRUD operations:
  - Create tasks
  - Retrieve tasks
  - Update tasks
  - Delete tasks
- Implemented API endpoints using FastAPI.
- Understood HTTP methods, routing, request handling and status codes.
- Data is stored temporarily in application memory and does not persist after restarting the application.

### Stage 2: Database Integration (SQLAlchemy ORM + SQLite)

**Planned / In Progress**

- Replace in-memory storage with database-backed operations.
- Integrate SQLAlchemy ORM.
- Create database models and establish database connectivity.
- Implement session management and database transactions.
- Use SQLite for persistent data storage.

### Stage 3: PostgreSQL Migration

**Planned**

- Migrate the existing SQLite implementation to PostgreSQL.
- Configure PostgreSQL database connectivity.
- Understand relational database management in a production-oriented environment.
- Improve database architecture and scalability.

## Technology Stack

| Category | Technology |
|---|---|
| Programming Language | Python |
| Backend Framework | FastAPI |
| ORM | SQLAlchemy (Stage 2) |
| Database | In-Memory Storage (Stage 1), SQLite (Stage 2), PostgreSQL (Stage 3) |
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
└── README.md
```

*The project structure will evolve as new development stages are implemented.*

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

*Adjust the application import path if your main.py is located elsewhere.*

### 6. Explore API documentation

Open the following URL in your browser:

```text
http://127.0.0.1:8000/docs
```

## Learning Objectives

- Understand REST API development using FastAPI.
- Implement CRUD operations.
- Understand the difference between in-memory storage and persistent storage.
- Learn SQLAlchemy ORM and database session management.
- Work with SQLite and PostgreSQL.
- Understand Git version control and incremental project development.

## Project Status

Currently at **Stage 1: In-Memory Storage**.

This project is actively evolving, with each development stage introducing new backend concepts and architectural improvements.