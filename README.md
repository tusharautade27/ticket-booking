# 🎟️ Ticket Booking System

A full-stack Ticket Booking System built with **FastAPI**, **Next.js**, **PostgreSQL**, and **JWT Authentication**.

Users can browse events, select seats, book tickets, download PDF tickets, scan QR codes, and validate tickets.

---

# 🚀 Live Features

- ✅ User Registration & Login
- ✅ JWT Authentication
- ✅ Role Based Authorization
- ✅ Event Management
- ✅ Venue Management
- ✅ Automatic Seat Generation
- ✅ Seat Hold System
- ✅ Double Booking Prevention
- ✅ Ticket Booking
- ✅ QR Code Generation
- ✅ PDF Ticket Generation
- ✅ Ticket Download
- ✅ Ticket Validation
- ✅ QR Code Scanner
- ✅ Dashboard Analytics
- ✅ Booking Cancellation
- ✅ REST API Documentation (Swagger)

---

# 🛠 Tech Stack

## Frontend

- Next.js 16
- React
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

## Other

- QRCode
- ReportLab PDF
- Uvicorn

---

# 🏗 Architecture

```
                 Next.js Frontend
                        │
                        │ REST API
                        ▼
                 FastAPI Backend
                        │
        ┌───────────────┴───────────────┐
        │                               │
   PostgreSQL Database          QR & PDF Service
```

---

# 📸 Screenshots

## Dashboard

![Dashboard](screenshots/dashboard.png)

---

## Events

![Events](screenshots/events.png)

---

## Seat Selection

![Seats](screenshots/seats.png)

---

## My Tickets

![Tickets](screenshots/tickets.png)

---

## Validate Ticket

![Validate](screenshots/validate-ticket.png)

---

## QR Scanner

![QR Scanner](screenshots/scan-ticket.png)

---

## Swagger API

![Swagger](screenshots/swagger.png)

---

# 📁 Project Structure

```
ticket-booking
│
├── backend
│   ├── app
│   ├── alembic
│   ├── storage
│   └── requirements.txt
│
├── frontend
│   ├── app
│   ├── components
│   ├── services
│   └── package.json
│
└── README.md
```

---

# 🔐 Authentication

- JWT Login
- Protected Routes
- Current User Dependency
- Role-based Access

---

# 🎫 Booking Flow

```
Login
      │
      ▼
Browse Events
      │
      ▼
Choose Seats
      │
      ▼
Create Booking
      │
      ▼
Generate QR
      │
      ▼
Generate PDF
      │
      ▼
Download Ticket
      │
      ▼
Validate Ticket
```

---

# ⚙️ Backend Setup

```bash
cd backend

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

Run migrations

```bash
alembic upgrade head
```

Run server

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

After starting the backend:

```
http://127.0.0.1:8000/docs
```

---

# 🌟 Future Improvements

- Payment Gateway
- Email Ticket
- Admin Dashboard
- Event Images
- Real-time Seat Locking
- Docker Deployment
- CI/CD
- Cloud Deployment

---

# 👨‍💻 Author

**Tushar Autade**

- GitHub: https://github.com/tusharautade27

---

# ⭐ If you like this project, give it a star!