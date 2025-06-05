📋 AUTO-REPORT-GENERATORГенерує PDF-звіти з Google Таблиць або CSV-файлів, архівує в ZIP і надсилає клієнтам на email — автоматично (через main.py) або через веб-інтерфейс Streamlit (run_app.sh). Включає аналіз даних за допомогою Gemini API.🔍 ОглядЦей проєкт автоматизує процес створення персоналізованих звітів. Він отримує дані з вказаного джерела, обробляє їх, генерує резюме за допомогою Gemini API, формує PDF-документи на основі HTML-шаблонів, архівує їх та надсилає на вказану електронну пошту.Основні можливості:✅ Зчитування даних з Google Sheets за ID або з завантаженого CSV-файлу.✅ Інтерактивне мапування стовпців для CSV-файлів через Streamlit UI.✅ Генерація текстового резюме для кожного запису за допомогою Google Gemini API.✅ Формування PDF-звітів на основі HTML-шаблонів з використанням jinja2 та weasyprint.✅ Архівування всіх згенерованих PDF-звітів у єдиний ZIP-файл.✅ Надсилання ZIP-архіву на вказану email-адресу через Gmail SMTP.✅ Багатомовний веб-інтерфейс на Streamlit для ручного запуску та налаштування.✅ Альтернативний запуск через скрипт main.py (наприклад, для автоматизації).✅ Безпечне управління секретами та API ключами через змінні середовища (підтримка .env файлів та GitHub Secrets).🧰 Стек технологійМова програмування: Python 3.12+Веб-інтерфейс: StreamlitРобота з даними: pandasGoogle Sheets: gspread, google-auth, google-auth-oauthlib, oauth2clientГенерація PDF: WeasyPrint, Jinja2Надсилання Email: smtplib (для SMTP)AI для резюме: google-generativeai (Gemini API)Управління залежностями: pip, requirements.txtЗмінні середовища: python-dotenvКонтейнеризація: DockerХмарна платформа (для деплою): Google Cloud Run (рекомендовано)CI/CD (в планах): GitHub Actions⚙️ Налаштування та ЗапускПередумовиPython 3.12 або новіше.pip для встановлення залежностей.Доступ до Google Cloud Platform для налаштування Google Sheets API та Gemini API.Акаунт Gmail з увімкненою двофакторною автентифікацією та згенерованим "паролем додатка" для SMTP.1. Клонування репозиторіюgit clone [https://github.com/DevilSmoke666/auto-report-generator.git](https://github.com/DevilSmoke666/auto-report-generator.git)
cd auto-report-generator
2. Налаштування Середовища та СекретівДодаток використовує змінні середовища для зберігання API ключів та інших конфігурацій.Для локальної розробки (не в Codespace):Створіть файл .env у кореневій папці проекту. Скопіюйте вміст з .env.local або .env.production як шаблон.Заповніть файл .env вашими актуальними значеннями:# Google Cloud / Sheets
GOOGLE_CREDENTIALS_JSON='вміст_вашого_сервісного_ключа_gcp.json' # Весь JSON рядок
GOOGLE_SHEET_ID="ID_вашої_основної_Google_Таблиці"
GOOGLE_SHEET_ID_TEST="ID_вашої_тестової_Google_Таблиці" # Опціонально, для tests/test_connection.py

# Gemini API
GEMINI_API_KEY="Ваш_Gemini_API_ключ"
GEMINI_MODEL_NAME="models/gemini-1.5-pro-latest" # Або інша модель

# Email SMTP (наприклад, для Gmail)
EMAIL_HOST="smtp.gmail.com"
EMAIL_PORT="465" # Для SSL
EMAIL_USER="ваша_gmail_адреса_відправника"
EMAIL_APP_PASSWORD="ваш_16-значний_пароль_додатка_gmail"
EMAIL_TO_DEFAULT="email_отримувача_за_замовчуванням_для_main.py" # Опціонально
EMAIL_TEST_RECIPIENT="email_для_отримання_тестових_листів" # Опціонально, для tests/test_connection.py

# Шляхи та назви файлів
REPORTS_DIR="reports" # Папка для збереження звітів
ZIP_NAME_TEMPLATE="all_reports_{today_date}.zip" # Шаблон для назви архіву
Для GitHub Codespaces:Перейдіть до налаштувань вашого репозиторію на GitHub: Settings -> Secrets and variables -> Codespaces.Натисніть "New repository secret" для кожної змінної, переліченої вище (наприклад, GOOGLE_CREDENTIALS_JSON, GEMINI_API_KEY тощо), та вставте відповідні значення.3. Встановлення залежностейПеребуваючи у кореневій папці проекту, виконайте:pip install -r requirements.txt
4. Запуск додаткуЧерез Streamlit UI:bash run_app.sh
Відкрийте надану Local URL (зазвичай http://localhost:8501) у вашому браузері.Через main.py (для автоматичного запуску з Google Sheets):Цей скрипт використовує GOOGLE_SHEET_ID та EMAIL_MAIN_PY_RECIPIENT (або EMAIL_TO_DEFAULT) з змінних середовища.python main.py
5. Запуск тестів з'єднанняpython tests/test_connection.py
Цей скрипт перевірить підключення до Google Sheets, Gemini API та SMTP, використовуючи відповідні змінні середовища (наприклад, GOOGLE_SHEET_ID_TEST, EMAIL_TEST_RECIPIENT).🚀 Деплой на Google Cloud RunЦей додаток може бути розгорнутий на Google Cloud Run за допомогою Docker. Детальні інструкції дивіться у документі Розгортання Streamlit-додатку на Google Cloud Run.Основні кроки:Підготуйте Dockerfile.Зберіть Docker-образ та опублікуйте його в Google Artifact Registry.Розгорніть сервіс на Cloud Run, вказавши шлях до образу.Налаштуйте змінні середовища (секрети) для сервісу Cloud Run, використовуючи Google Secret Manager.Приклад команд (деталі в посібнику):# (Переконайтеся, що gcloud CLI налаштовано)
# Замініть [PROJECT_ID], [REGION], [REPO_NAME], [IMAGE_NAME], [SERVICE_NAME] на ваші значення

# Збірка образу (локально або через Cloud Build)
export IMAGE_URI="[REGION]-docker.pkg.dev/[PROJECT_ID]/[REPO_NAME]/[IMAGE_NAME]:latest"
docker build -t $IMAGE_URI .
docker push $IMAGE_URI

# Розгортання на Cloud Run
gcloud run deploy [SERVICE_NAME] \
    --image $IMAGE_URI \
    --platform managed \
    --region [REGION] \
    --allow-unauthenticated \
    --set-env-vars "GOOGLE_SHEET_ID=ваш_id,GEMINI_MODEL_NAME=models/gemini-1.5-pro-latest" \
    # Для секретів використовуйте --set-secrets або налаштування через UI з Secret Manager
    # Наприклад: --set-secrets="GEMINI_API_KEY=ваша_назва_секрету_в_secret_manager:latest"
🛠 Структура проектуauto-report-generator/
├── .github/workflows/         # Конфігурації GitHub Actions (для CI/CD)
│ └── tests.yml
├── .tmp/                      # Тимчасові файли (в .gitignore)
├── app/                       # Основний код додатку
│ ├── __init__.py
│ ├── config_fields.py       # Централізована конфігурація полів
│ ├── context_builder.py     # Побудова контексту для PDF
│ ├── email_sender.py        # Надсилання email
│ ├── gsheet.py              # Робота з Google Sheets та CSV
│ ├── pdf_generator.py       # Генерація PDF з HTML шаблону
│ ├── report_generator.py    # Основна логіка генерації та надсилання
│ ├── run_app.py             # Головний файл Streamlit додатку
│ ├── ui_components.py       # Модуль для UI елементів та мовної панелі
│ └── zipper.py              # Архівування файлів
├── reports/                   # Згенеровані звіти (в .gitignore)
├── screenshots/               # Скріншоти для README
├── templates/                 # HTML шаблони
│ ├── email_template.html
│ └── report_template.html
├── tests/                     # Тести
│ ├── __init__.py
│ ├── test_connection.py
│ └── test_email_sender.py   # (Приклад, можна додати більше тестів)
├── .dockerignore
├── .env.local                 # Шаблон для локальних змінних середовища
├── .env.production            # Шаблон для продакшн змінних середовища
├── .gitignore
├── Dockerfile                 # Інструкції для Docker
├── main.py                    # Альтернативна точка входу (наприклад, для cron)
├── Makefile                   # (Якщо використовується для команд збірки/деплою)
├── README.md
└── requirements.txt           # Залежності Python
🔧 Майбутні покращенняПовноцінна реалізація GitHub Actions для CI/CD (автоматичне тестування, збірка Docker, деплой).Розширення мовної підтримки в UI.Додавання більше юніт-тестів та інтеграційних тестів.Можливість вибору HTML-шаблону для звіту через UI.Збереження історії генерації звітів.📋 AUTO-REPORT-GENERATORГенерує PDF-звіти з Google Таблиць або CSV-файлів, архівує в ZIP і надсилає клієнтам на email — автоматично (через main.py) або через веб-інтерфейс Streamlit (run_app.sh). Включає аналіз даних за допомогою Gemini API.🔍 ОглядЦей проєкт автоматизує процес створення персоналізованих звітів. Він отримує дані з вказаного джерела, обробляє їх, генерує резюме за допомогою Gemini API, формує PDF-документи на основі HTML-шаблонів, архівує їх та надсилає на вказану електронну пошту.Основні можливості:✅ Зчитування даних з Google Sheets за ID або з завантаженого CSV-файлу.✅ Інтерактивне мапування стовпців для CSV-файлів через Streamlit UI.✅ Генерація текстового резюме для кожного запису за допомогою Google Gemini API.✅ Формування PDF-звітів на основі HTML-шаблонів з використанням jinja2 та weasyprint.✅ Архівування всіх згенерованих PDF-звітів у єдиний ZIP-файл.✅ Надсилання ZIP-архіву на вказану email-адресу через Gmail SMTP.✅ Багатомовний веб-інтерфейс на Streamlit для ручного запуску та налаштування.✅ Альтернативний запуск через скрипт main.py (наприклад, для автоматизації).✅ Безпечне управління секретами та API ключами через змінні середовища (підтримка .env файлів та GitHub Secrets).🧰 Стек технологійМова програмування: Python 3.12+Веб-інтерфейс: StreamlitРобота з даними: pandasGoogle Sheets: gspread, google-auth, google-auth-oauthlib, oauth2clientГенерація PDF: WeasyPrint, Jinja2Надсилання Email: smtplib (для SMTP)AI для резюме: google-generativeai (Gemini API)Управління залежностями: pip, requirements.txtЗмінні середовища: python-dotenvКонтейнеризація: DockerХмарна платформа (для деплою): Google Cloud Run (рекомендовано)CI/CD (в планах): GitHub Actions⚙️ Налаштування та ЗапускПередумовиPython 3.12 або новіше.pip для встановлення залежностей.Доступ до Google Cloud Platform для налаштування Google Sheets API та Gemini API.Акаунт Gmail з увімкненою двофакторною автентифікацією та згенерованим "паролем додатка" для SMTP.1. Клонування репозиторіюgit clone [https://github.com/DevilSmoke666/auto-report-generator.git](https://github.com/DevilSmoke666/auto-report-generator.git)
cd auto-report-generator
2. Налаштування Середовища та СекретівДодаток використовує змінні середовища для зберігання API ключів та інших конфігурацій.Для локальної розробки (не в Codespace):Створіть файл .env у кореневій папці проекту. Скопіюйте вміст з .env.local або .env.production як шаблон.Заповніть файл .env вашими актуальними значеннями:# Google Cloud / Sheets
GOOGLE_CREDENTIALS_JSON='вміст_вашого_сервісного_ключа_gcp.json' # Весь JSON рядок
GOOGLE_SHEET_ID="ID_вашої_основної_Google_Таблиці"
GOOGLE_SHEET_ID_TEST="ID_вашої_тестової_Google_Таблиці" # Опціонально, для tests/test_connection.py

# Gemini API
GEMINI_API_KEY="Ваш_Gemini_API_ключ"
GEMINI_MODEL_NAME="models/gemini-1.5-pro-latest" # Або інша модель

# Email SMTP (наприклад, для Gmail)
EMAIL_HOST="smtp.gmail.com"
EMAIL_PORT="465" # Для SSL
EMAIL_USER="ваша_gmail_адреса_відправника"
EMAIL_APP_PASSWORD="ваш_16-значний_пароль_додатка_gmail"
EMAIL_TO_DEFAULT="email_отримувача_за_замовчуванням_для_main.py" # Опціонально
EMAIL_TEST_RECIPIENT="email_для_отримання_тестових_листів" # Опціонально, для tests/test_connection.py

# Шляхи та назви файлів
REPORTS_DIR="reports" # Папка для збереження звітів
ZIP_NAME_TEMPLATE="all_reports_{today_date}.zip" # Шаблон для назви архіву
Для GitHub Codespaces:Перейдіть до налаштувань вашого репозиторію на GitHub: Settings -> Secrets and variables -> Codespaces.Натисніть "New repository secret" для кожної змінної, переліченої вище (наприклад, GOOGLE_CREDENTIALS_JSON, GEMINI_API_KEY тощо), та вставте відповідні значення.3. Встановлення залежностейПеребуваючи у кореневій папці проекту, виконайте:pip install -r requirements.txt
4. Запуск додаткуЧерез Streamlit UI:bash run_app.sh
Відкрийте надану Local URL (зазвичай http://localhost:8501) у вашому браузері.Через main.py (для автоматичного запуску з Google Sheets):Цей скрипт використовує GOOGLE_SHEET_ID та EMAIL_MAIN_PY_RECIPIENT (або EMAIL_TO_DEFAULT) з змінних середовища.python main.py
5. Запуск тестів з'єднанняpython tests/test_connection.py
Цей скрипт перевірить підключення до Google Sheets, Gemini API та SMTP, використовуючи відповідні змінні середовища (наприклад, GOOGLE_SHEET_ID_TEST, EMAIL_TEST_RECIPIENT).🚀 Деплой на Google Cloud RunЦей додаток може бути розгорнутий на Google Cloud Run за допомогою Docker. Детальні інструкції дивіться у документі Розгортання Streamlit-додатку на Google Cloud Run.Основні кроки:Підготуйте Dockerfile.Зберіть Docker-образ та опублікуйте його в Google Artifact Registry.Розгорніть сервіс на Cloud Run, вказавши шлях до образу.Налаштуйте змінні середовища (секрети) для сервісу Cloud Run, використовуючи Google Secret Manager.Приклад команд (деталі в посібнику):# (Переконайтеся, що gcloud CLI налаштовано)
# Замініть [PROJECT_ID], [REGION], [REPO_NAME], [IMAGE_NAME], [SERVICE_NAME] на ваші значення

# Збірка образу (локально або через Cloud Build)
export IMAGE_URI="[REGION]-docker.pkg.dev/[PROJECT_ID]/[REPO_NAME]/[IMAGE_NAME]:latest"
docker build -t $IMAGE_URI .
docker push $IMAGE_URI

# Розгортання на Cloud Run
gcloud run deploy [SERVICE_NAME] \
    --image $IMAGE_URI \
    --platform managed \
    --region [REGION] \
    --allow-unauthenticated \
    --set-env-vars "GOOGLE_SHEET_ID=ваш_id,GEMINI_MODEL_NAME=models/gemini-1.5-pro-latest" \
    # Для секретів використовуйте --set-secrets або налаштування через UI з Secret Manager
    # Наприклад: --set-secrets="GEMINI_API_KEY=ваша_назва_секрету_в_secret_manager:latest"
🛠 Структура проектуauto-report-generator/
├── .github/workflows/         # Конфігурації GitHub Actions (для CI/CD)
│ └── tests.yml
├── .tmp/                      # Тимчасові файли (в .gitignore)
├── app/                       # Основний код додатку
│ ├── __init__.py
│ ├── config_fields.py       # Централізована конфігурація полів
│ ├── context_builder.py     # Побудова контексту для PDF
│ ├── email_sender.py        # Надсилання email
│ ├── gsheet.py              # Робота з Google Sheets та CSV
│ ├── pdf_generator.py       # Генерація PDF з HTML шаблону
│ ├── report_generator.py    # Основна логіка генерації та надсилання
│ ├── run_app.py             # Головний файл Streamlit додатку
│ ├── ui_components.py       # Модуль для UI елементів та мовної панелі
│ └── zipper.py              # Архівування файлів
├── reports/                   # Згенеровані звіти (в .gitignore)
├── screenshots/               # Скріншоти для README
├── templates/                 # HTML шаблони
│ ├── email_template.html
│ └── report_template.html
├── tests/                     # Тести
│ ├── __init__.py
│ ├── test_connection.py
│ └── test_email_sender.py   # (Приклад, можна додати більше тестів)
├── .dockerignore
├── .env.local                 # Шаблон для локальних змінних середовища
├── .env.production            # Шаблон для продакшн змінних середовища
├── .gitignore
├── Dockerfile                 # Інструкції для Docker
├── main.py                    # Альтернативна точка входу (наприклад, для cron)
├── Makefile                   # (Якщо використовується для команд збірки/деплою)
├── README.md
└── requirements.txt           # Залежності Python
🔧 Майбутні покращенняПовноцінна реалізація GitHub Actions для CI/CD (автоматичне тестування, збірка Docker, деплой).Розширення мовної підтримки в UI.Додавання більше юніт-тестів та інтеграційних тестів.Можливість вибору HTML-шаблону для звіту через UI.Збереження історії генерації звітів.