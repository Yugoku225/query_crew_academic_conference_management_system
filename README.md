# 🎓 Query Crew – Academic Conference Management System

### A Flask & MySQL-Based Web Application for Managing Academic Conferences

An academic conference management platform designed to simplify and organize the core activities involved in conducting academic conferences, including user management, conference creation, research paper submissions, peer reviews, and session scheduling.

The application provides a centralized platform for managing conference-related information through a structured relational database and a modular Flask backend.

---

## 🚀 Project Overview

Managing academic conferences involves coordinating multiple stakeholders, including organizers, authors, reviewers, and participants.

This project aims to streamline these activities by providing a web-based system that organizes conference data, maintains relationships between entities, and supports essential management operations.

The application uses Flask for backend development and MySQL for persistent data storage, with SQLAlchemy handling database operations and ORM-based relationships.

### Key Objectives

- Centralize academic conference information.
- Manage users and their roles.
- Create and maintain conference records.
- Handle research paper submissions.
- Manage paper reviews and reviewer feedback.
- Organize conference sessions.
- Maintain data consistency through relational database design.
- Implement CRUD operations across the major application modules.

## ✨ Key Features

### 1. User Management

Provides functionality for managing users within the conference system.

- Create new user records.
- View all registered users.
- Retrieve individual user details.
- Update user information and roles.
- Delete user records.
- Support different user roles, including organizers, authors, and reviewers.

### 2. Conference Management

Allows organizers to manage academic conference information.

- Create new conferences.
- Store conference names and locations.
- Maintain conference dates.
- Associate conferences with their respective organizers.
- View conference details.
- Update and delete conference records.

### 3. Research Paper Management

Provides functionality for managing academic research paper submissions.

- Submit research papers.
- Store paper titles and abstracts.
- Associate papers with their respective authors.
- Link submissions to specific conferences.
- Maintain submission timestamps.
- View, update, and delete paper records.

### 4. Peer Review Management

Facilitates the management of academic paper reviews.

- Create reviews for submitted papers.
- Associate reviews with specific reviewers.
- Store reviewer comments and ratings.
- Retrieve individual review details.
- Update existing reviews.
- Delete review records.

### 5. Conference Session Management

Supports the organization of conference sessions.

- Create conference sessions.
- Store session titles and descriptions.
- Maintain session end times.
- Associate sessions with conferences.
- View, update, and delete session records.

---

## 🏗️ System Architecture

The application follows a modular backend architecture using Flask Blueprints.

```text
                 USER
                  |
                  v
          Flask Web Application
                  |
                  v
            Application Layer
                  |
          +-------+-------+
          |               |
          v               v
      Templates       Flask Routes
      (Jinja2)            |
                          |
             +------------+------------+
             |            |            |
             v            v            v
          Users       Conference     Papers
          Routes        Routes       Routes
             |            |            |
             +------------+------------+
                          |
             +------------+------------+
             |                         |
             v                         v
        Review Routes             Session Routes
             |                         |
             +------------+------------+
                          |
                          v
                 Flask-SQLAlchemy
                          |
                          v
                    MySQL Database
                          |
                          v
                  Relational Tables
```

### Architecture Components

| Component | Responsibility |
|---|---|
| Flask | Backend web framework |
| Flask Blueprints | Modular route organization |
| Jinja2 | Dynamic HTML rendering |
| Flask-SQLAlchemy | ORM and database operations |
| Flask-Migrate | Database schema migrations |
| Alembic | Migration management |
| MySQL | Relational database |
| HTML/CSS | Frontend structure and styling |

---

## 🗄️ Database Design

The project uses MySQL as its relational database, with SQLAlchemy ORM models defining the database entities and their relationships.

### Database Entities

| Table | Description |
|---|---|
| Users | Stores user information and roles |
| Conferences | Stores conference details and organizer references |
| Papers | Stores submitted research papers |
| Reviews | Stores reviewer comments and ratings |
| Sessions | Stores conference session information |

### Entity Relationships

The database uses foreign keys to establish relationships between entities.

- **Users → Conferences:** One organizer can organize multiple conferences.
- **Users → Papers:** One author can submit multiple papers.
- **Conferences → Papers:** One conference can receive multiple paper submissions.
- **Papers → Reviews:** A paper can have multiple reviews.
- **Users → Reviews:** A reviewer can create multiple reviews.
- **Conferences → Sessions:** A conference can have multiple sessions.

### Simplified ER Diagram

```text
             +----------------+
             |     USERS      |
             +----------------+
             | id (PK)        |
             | username       |
             | email          |
             | password       |
             | role           |
             +----------------+
                |          |
                |          |
          1:N   |          | 1:N
                v          v
       +-------------+  +-------------+
       | CONFERENCES |  |    PAPERS   |
       +-------------+  +-------------+
       | id (PK)     |  | id (PK)     |
       | name        |  | title       |
       | location    |  | abstract    |
       | date        |  | author_id   |
       | organizer_id|  | conference_id|
       +-------------+  +-------------+
              |                |
              | 1:N            | 1:N
              v                v
        +-------------+  +-------------+
        |  SESSIONS   |  |   REVIEWS   |
        +-------------+  +-------------+
        | id (PK)     |  | id (PK)     |
        | title       |  | comments    |
        | description |  | rating      |
        | end_time    |  | paper_id    |
        |conference_id|  | reviewer_id |
        +-------------+  +-------------+
```

### Database Normalization

The project also includes database design and normalization documentation covering:

- Relational schema design.
- Primary and foreign key constraints.
- Entity relationships.
- SQL queries.
- Third Normal Form (3NF) normalization.

The objective is to minimize redundant data, maintain referential integrity, and establish a structured database design.

---

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Backend Framework | Flask 3.0.3 |
| Database | MySQL |
| ORM | Flask-SQLAlchemy |
| Database Migrations | Flask-Migrate, Alembic |
| Frontend | HTML, CSS, Jinja2 |
| Database Connectivity | MySQL Connector / PyMySQL |
| Version Control | Git, GitHub |

---

## 📂 Project Structure

```text
query_crew_academic_conference_management_system/
│
├── migrations/
│   └── Database migration files
│
├── models/
│   ├── __init__.py
│   └── models.py
│
├── routes/
│   ├── users_routes.py
│   ├── conference_routes.py
│   ├── paper_routes.py
│   ├── review_routes.py
│   └── session_routes.py
│
├── static/
│   └── css/
│
├── templates/
│   ├── user/
│   ├── conference/
│   ├── paper/
│   ├── reviews/
│   └── sessions/
│
├── app.py
├── requirements.txt
├── README.md
└── Database, Query and 3NF normalization
```

---

## ⚙️ Installation and Setup

### Prerequisites

Make sure you have installed:

- Python 3.9+
- MySQL Server
- MySQL Workbench (optional)
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/Yugoku225/query_crew_academic_conference_management_system.git

cd query_crew_academic_conference_management_system
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment.

**macOS / Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure MySQL Database

Open MySQL and create the database:

```sql
CREATE DATABASE academic_conference_management_system;
```

Configure your database connection using an environment variable:

```bash
export DATABASE_URL="mysql+mysqlconnector://USERNAME:PASSWORD@localhost/academic_conference_management_system"
```

Replace `USERNAME` and `PASSWORD` with your MySQL credentials.

For Windows PowerShell:

```powershell
$env:DATABASE_URL="mysql+mysqlconnector://USERNAME:PASSWORD@localhost/academic_conference_management_system"
```

### 5. Initialize Database Migrations

Run:

```bash
flask db upgrade
```

If migrations have not yet been initialized, first run:

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 6. Run the Application

```bash
python app.py
```

The application will be available at:

```text
http://127.0.0.1:5000/
```

---

## 🔗 Application Routes

The application uses modular Flask Blueprints to organize different functionalities.

| Module | Route | HTTP Method | Operation |
|---|---|---|---|
| Users | `/users` | GET | View users |
| Users | `/users/new` | GET, POST | Create user |
| Users | `/users/<id>` | GET | View user details |
| Users | `/users/<id>/edit` | GET, POST | Update user |
| Users | `/users/<id>/delete` | POST | Delete user |
| Conferences | `/conferences` | GET, POST | View / create conferences |
| Conferences | `/conferences/<id>` | GET, POST | View / update conference |
| Papers | `/papers` | GET, POST | View / create papers |
| Papers | `/papers/<id>` | GET, POST | View / update paper |
| Reviews | `/reviews` | GET, POST | View / create reviews |
| Reviews | `/reviews/<id>` | GET, POST | View / update review |
| Sessions | `/sessions` | GET | View sessions |
| Sessions | `/sessions/new` | GET, POST | Create session |

The application also includes corresponding deletion routes for conference, paper, review, and session records.

---

## 📚 Key Concepts Implemented

### 1. CRUD Operations

Implemented Create, Read, Update, and Delete functionality across the main application entities.

### 2. Object Relational Mapping (ORM)

Used Flask-SQLAlchemy to map Python classes to relational database tables and manage database interactions using Python objects.

### 3. Database Relationships

Implemented foreign keys and SQLAlchemy relationships to connect users, conferences, papers, reviews, and sessions.

### 4. Database Migrations

Used Flask-Migrate and Alembic to manage database schema changes and maintain migration history.

### 5. Modular Backend Architecture

Organized application functionality using Flask Blueprints, separating business modules into individual route files.

### 6. Database Normalization

Studied relational database design and applied normalization concepts, including Third Normal Form (3NF).

---

## 🔮 Future Enhancements

- Implement secure user authentication and role-based authorization.
- Introduce password hashing and session management.
- Add paper assignment workflows for reviewers.
- Implement conference registration and participant management.
- Add paper submission status tracking.
- Introduce advanced reviewer assignment mechanisms.
- Implement email notifications for submission and review updates.
- Add an administrative dashboard with conference analytics.
- Improve API documentation and automated testing.

---

## ⚠️ Security Considerations

This repository is an academic project. Before production deployment, the following improvements are recommended:

- Hash passwords using a secure password-hashing algorithm.
- Store database credentials and Flask secret keys in environment variables.
- Disable Flask debug mode in production.
- Implement authentication and authorization checks on protected routes.
- Validate and sanitize user inputs.

---

## 👨‍💻 Author

**Yugant Raj**

B.Tech – Computer Science

GitHub: [@Yugoku225](https://github.com/Yugoku225)

**Repository:** [Query Crew – Academic Conference Management System](https://github.com/Yugoku225/query_crew_academic_conference_management_system)

---

⭐ If you find this project interesting, consider starring the repository!
