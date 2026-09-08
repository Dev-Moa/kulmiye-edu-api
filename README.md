# Kulmiye Edu — API

Backend for the Kulmiye Edu platform — a university & scholarship discovery service for Somali students.

## Background

The backend half of my **first project**, built during my internship — my introduction to production Django, DRF, JWT auth, and cloud deployment.

## Tech stack

- **Django 4.2** + **Django REST Framework**
- **JWT auth** (SimpleJWT)
- **PostgreSQL** (dj-database-url) · **S3 storage** (boto3)
- API documentation via **drf-spectacular**
- Served with **Gunicorn** on **Railway**

## Data model

- `University` — institutions with programs and degrees
- `Program` / `Degree` — programs and the degrees they lead to
- `ProgramScholarship` — scholarships linked to programs
- `Enrollment` — student enrollments
- `EducationType` / `EducationLanguage` — reference data

## Endpoints (overview)

- `auth/` — signup & sign-in (JWT)
- universities, programs, degrees, scholarships — list + search with filters
- enrollment management

## Frontend

See [kulmiye-edu-ui](https://github.com/Dev-Moa/kulmiye-edu-ui) — Vue 3 + Tailwind.

## Local setup

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Status

Actively maintained.
