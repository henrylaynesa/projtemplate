# Flask + React TypeScript + PostgreSQL Project Template

A full-stack web application template built with Flask (Python), React (TypeScript), and PostgreSQL. This template provides a solid foundation for building modern web applications with a clean separation between frontend and backend.

## 🚀 Features

- **Backend**: Flask REST API with SQLAlchemy ORM
- **Frontend**: React 19 with TypeScript
- **Database**: PostgreSQL with Alembic migrations
- **Development**: Hot reloading for both frontend and backend
- **Containerization**: Docker and Docker Compose setup
- **Code Quality**: Pre-commit hooks and linting configuration
- **Environment Management**: Python virtual environments and Node.js version management

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.11+** (managed via `.python-version`)
- **Node.js 20** (managed via `.nvmrc`)
- **Docker & Docker Compose** (for containerized development)
- **PostgreSQL** (if running locally without Docker)

## 🛠️ Quick Start

### Option 1: Using Docker (Recommended)

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd projtemplate
   ```

2. **Start all services**
   ```bash
   docker-compose up --build
   ```

3. **Access the application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:5000
   - Database: localhost:5432

### Option 2: Local Development

1. **Set up the backend**
   ```bash
   cd backend
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Set up the frontend**
   ```bash
   cd frontend
   npm install
   ```

3. **Configure environment variables**
   ```bash
   # Copy and configure backend environment
   cp backend/.env.example backend/.env
   # Edit backend/.env with your database credentials
   ```

4. **Start the services**
   ```bash
   # Terminal 1: Start PostgreSQL (if not using Docker)
   # Terminal 2: Start backend
   cd backend
   python main.py

   # Terminal 3: Start frontend
   cd frontend
   npm start
   ```

## 📁 Project Structure

```
projtemplate/
├── backend/                 # Flask backend application
│   ├── app/                # Application package
│   │   ├── __init__.py     # Flask app factory
│   │   ├── config.py       # Configuration settings
│   │   ├── models.py       # SQLAlchemy models
│   │   └── routes.py       # API routes
│   ├── alembic/            # Database migrations
│   ├── Dockerfile          # Multi-stage Dockerfile
│   ├── nginx.conf          # Nginx configuration
│   ├── requirements.txt    # Python dependencies
│   └── main.py             # Flask application entry point
├── frontend/               # React frontend application
│   ├── src/               # Source code
│   │   ├── App.tsx        # Main application component
│   │   └── index.tsx      # Application entry point
│   ├── public/            # Static assets
│   └── Dockerfile          # Frontend Dockerfile
├── docker-compose.yml      # Main compose file with profiles
├── docker-compose.dev.yml  # Development-specific compose
├── docker-compose.prod.yml # Production-specific compose
├── .gitignore            # Git ignore rules
├── .pre-commit-config.yaml # Pre-commit hooks
└── README.md             # This file
```

## 🔧 Development

### Backend Development

The Flask backend is located in the `backend/` directory and includes:

- **Flask 3.1.1**: Modern Flask with async support
- **SQLAlchemy 2.0**: ORM for database operations
- **Alembic**: Database migration management
- **psycopg2**: PostgreSQL adapter
- **Flask-SQLAlchemy**: Flask integration with SQLAlchemy

**Key files:**
- `backend/app/__init__.py`: Flask application factory
- `backend/app/models.py`: Database models
- `backend/app/routes.py`: API endpoints
- `backend/app/config.py`: Configuration management

### Frontend Development

The React frontend is located in the `frontend/` directory and includes:

- **React 19**: Latest React with concurrent features
- **TypeScript 4.9**: Type-safe JavaScript
- **React Scripts**: Development and build tools
- **Testing Library**: Component testing utilities

**Key files:**
- `frontend/src/App.tsx`: Main application component
- `frontend/src/index.tsx`: Application entry point
- `frontend/package.json`: Dependencies and scripts

### Database Management

The project uses PostgreSQL with Alembic for migrations:

```bash
# Create a new migration
cd backend
alembic revision --autogenerate -m "Description of changes"

# Apply migrations
alembic upgrade head

# Rollback migrations
alembic downgrade -1
```

## 🐳 Docker Development

The project includes Docker configuration for easy development:

### Docker Setup

#### Development Environment

For development with hot reloading and volume mounts:

```bash
# Start development environment
docker compose up

# Or explicitly use development profile
docker compose --profile dev up
```

This will start:
- PostgreSQL database (port 5432)
- Backend with development stage (port 5000)
- Frontend with development stage (port 3000)

#### Production Environment

For production with nginx reverse proxy:

```bash
# Start production environment
docker compose --profile prod up

# Or use the production-specific compose file
docker compose -f docker-compose.prod.yml up
```

This will start:
- PostgreSQL database (port 5432)
- Backend with production stage (internal only)
- Nginx reverse proxy (port 80)
- Frontend with production stage (internal only)

### Docker Stages

#### Backend Dockerfile Stages

1. **Development Stage** (`development`)
   - Includes development dependencies
   - Volume mounts for hot reloading
   - Debug mode enabled
   - Direct port exposure

2. **Production Stage** (`production`)
   - Optimized for production
   - Non-root user for security
   - Production environment variables
   - Internal port only (no direct exposure)

3. **Nginx Stage** (`nginx`)
   - Alpine-based nginx
   - Reverse proxy configuration
   - Rate limiting and security headers
   - Gzip compression

#### Nginx Configuration

The nginx configuration includes:
- Reverse proxy to backend on port 5000
- Rate limiting (10 requests/second with burst of 20)
- Security headers
- Gzip compression
- Health check endpoint at `/health`
- API routes under `/api/`

## 🔒 Environment Variables

Create a `.env` file in the `backend/` directory:

```env
# Database Configuration
DATABASE_URL=postgresql://username:password@localhost:5432/dbname
POSTGRES_DB=dbname
POSTGRES_USER=username
POSTGRES_PASSWORD=password

# Flask Configuration
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
DEBUG=True
```

## 🧪 Testing

### Backend Testing

```bash
cd backend
python -m pytest
```

### Frontend Testing

```bash
cd frontend
npm test
```

## 📦 Building for Production

### Backend

```bash
cd backend
pip install -r requirements.txt
python main.py
```

### Frontend

```bash
cd frontend
npm run build
```

The built files will be in `frontend/build/` and can be served by any static file server.

## 🚀 Deployment

### Using Docker Compose (Production)

1. **Build production images**
   ```bash
   docker-compose -f docker-compose.prod.yml build
   ```

2. **Deploy**
   ```bash
   docker-compose -f docker-compose.prod.yml up -d
   ```

### Manual Deployment

1. **Backend**: Deploy the Flask application to your preferred hosting service
2. **Frontend**: Build and deploy the React app to a static hosting service
3. **Database**: Set up PostgreSQL on your preferred database hosting service

## 🔧 Configuration

### Development vs Production

The application automatically detects the environment:

- **Development**: Debug mode enabled, detailed error messages
- **Production**: Debug mode disabled, optimized for performance

### Database Configuration

The application supports multiple database configurations:

- **Development**: Local PostgreSQL instance
- **Production**: Cloud database (AWS RDS, Google Cloud SQL, etc.)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/your-repo/issues) page
2. Create a new issue with detailed information
3. Review the documentation in the `backend/README.md` and `frontend/README.md` files

## 🔄 Updates and Maintenance

- **Python dependencies**: Managed via `requirements.txt`
- **Node.js dependencies**: Managed via `package.json`
- **Database schema**: Managed via Alembic migrations
- **Code quality**: Enforced via pre-commit hooks

---

**Happy coding! 🎉**
