
# Triumph-Backend

Triumph-Backend is a Django-based backend application designed for managing user authentication, ticket management, and customer support team details. The project utilizes Django Rest Framework (DRF) for creating API endpoints and Simple JWT for token-based authentication.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [API Endpoints](#api-endpoints)
- [Project Structure](#project-structure)


## Features

- **User Authentication:** 
  - Register new users.
  - Login functionality with JWT token generation.
  
- **Ticket Management:** 
  - Create, retrieve, update, and delete tickets.
  - Support for ticket filtering based on status, priority, and user.
  - Role-based access to tickets (owners and superusers).

- **Customer Support Team:** 
  - View the list of customer support team members.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/amisalaam/Triumph-Backend.git
   cd Triumph-Backend
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser:**

   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server:**

   ```bash
   python manage.py runserver
   ```

## Configuration

- Ensure you have a `.env` file to set up your environment variables,

Here’s the `API Endpoints` section with the API routes presented in a table format:

```markdown
## API Endpoints

| Endpoint                       | HTTP Method | Description                                 |
|--------------------------------|-------------|---------------------------------------------|
| **Authentication**             |             |                                             |
| `/api/register/`               | POST        | Register a new user                         |
| `/api/login/`                  | POST        | Login a user and obtain JWT tokens          |
| **Ticket Management**          |             |                                             |
| `/api/tickets/`                | POST        | Create a new ticket                         |
| `/api/tickets/`                | GET         | List all tickets with optional filters      |
| `/api/tickets/<int:pk>/`       | GET         | Retrieve a specific ticket                  |
| `/api/tickets/<int:pk>/`       | PUT         | Update a specific ticket                    |
| `/api/tickets/<int:pk>/`       | DELETE      | Delete a specific ticket                    |
| **Customer Support Team**      |             |                                             |
| `/api/customer/support/`       | GET         | List all customer support team members      |
```

This table format provides a clear and concise overview of the API endpoints, making it easier for users to understand the available routes and their functions.

## Project Structure

```
Triumph-Backend/
│
├── authentication/           # App handling user authentication
│   ├── migrations/           # Database migrations
│   ├── models.py             # Custom user model
│   ├── serializers.py        # DRF serializers for authentication
│   ├── urls.py               # URL routes for authentication
│   ├── views.py              # View logic for authentication
│
├── tickets/                  # App handling ticket management
│   ├── migrations/           # Database migrations
│   ├── models.py             # Models for Ticket and CustomerSupportTeam
│   ├── serializers.py        # DRF serializers for tickets and support teams
│   ├── urls.py               # URL routes for tickets and support teams
│   ├── views.py              # View logic for tickets and support teams
│
├── TriumphBackend/           # Project settings and configurations
│   ├── settings.py           # Django project settings
│   ├── urls.py               # Project-wide URL routes
│   ├── wsgi.py               # WSGI application configuration
│
├── manage.py                 # Django management script
└── requirements.txt          # List of Python dependencies
```
