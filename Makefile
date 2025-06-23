# ==============================================================================
# Makefile для Auto-Report Generator
#
# Цей Makefile автоматизує типові завдання розробки та розгортання для вашої
# Streamlit програми, забезпечуючи узгодженість між середовищами, включаючи
# GitHub Codespaces.
# ==============================================================================

# --- Змінні ---
# Визначте назву директорії вашого віртуального середовища
VENV_DIR = venv

# Шлях до виконуваного файлу Python всередині віртуального середовища
PYTHON_BIN = $(VENV_DIR)/bin/python

# Шлях до виконуваного файлу Streamlit всередині віртуального середовища
STREAMLIT_BIN = $(VENV_DIR)/bin/streamlit

# Шлях до виконуваного файлу pytest всередині віртуального середовища
PYTEST_BIN = $(VENV_DIR)/bin/pytest

# Шлях до виконуваного файлу black всередині віртуального середовища
BLACK_BIN = $(VENV_DIR)/bin/black

# Шлях до виконуваного файлу flake8 всередині віртуального середовища
FLAKE8_BIN = $(VENV_DIR)/bin/flake8

# Google Cloud Project ID (replace with your actual project ID if needed)
# You might fetch this from gcloud config or set it explicitly
GCP_PROJECT_ID = autoreportbot # <-- ВАЖЛИВО: ЗАМІНІТЬ НА ВАШ ФАКТИЧНИЙ ID ПРОЄКТУ GCP
GCR_IMAGE_NAME = gcr.io/$(GCP_PROJECT_ID)/auto-report
GCP_REGION = europe-west1
CLOUD_RUN_SERVICE_NAME = auto-report

# --- Phony Targets (запобігає конфліктам з файлами з такою ж назвою) ---
.PHONY: setup run streamlit test format lint unittest build deploy all clean


# --- Основні завдання розробки ---

# setup: Створює та ініціалізує віртуальне середовище, потім встановлює залежності.
# Це має бути перша команда, яку ви запускаєте при клонуванні репозиторію або відкритті Codespace.
setup:
	@echo "✨ Налаштування віртуального середовища та встановлення залежностей..."
	@if [ -d "$(VENV_DIR)" ]; then \
		echo "Видаляємо існуюче віртуальне середовище: $(VENV_DIR)..."; \
		rm -rf $(VENV_DIR); \
	fi
	@echo "Створення нового віртуального середовища у $(VENV_DIR)..."
	python3 -m venv $(VENV_DIR)
	@echo "Оновлення pip та встановлення вимог у віртуальне середовище..."
	$(PYTHON_BIN) -m pip install --upgrade pip
	$(PYTHON_BIN) -m pip install -r requirements.txt
	@echo "✅ Налаштування завершено. Тепер ви можете запустити 'make run'."


# run: Запускає Streamlit програму з правильно встановленим `PYTHONPATH`.
# Це для локального тестування в Codespaces.
run:
	@echo "🚀 Запуск Streamlit програми..."
	PYTHONPATH=. $(STREAMLIT_BIN) run app/run_app.py


# streamlit: Псевдонім для таргету 'run'.
streamlit: run


# test: Запускає всі тести (поки що заглушка, використовує таргет pytest).
test: unittest


# format: Форматує код Python за допомогою Black.
format:
	@echo "🎨 Форматування коду за допомогою Black..."
	$(BLACK_BIN) . --line-length 100
	@echo "✅ Форматування завершено."


# lint: Перевіряє код Python на стильові помилки за допомогою Flake8.
lint:
	@echo "🔍 Перевірка коду за допомогою Flake8..."
	$(FLAKE8_BIN) . --ignore=E501
	@echo "✅ Перевірка завершена."


# unittest: Запускає юніт-тести за допомогою Pytest.
unittest:
	@echo "🧪 Запуск юніт-тестів за допомогою Pytest..."
	PYTHONPATH=./ $(PYTEST_BIN) tests/
	@echo "✅ Юніт-тести завершено."


# project: Запускає форматування, лінтинг, юніт-тести, а потім запускає Streamlit.
project: format lint unittest run


# --- Завдання розгортання Google Cloud ---

# build: Створює образ Docker та завантажує його до Google Container Registry (GCR).
build:
	@echo "📦 Створення образу Docker та завантаження до GCR: $(GCR_IMAGE_NAME)..."
	gcloud builds submit --tag $(GCR_IMAGE_NAME) .
	@echo "✅ Образ Docker створено та завантажено."

# deploy: Розгортає програму в Google Cloud Run.
deploy:
	@echo "🚀 Розгортання до сервісу Google Cloud Run: $(CLOUD_RUN_SERVICE_NAME) у регіоні $(GCP_REGION)..."
	gcloud run deploy $(CLOUD_RUN_SERVICE_NAME) \
		--image $(GCR_IMAGE_NAME) \
		--platform managed \
		--region $(GCP_REGION) \
		--allow-unauthenticated
	@echo "✅ Розгортання до Cloud Run завершено."


# all: Виконує повну послідовність збірки та розгортання.
all: build deploy


# --- Допоміжні завдання ---

# clean: Очищає артефакти збірки та віртуальне середовище.
clean:
	@echo "🧹 Очищення згенерованих файлів та віртуального середовища..."
	rm -rf $(VENV_DIR)
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	@echo "✅ Очищення завершено."