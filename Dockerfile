FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Working directory
WORKDIR app/


# updating the packages
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY . . 

## install all dependencies and requirements and make python packages
RUN pip install --no-cache-dir -e .

# Flask port
EXPOSE 5000

# running the app
CMD ["python", "app/main.py"]