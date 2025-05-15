#!/bin/sh
# entrypoint.sh - Скрипт точки входу для Docker-контейнера

# Встановлюємо строгий режим: виходити при помилці, виходити при використанні неініціалізованих змінних
set -e
set -u

# --- Налаштування шляхів до файлів облікових даних ---
# Ці змінні середовища мають бути встановлені у Dockerfile (через ENV)
# і вказувати, куди entrypoint.sh має записати вміст секретів.
# Приклад з Dockerfile:
# ENV GOOGLE_APPLICATION_CREDENTIALS="/app/config/gcp_credentials.json"
# ENV GMAIL_CREDENTIALS_PATH="/app/config/gmail_token.json"

GCP_CREDS_FILE_PATH="${GOOGLE_APPLICATION_CREDENTIALS}"
GMAIL_CREDS_FILE_PATH="${GMAIL_CREDENTIALS_PATH}"

# Назви змінних середовища, які будуть містити ВМІСТ файлів JSON
# Ці змінні ти маєш надати контейнеру під час запуску (наприклад, з секретів GitHub Codespaces)
GCP_SECRET_ENV_VAR_NAME="GOOGLE_CREDENTIALS_JSON"
GMAIL_SECRET_ENV_VAR_NAME="GMAIL_CREDENTIALS_CONTENT"

# --- Функція для створення файлу з секрету ---
create_secret_file() {
  local secret_content_env_var_name="$1" # Назва змінної середовища, що містить вміст секрету
  local target_file_path="$2"          # Шлях, куди записати файл

  # Перевіряємо, чи встановлена змінна середовища з вмістом секрету
  # Використовуємо eval для отримання значення змінної за її ім'ям
  eval "secret_content=\${$secret_content_env_var_name}"

  if [ -n "$secret_content" ]; then
    # Створюємо каталог для файлу, якщо його немає
    target_dir=$(dirname "$target_file_path")
    mkdir -p "$target_dir"
    
    # Записуємо вміст секрету у файл
    echo "$secret_content" > "$target_file_path"
    chmod 600 "$target_file_path" # Встановлюємо обмежені права на файл
    echo "Інформація: Файл облікових даних '$target_file_path' успішно створено з змінної середовища '$secret_content_env_var_name'."
  else
    echo "ПОПЕРЕДЖЕННЯ: Змінна середовища '$secret_content_env_var_name' не встановлена або порожня. Файл '$target_file_path' не буде створено."
  fi
}

# --- Створення файлів облікових даних ---
echo "Інформація: Запускається entrypoint.sh..."

# Створюємо файл для Google Cloud Platform credentials
if [ -n "$GCP_CREDS_FILE_PATH" ]; then
  create_secret_file "$GCP_SECRET_ENV_VAR_NAME" "$GCP_CREDS_FILE_PATH"
else
  echo "ПОПЕРЕДЖЕННЯ: Змінна GOOGLE_APPLICATION_CREDENTIALS (шлях до файлу) не встановлена у Dockerfile."
fi

# Створюємо файл для Gmail credentials
if [ -n "$GMAIL_CREDS_FILE_PATH" ]; then
  create_secret_file "$GMAIL_SECRET_ENV_VAR_NAME" "$GMAIL_CREDS_FILE_PATH"
else
  echo "ПОПЕРЕДЖЕННЯ: Змінна GMAIL_CREDENTIALS_PATH (шлях до файлу) не встановлена у Dockerfile."
fi

echo "Інформація: Завершено створення файлів облікових даних. Запускається основна команда контейнера..."
echo "Команда: $@" # Виводимо команду, яка буде виконана

# Виконуємо команду, передану як аргументи до цього скрипта
# (тобто, те, що вказано в CMD у Dockerfile)
exec "$@"
