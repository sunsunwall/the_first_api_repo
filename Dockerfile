FROM python:3.11-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

# .pyc cache off to keep image clean
ENV PYTHONDONTWRITEBYTECODE=1
# Unbuffered logs for immediate output
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copy pyproject.toml and uv.lock (if it exists)
COPY pyproject.toml uv.lock* ./

# Install dependencies using uv
RUN uv sync --frozen --no-cache

COPY . .

ENV PORT=8080
EXPOSE 8080

CMD ["uv", "run", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]