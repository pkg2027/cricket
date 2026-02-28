FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

EXPOSE 8726

CMD ["uvicorn", "web_app:app", "--host", "0.0.0.0", "--port", "8726"]
