# 🐍 Базовий образ Python
FROM python:3.12-slim

# Встановлюємо змінні середовища для Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 🧰 Встановлюємо системні залежності
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpangocairo-1.0-0 \
    libpango-1.0-0 \
    libgdk-pixbuf2.0-0 \
    libffi-dev \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 📁 Встановлюємо робочу директорію всередині контейнера
WORKDIR /app

# 📦 Спочатку копіюємо тільки файл залежностей для кешування
COPY ./requirements.txt /app/requirements.txt

# 📚 Встановлюємо залежності Python
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# 🌍 Встановлюємо шляхи для облікових даних та PYTHONPATH
# Файли за цими шляхами будуть створені скриптом entrypoint.sh
ENV GOOGLE_APPLICATION_CREDENTIALS="/app/config/gcp_credentials.json"
ENV GMAIL_CREDENTIALS_PATH="/app/config/gmail_token.json" # Або як ти його називаєш у config.py
ENV PYTHONPATH="/app"

# 📄 Копіюємо необхідні частини проєкту
# Важливо: .dockerignore має виключати реальні файли секретів з app/config/
COPY ./app /app/app                     # Твій основний пакет 'app'
COPY ./templates /app/templates         # HTML шаблони
COPY ./run_app.py /app/run_app.py       # Головний скрипт Streamlit
COPY ./gpt_writer.py /app/gpt_writer.py # Скрипт для роботи з GPT
# Якщо main.py потрібен для роботи контейнера, додай його:
# COPY ./main.py /app/main.py
# Якщо каталог config з app/config/ містить якісь НЕсекретні файли, які потрібні,
# їх можна копіювати окремо, але НЕ копіюй весь каталог app/config напряму, якщо там секрети.
# Краще, щоб entrypoint.sh створював каталог /app/config, якщо його немає.

# 📜 Копіюємо скрипт entrypoint.sh та робимо його виконуваним
COPY ./entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# 🚪 Відкриваємо порт
EXPOSE 8080

# 🚦 Вказуємо entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]

# 🚀 Команда за замовчуванням для Streamlit
# Запускає /app/run_app.py всередині контейнера
CMD [ "streamlit", "run", "run_app.py", "--server.port=8080", "--server.address=0.0.0.0", "--server.enableCORS=false" ]
