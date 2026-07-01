# Multi-stage build for smaller image
FROM python:3.9-slim AS base
WORKDIR /app
COPY health_check.py .
RUN pip install --no-cache-dir psutil

# Final stage
FROM base AS prod
CMD ["python", "health_check.py"]
