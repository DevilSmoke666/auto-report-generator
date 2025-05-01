# ▶️ Запуск Streamlit-додатку
run:
	PYTHONPATH=. streamlit run app/run_app.py

# 🧪 Запуск Pytest
test:
	PYTHONPATH=. pytest tests/

# 🎨 Форматування коду
format:
	black . --line-length 100

# 🔍 Лінтинг (flake8)
lint:
	flake8 . --ignore=E501

# 🚀 Streamlit окремо
streamlit:
	streamlit run app/app.py

# 🔄 Запуск усього проєкту (формат, лінт, тести, Streamlit)
project: format lint unittest
	streamlit run app/app.py

# ☁️ Build & deploy на GCP
build:
	gcloud builds submit --tag gcr.io/autoreportbot/auto-report .

deploy:
	gcloud run deploy auto-report \
		--image gcr.io/autoreportbot/auto-report \
		--platform managed \
		--region europe-west1 \
		--allow-unauthenticated

# 🧪 Юніт-тести (з правильним шляхом)
unittest:
	PYTHONPATH=. pytest tests/

# 🧾 Тестування конфігів окремо
test-config:
	PYTHONPATH=. pytest tests/test_config.py

# 🔁 Збірка і деплой
all: build deploy
