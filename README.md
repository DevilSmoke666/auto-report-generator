📋 AUTO-REPORT-GENERATORГенерує PDF-звіти з Google Таблиць або CSV-файлів, архівує в ZIP і надсилає клієнтам на email — автоматично (через main.py) або через веб-інтерфейс Streamlit (run_app.sh). Включає аналіз даних за допомогою Gemini API.🔍 ОглядЦей проєкт автоматизує процес створення персоналізованих звітів. Він отримує дані з вказаного джерела, обробляє їх, генерує резюме за допомогою Gemini API, формує PDF-документи на основі HTML-шаблонів, архівує їх та надсилає на вказану електронну пошту.Основні можливості:✅ Зчитування даних з Google Sheets за ID або з завантаженого CSV-файлу.✅ Інтерактивне мапування стовпців для CSV-файлів через Streamlit UI.✅ Генерація текстового резюме для кожного запису за допомогою Google Gemini API.✅ Формування PDF-звітів на основі HTML-шаблонів з використанням jinja2 та weasyprint.✅ Архівування всіх згенерованих PDF-звітів у єдиний ZIP-файл.✅ Надсилання ZIP-архіву на вказану email-адресу через Gmail SMTP.✅ Багатомовний веб-інтерфейс на Streamlit для ручного запуску та налаштування.✅ Альтернативний запуск через скрипт main.py (наприклад, для автоматизації).✅ Безпечне управління секретами та API ключами через змінні середовища (підтримка .env файлів та GitHub Secrets/Google Secret Manager).🧰 Стек технологійМова програмування: Python 3.12+Веб-інтерфейс: StreamlitРобота з даними: pandasGoogle Sheets: gspread, google-auth, oauth2clientГенерація PDF: WeasyPrint, Jinja2Надсилання Email: smtplib (для SMTP)AI для резюме: google-generativeai (Gemini API)Управління залежностями: pip, requirements.txtЗмінні середовища: python-dotenvКонтейнеризація: DockerХмарна платформа: Google Cloud RunCI/CD: GitHub Actions (в планах)⚙️ Налаштування та ЗапускПередумовиPython 3.12 або новіше.pip для встановлення залежностей.Доступ до Google Cloud Platform для налаштування Google Sheets API та Gemini API.Акаунт Gmail з увімкненою двофакторною автентифікацією та згенерованим "паролем додатка" для SMTP.1. Клонування репозиторіюgit clone [https://github.com/DevilSmoke666/auto-report-generator.git](https://github.com/DevilSmoke666/auto-report-generator.git)
cd auto-report-generator
2. Налаштування СекретівДля локальної розробки (включаючи GitHub Codespaces):Створіть файл .env у корені проекту, скопіювавши вміст з .env.local або .env.production.Для GitHub Codespaces: Налаштуйте Repository secrets в налаштуваннях репозиторію (Settings -> Secrets and variables -> Codespaces). Додаток автоматично прочитає їх як змінні середовища.Необхідні змінні:GOOGLE_CREDENTIALS_JSON: Вміст вашого JSON-ключа сервісного акаунта Google.GOOGLE_SHEET_ID: ID вашої Google Таблиці за замовчуванням.GEMINI_API_KEY: Ваш ключ Gemini API.EMAIL_HOST: напр., smtp.gmail.comEMAIL_PORT: напр., 465EMAIL_USER: Ваша адреса Gmail.EMAIL_APP_PASSWORD: Ваш 16-значний пароль додатка.3. Встановлення залежностейpip install -r requirements.txt
4. Запуск додаткуЧерез Streamlit UI:bash run_app.sh
Відкрийте надану URL-адресу у вашому браузері.Через main.py (для автоматичного запуску):python main.py
🚀 Деплой на Google Cloud RunЦей додаток може бути розгорнутий на Google Cloud Run за допомогою Docker.Основні кроки:Підготуйте Dockerfile (приклад наведено нижче).Збережіть ваші секрети в Google Secret Manager.Зберіть Docker-образ та опублікуйте його в Google Artifact Registry.Розгорніть сервіс на Cloud Run, підключивши секрети з Secret Manager.Налаштуйте IAM дозволи для доступу до секретів.Приклад Dockerfile:# Використовуємо офіційний легкий образ Python
FROM python:3.12-slim

# Встановлюємо системні залежності для weasyprint
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpango-1.0-0 libpangocairo-1.0-0 \
    libpangoft2-1.0-0 libgdk-pixbuf2.0-0 libffi-dev curl fonts-dejavu \
    && rm -rf /var/lib/apt/lists/*

# Встановлюємо робочу директорію
WORKDIR /app

# Встановлюємо залежності Python
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Копіюємо решту коду
COPY . .

# Встановлюємо PYTHONPATH
ENV PYTHONPATH "${PYTHONPATH}:/app"

# Вказуємо порт
EXPOSE 8080

# Команда для запуску Streamlit
CMD ["python", "-m", "streamlit", "run", "app/run_app.py", "--server.port", "$PORT", "--server.address", "0.0.0.0", "--server.enableCORS=false"]
Для отримання детальних інструкцій з розгортання, будь ласка, зверніться до відповідного посібника.