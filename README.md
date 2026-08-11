# 💼 Job Application Tracker

A full-stack web application built with Django and Django REST Framework to help job seekers track and manage their job applications — with a Kanban board, analytics dashboard, JWT authentication, and CSV export.

## 🔗 Live Demo
👉 [https://job-tracker-unzi.onrender.com](https://job-tracker-unzi.onrender.com)

## ✨ Features

- **JWT Authentication** — Secure register, login, logout and forgot password
- **REST API** — 7 fully documented API endpoints built with Django REST Framework
- **Kanban Board** — Visual board with Applied, Interview, Offer, Rejected columns
- **Analytics Dashboard** — Stats cards with total applications, interviews, offers, rejections
- **Charts** — Monthly applications bar chart + status doughnut chart using Chart.js
- **Search & Filter** — Search by company/role, filter by status
- **Add / Edit / Delete** — Full CRUD for job applications
- **Export to CSV** — Download all applications as a spreadsheet
- **Forgot Password** — Reset password via username
- **9 Automated Tests** — Full test coverage using Django test framework
- **PostgreSQL Database** — Production-grade relational database
- **Deployed on Render** — Live on the internet with cloud PostgreSQL

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3, Django 5, Django REST Framework |
| Authentication | JWT (djangorestframework-simplejwt) |
| Database | PostgreSQL (local) / Render PostgreSQL (production) |
| ORM | Django ORM |
| Frontend | HTML, Bootstrap 5, Jinja2, Vanilla JS |
| Charts | Chart.js |
| Testing | Django TestCase, APIClient |
| Deployment | Render, Gunicorn, Whitenoise |
| Version Control | Git, GitHub |

## 📁 Project Structure

```
job_tracker/
├── job_tracker/
│   ├── settings.py         # Django configuration
│   ├── urls.py             # Main URL routing
│   └── wsgi.py             # WSGI entry point
├── jobs/
│   ├── models.py           # JobApplication database model
│   ├── serializers.py      # DRF serializers
│   ├── views.py            # API views and logic
│   ├── urls.py             # API URL patterns
│   ├── admin.py            # Django admin config
│   └── tests.py            # 9 automated tests
├── templates/
│   └── jobs/
│       ├── base.html       # Base template
│       ├── login.html      # Login page
│       ├── register.html   # Register page
│       ├── dashboard.html  # Main dashboard
│       └── reset_password.html
├── static/
│   └── css/style.css       # Custom styles
├── requirements.txt        # Python dependencies
├── build.sh               # Render build script
└── Dockerfile             # Docker configuration
```

## 🔌 API Endpoints

| Method | Endpoint | Description | Auth |
|---|---|---|---|
| POST | `/api/auth/register/` | Create new account | No |
| POST | `/api/auth/login/` | Get JWT token | No |
| POST | `/api/auth/refresh/` | Refresh JWT token | No |
| POST | `/api/auth/reset-password/` | Reset password | No |
| GET/POST | `/api/applications/` | List/Create applications | Yes |
| GET/PUT/DELETE | `/api/applications/<id>/` | Get/Update/Delete application | Yes |
| GET | `/api/dashboard/` | Stats and chart data | Yes |
| GET | `/api/export/` | Download CSV | Yes |

## 🚀 How to Run Locally

```bash
# Clone the repository
git clone https://github.com/Preethi-Sri/job-tracker.git
cd job-tracker

# Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Set up PostgreSQL database
# Create a database called 'job_tracker' in PostgreSQL

# Run migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Run the server
python manage.py runserver
```

Open 👉 `http://127.0.0.1:8000`

## 🧪 Running Tests

```bash
python manage.py test jobs
```

Expected output:
```
Found 9 test(s).
.........
Ran 9 tests in 8.7s
OK
```

## 📊 Database Schema

**JobApplication Table**
| Column | Type | Description |
|---|---|---|
| id | Integer | Primary key |
| user | ForeignKey | Owner (User) |
| company | String | Company name |
| role | String | Job role |
| location | String | Job location |
| job_type | String | full-time/part-time/contract |
| status | String | applied/interview/offer/rejected |
| applied_date | Date | Date applied |
| interview_date | Date | Interview date (optional) |
| salary | String | Expected salary |
| job_url | URL | Link to job posting |
| notes | Text | Additional notes |
| created_at | DateTime | Auto timestamp |

## 🌍 Deployment

The app is deployed on **Render** with:
- Gunicorn as WSGI server
- Whitenoise for static file serving
- Render PostgreSQL as cloud database
- Environment variables for secrets

## 👩‍💻 Author

**Preethi Kaleeswaran**
- GitHub: [@Preethi-Sri](https://github.com/Preethi-Sri)
- LinkedIn: [preethi-kaleeswaran](https://www.linkedin.com/in/preethi-kaleeswaran-1328b1199/)
- Live App: [job-tracker-unzi.onrender.com](https://job-tracker-unzi.onrender.com)
