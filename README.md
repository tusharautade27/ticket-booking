

# 🎟️ Ticket Booking System

<p align="center">
  <img src="banner.png" width="100%">
</p>

<p align="center">


A modern **Full Stack Ticket Booking System** built with **FastAPI**, **Next.js**, **PostgreSQL**, and **JWT Authentication**.

Users can browse events, select seats, securely book tickets, generate QR codes, download PDF tickets, validate tickets, and scan QR codes.

---

## 🚀 Tech Badges

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.116-009688?logo=fastapi)
![Next.js](https://img.shields.io/badge/Next.js-16-black?logo=next.js)
![React](https://img.shields.io/badge/React-19-61DAFB?logo=react)
![TypeScript](https://img.shields.io/badge/TypeScript-5-3178C6?logo=typescript)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17-336791?logo=postgresql)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2-red)
![Alembic](https://img.shields.io/badge/Alembic-Migrations-green)
![JWT](https://img.shields.io/badge/Auth-JWT-black)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📊 Repository

![GitHub last commit](https://img.shields.io/github/last-commit/tusharautade27/ticket-booking)

![GitHub Repo stars](https://img.shields.io/github/stars/tusharautade27/ticket-booking?style=social)

![GitHub forks](https://img.shields.io/github/forks/tusharautade27/ticket-booking?style=social)

---

# ✨ Features

| Feature | Status |
|----------|--------|
| User Registration | ✅ |
| User Login | ✅ |
| JWT Authentication | ✅ |
| Role Based Authorization | ✅ |
| Event Management | ✅ |
| Venue Management | ✅ |
| Automatic Seat Generation | ✅ |
| Seat Hold System | ✅ |
| Double Booking Prevention | ✅ |
| Ticket Booking | ✅ |
| QR Code Generation | ✅ |
| PDF Ticket Generation | ✅ |
| Ticket Download | ✅ |
| Ticket Validation | ✅ |
| QR Scanner | ✅ |
| Dashboard Analytics | ✅ |
| Booking Cancellation | ✅ |
| Swagger API Documentation | ✅ |

---

# 🛠 Tech Stack

## Frontend

- Next.js 16
- React 19
- TypeScript
- Tailwind CSS
- React Query
- Axios
- Shadcn UI

## Backend

- FastAPI
- SQLAlchemy
- Alembic
- PostgreSQL
- Pydantic
- JWT Authentication

## Additional Libraries

- QRCode
- ReportLab
- Uvicorn

---

# 🏗 System Architecture

```text
                   Next.js Frontend
                           │
                           │ REST API
                           ▼
                    FastAPI Backend
                           │
        ┌──────────────────┴──────────────────┐
        │                                     │
 PostgreSQL Database                QR & PDF Service
```

---

# 🎫 Booking Workflow

```text
User Login
      │
      ▼
Browse Events
      │
      ▼
Select Seats
      │
      ▼
Create Booking
      │
      ▼
Generate QR Code
      │
      ▼
Generate PDF Ticket
      │
      ▼
Download Ticket
      │
      ▼
Validate Ticket
```

---

# 📸 Screenshots

| Login | Dashboard |
|-------|-----------|
| ![](screenshots/login.png) | ![](screenshots/dashboard.png) |

| Events | Venues |
|--------|---------|
| ![](screenshots/events.png) | ![](screenshots/venues.png) |

| Seat Selection | My Tickets |
|----------------|------------|
| ![](screenshots/seats.png) | ![](screenshots/tickets.png) |

| Validate Ticket | QR Scanner |
|----------------|------------|
| ![](screenshots/validate-ticket.png) | ![](screenshots/scan-qr.png) |

| Swagger API |
|-------------|
| ![](screenshots/swagger.png) |

---

# 📁 Project Structure

```text
ticket-booking
│
├── backend
│   ├── app
│   ├── alembic
│   ├── storage
│   ├── requirements.txt
│   └── app/main.py
│
├── frontend
│   ├── app
│   ├── components
│   ├── services
│   ├── lib
│   └── package.json
│
├── screenshots
│
├── README.md
└── LICENSE
```

---

# 🔐 Authentication

- JWT Authentication
- Protected Routes
- Current User Dependency
- Role-Based Authorization

---

# ⚙ Backend Setup

```bash
cd backend

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

Run database migrations

```bash
alembic upgrade head
```

Start server

```bash
uvicorn app.main:app --reload
```

---

# 💻 Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

---

# 📖 API Documentation

Once the backend is running:

```
http://127.0.0.1:8000/docs
```

Swagger UI provides complete REST API documentation.

---

# 🌍 Deployment (Planned)

Frontend

- Vercel

Backend

- Render / Railway

Database

- Neon PostgreSQL

---

# 🚀 Future Improvements

- Payment Gateway Integration
- Email Ticket Delivery
- Admin Dashboard
- User Profile Management
- Event Image Upload
- Real-time Seat Locking
- Docker Support
- CI/CD Pipeline
- Cloud Deployment

---

# 👨‍💻 Author

## Tushar Autade

GitHub

https://github.com/tusharautade27

---

# ⭐ Support

If you found this project helpful, please consider giving it a ⭐ on GitHub.

It helps others discover the project and motivates future improvements.