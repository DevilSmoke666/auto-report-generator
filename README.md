# 📊 AUTO-REPORT-GENERATOR

> Автоматичний генератор звітів з Google Таблиць у форматі PDF із надсиланням на email

---

## 🚀 Що робить цей проєкт?

Цей інструмент:
- Зчитує інформацію з Google Таблиці (API)
- Формує індивідуальні PDF-звіти з шаблону (HTML ➞ PDF)
- Генерує аналітичне summary за допомогою Google Gemini API
- Створює ZIP-архів зі звітами
- Надсилає HTML-лист із вкладеним архівом на вказану адресу email

---

## 📁 Структура проєкту

```
├── main.py                  # Основна точка запуску
├── email_sender.py         # Надсилання листів з HTML-оформленням
├── gsheet.py               # Зчитування з Google Sheets
├── pdf_generator.py        # Генерація PDF з шаблону
├── gpt_writer.py           # Використання Gemini для summary
├── templates/
│   ├── report_template.html    # PDF-шаблон
│   └── email_template.html     # HTML-шаблон для email
├── credentials.json        # Ключі до Google Sheets
├── .env                    # Приховані змінні: email, паролі, ключі
├── all_reports.zip         # Згенерований архів для надсилання
├── requirements.txt        # Бібліотеки Python
├── Makefile                # Простий запуск команди (make run / test)
```

---

## 🧠 Технології

- `Python 3.12`
- `jinja2`, `pdfkit`, `wkhtmltopdf` — генерація PDF
- `google-api-python-client`, `gspread` — інтеграція з Google Sheets
- `Gemini API` (Google Generative AI) — smart summary
- `email.mime`, `smtplib` — надсилання email
- `dotenv`, `Makefile` — зручно й безпечно

---

## 🛠️ Як запустити?

1. 🔑 Отримай Google API credentials (service account JSON)
2. 📄 Створи файл `.env` з:
```
EMAIL_USER=...
EMAIL_APP_PASSWORD=...
EMAIL_TO=...
GOOGLE_SHEET_ID=...
GEMINI_API_KEY=...
```
3. 📦 Встанови залежності:
```bash
pip install -r requirements.txt
```
4. ▶️ Запуск:
```bash
make run  # Генерація звітів та email
make test # Перевірка доступу до API (Gemini / Sheets / Email)
```

---

## 📨 Приклад листа

HTML-лист із стилізованим повідомленням і кнопкою для завантаження архіву:

```
[✓] Email з HTML: all_reports.zip надіслано!
```

---

## 📌 План подальших покращень

- [ ] ✅ Динамічне вказання email з таблиці (пер клієнт)
- [ ] Web-інтерфейс через Streamlit
- [ ] Telegram-бот інтеграція
- [ ] CI/CD через GitHub Actions
- [ ] Docker-версія (для деплою на сервер)
- [ ] Вивантаження архіву в Google Drive або Firebase

---

## 🙌 Автор
Ярослав @DevilSmoke666 — Python-розробник, Crypto-аналітик, AI-інтегратор ✨

---

## 🧠 Команда підтримки
Пишіть у чат-бота, якщо хочете розгорнути власного звіт-бота у своїй компанії.

