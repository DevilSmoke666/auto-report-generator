# 🐍 Базовий образ
FROM python:3.12-slim

# 🧰 Системні залежності для WeasyPrint
RUN apt-get update && apt-get install -y \
    build-essential \
    libpangocairo-1.0-0 \
    libpango-1.0-0 \
    libgdk-pixbuf2.0-0 \
    libffi-dev \
    curl \
    && apt-get clean

# 📁 Робоча директорія
WORKDIR /app

# 📦 Копіюємо проєкт
COPY . .

# 📚 Встановлюємо залежності
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# 🌍 Додаємо змінну середовища для GCP credentials
ENV GOOGLE_APPLICATION_CREDENTIALS="/app/config/autoreportbot-5392a52edec4.json"

ENV PYTHONPATH=/app


# 🚀 Запускаємо Streamlit
CMD ["streamlit", "run", "app/run_app.py", "--server.port=8080", "--server.address=0.0.0.0", "--server.enableCORS=false"]
