# Multi-stage Dockerfile for backend with development and production stages

# =============================================================================
# DEVELOPMENT STAGE
# =============================================================================
FROM python:3.13-slim AS development

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install uv
RUN pip install uv

# Copy dependency files first (for better caching)
COPY pyproject.toml requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Expose port
EXPOSE 5000

# Set environment variables for development
ENV FLASK_APP=main.py
ENV FLASK_ENV=development
ENV PYTHONPATH=/app

# Run the application in development mode
CMD ["python", "main.py"]

# =============================================================================
# PRODUCTION STAGE
# =============================================================================
FROM python:3.13-slim AS production

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install uv
RUN pip install uv

# Copy dependency files first (for better caching)
COPY pyproject.toml requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Create non-root user for security
RUN useradd --create-home --shell /bin/bash app && \
    chown -R app:app /app
USER app

# Expose port
EXPOSE 5000

# Set environment variables for production
ENV FLASK_APP=main.py
ENV FLASK_ENV=production
ENV PYTHONPATH=/app

# Run the application in production mode
CMD ["python", "main.py"]

# =============================================================================
# NGINX STAGE
# =============================================================================
FROM nginx:alpine AS nginx

# Copy nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80
EXPOSE 80

# Start nginx
CMD ["nginx", "-g", "daemon off;"]
