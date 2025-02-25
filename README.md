# Scalable Task Manager API

A simple but well-structured API for creating, updating, and tracking tasks, showcasing:
✅ Authentication & User Management (JWT or OAuth)
✅ CRUD operations for tasks (Create, Read, Update, Delete)
✅ Database Optimization (PostgreSQL with indexes for performance)
✅ Background Jobs (e.g., Celery or Task Queues for sending reminders)
✅ Containerization & CI/CD (Docker + GitHub Actions)

## Tech Stack:
	•	Backend: Flask (or FastAPI) / Django REST Framework
	•	Database: PostgreSQL (or MySQL)
	•	Authentication: JWT (using PyJWT)
	•	Background Processing: Celery + Redis (for task scheduling)
	•	Deployment (Optional): Docker + GitHub Actions + Render/Heroku

### Features

Basic CRUD API
	•	Users can create, update, delete, and list tasks
	•	Each task has a title, description, priority, and due date
	•	Store tasks in PostgreSQL with proper indexing

Authentication & User Accounts
	•	User registration and login (JWT authentication)
	•	Each user sees only their own tasks

Background Jobs & Performance Tweaks
	•	Auto-send reminders for overdue tasks using Celery + Redis
	•	Implement caching (Redis) for faster task retrieval