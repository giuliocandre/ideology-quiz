# ---------- Build stage ----------
FROM python:3.11-slim AS builder

# Create virtual environment directory
ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
 && rm -rf /var/lib/apt/lists/*

# Preinstall dependencies
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# ---------- Final stage ----------
FROM python:3.11-slim

# Set environment
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Copy virtualenv from builder
COPY --from=builder $VIRTUAL_ENV $VIRTUAL_ENV

# Set working directory
WORKDIR /app

# Copy app source
COPY . .

# Expose port
EXPOSE 8000

# Start server
CMD ["uvicorn", "quiz.app:main", "--host", "0.0.0.0", "--port", "8000"]
