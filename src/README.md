
# 🎓 Student Support Ticket Management API

A RESTful backend service built with **FastAPI** to manage student support tickets in colleges or training institutes.  
The system allows students to raise support tickets while enabling support staff to track and update them efficiently.

This project replaces manual handling via email or messaging with a structured and secure API-based system. :contentReference[oaicite:0]{index=0}

---

## 📌 Objective

The application demonstrates:

- REST API design using FastAPI
- JWT-based authentication
- Request & response handling
- URL routing and path operations
- Pydantic validation
- Logging integration
- Swagger API documentation

---

## 🚀 Features

### Authentication
- User login using username & password
- JWT token generation
- Secure access to protected endpoints

### Ticket Management
- Students can create support tickets
- Students can view their tickets
- Support staff can view all tickets
- Support staff can update ticket status

### API Standards
- REST-compliant endpoints
- Structured JSON responses
- Proper HTTP status codes
- Request validation

### Developer Features
- Swagger documentation
- Logging of requests and actions
- Clean project structure
- Separation of concerns

---

## 🧱 Project Structure

```

student_support_api/
│
├── main.py
├── routes/
│   ├── auth.py
│   └── tickets.py
├── models/
│   ├── user.py
│   └── ticket.py
├── schemas/
│   ├── user.py
│   └── ticket.py
├── utils/
│   ├── jwt_handler.py
│   └── logger.py
└── README.md

````

---

## ⚙️ Installation & Setup

### 1. Clone Repository
```bash
git clone <repository-url>
cd student_support_api
````

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Server

```bash
uvicorn main:app --reload
```

Server runs at:

```
http://127.0.0.1:8000
```

---

## 📖 API Documentation (Swagger)

Swagger UI:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```

Swagger supports JWT authentication for testing secured endpoints.

---

## 🔐 Authentication Flow

1. Login via `/login`
2. Receive JWT token
3. Use token in headers:

```
Authorization: Bearer <JWT_TOKEN>
```

---

## 📡 API Endpoints

### Authentication

| Method | Endpoint | Description                     |
| ------ | -------- | ------------------------------- |
| POST   | `/login` | Authenticate user and get token |

### Ticket APIs

| Method | Endpoint               | Description          |
| ------ | ---------------------- | -------------------- |
| POST   | `/tickets`             | Create ticket        |
| GET    | `/tickets`             | Get tickets          |
| GET    | `/tickets/{ticket_id}` | Get ticket details   |
| PUT    | `/tickets/{ticket_id}` | Update ticket status |

---

## 📦 Request & Response Format

Example API response:

```json
{
  "success": true,
  "data": {},
  "message": "Operation successful"
}
```

---

## 🧾 Ticket Fields

A ticket includes:

* Title
* Description
* Priority (Low / Medium / High)
* Status (Open / In Progress / Resolved)
* Created timestamp
* Owner information

---

## 🧠 Role-Based Access

### Student

* Create tickets
* View own tickets only

### Support Staff

* View all tickets
* Update ticket status

---

## 📋 Logging

System logs include:

* Incoming requests
* Authentication success/failure
* Ticket creation & updates
* Errors with timestamps and endpoints

---

## 🧪 Example Workflow

1. Login
2. Copy JWT token
3. Create ticket
4. View ticket list
5. Support updates status
6. Student checks resolution

---

## 🔮 Future Improvements

* Database integration
* Ticket comments
* File attachments
* Email notifications
* Admin dashboard
* Pagination & filtering
* Role management

---

## 🎯 Learning Outcomes

After completing this project, learners can:

* Build APIs with FastAPI
* Implement JWT authentication
* Validate data with Pydantic
* Design RESTful routes
* Use Swagger documentation
* Add logging in backend services

---

## 📄 License

This project is intended for educational and training purposes.

---

## 👨‍💻 Author

Student Support Ticket API — Backend Learning Project

