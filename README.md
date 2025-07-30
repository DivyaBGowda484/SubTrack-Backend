# 📦 SubTrack – Smart Subscription & Expense Tracker

SubTrack is a backend-focused system built with FastAPI that helps users manage recurring subscriptions, control expenses, and gain financial clarity. It centralizes tracking for all subscriptions — from OTT platforms to SaaS tools — while offering reminders, summaries, and budget insights.

---

## ❓ Problem Statement

In today’s digital world, most people subscribe to multiple services — streaming, productivity, health, cloud, etc. These often lead to:
- Missed renewal reminders 💸  
- Overlapping subscriptions or forgotten free trials ⏰  
- Untracked expenses across cards, UPI, wallets, and banks 💳

### 💥 Impact
- Prevents financial leaks by identifying recurring payments.
- Lets users cancel, downgrade, or optimize subscriptions.
- Helps households/freelancers plan recurring monthly budgets.

---

## 🛠️ Tech Stack

### 🚀 Backend
- **Framework**: FastAPI (async, high-performance)
- **Database**: PostgreSQL (structured storage)
- **ORM**: SQLAlchemy or Tortoise ORM
- **Caching**: Redis
- **Queue**: Celery + Redis for async tasks
- **Authentication**: JWT (OAuth2PasswordBearer)
- **API Server**: Uvicorn + Gunicorn
- **Email**: SMTP + Celery (reminders)

### 🧰 Tools & Integrations
- **Docker + Docker Compose**
- **Traefik or NGINX** (Reverse proxy/load balancer)
- **Payment APIs**: Stripe, Razorpay (sync subscriptions)
- **CSV Parser**: For bank statements
- **Gmail API** *(optional)*: Email subscription parsing

---

## 📥 Setup Instructions

> ⚠️ Prerequisites:
- Python 3.10+
- Docker + Docker Compose
- PostgreSQL, Redis installed (or use Docker services)

### 🔧 Clone the Repository

```bash
git clone https://github.com/DivyaBGowda484/SubTrack-Backend.git
cd SubTrack-Backend
```

### 🐳 Run via Docker 

```bash
docker-compose up --build
```

---

### 🌐 API Endpoints

| Endpoint                 | Description                |
| ------------------------ | -------------------------- |
| `POST /auth/signup`      | Register a new user        |
| `POST /auth/login`       | Authenticate & get token   |
| `GET /subscriptions/`    | View all subscriptions     |
| `POST /subscriptions/`   | Add new subscription       |
| `GET /dashboard/summary` | Monthly dashboard          |
| `POST /expenses/import`  | Upload CSV bank statements |
| `GET /notifications/`    | Manage reminders           |

---

### 🧠 Features

- Subscription tracking by category (OTT, utility, education, etc.)
- Auto-frequency normalization (monthly view)
- Renewal reminders (email/push)
- Budget summary by month and category
- CSV export for taxes and budgeting
- Detect price hikes (price creep alerts)
- Scalable microservices-ready architecture

---

## ⚙️ Scalability & Deployment

- Dockerized with multi-container support  
- PostgreSQL on **AWS RDS**, Redis via **ElastiCache**  
- Deployment via **AWS ECS** or **Kubernetes**  
- CI/CD with **GitHub Actions**:  
  - `Lint → Test → Deploy`

---

## 🔐 Security Practices

- JWT Authentication with token expiry  
- Role-based access control (admin/user)  
- Input validation using **Pydantic**  
- Password hashing with **bcrypt**  
- HTTPS enabled via **Traefik + Certbot**  
- API rate-limiting using **slowapi**

---

## 🧩 Future Enhancements

- 🧠 AI-based subscription recommendations  
- 📈 Expense trend prediction using ML models  
- 📱 Mobile app integration (Android/iOS)  
- 🧾 OCR support for PDF bank statements  
- 💬 Reminders via WhatsApp and Telegram

# SubTrack Deployment Infrastructure

This folder contains deployment and infrastructure configuration for SubTrack.

## Services
- **backend**: FastAPI server using Gunicorn + Uvicorn workers
- **frontend**: React app served via Vite during development or static build in production
- **db**: PostgreSQL database
- **redis**: Redis instance for caching and Celery
- **nginx**: Reverse proxy with SSL via Let's Encrypt
- **certbot**: Certificate renewal setup
- **celery**: Background worker process managed by supervisord or PM2

## Usage

### Development
```bash
cd infra
docker-compose up --build
