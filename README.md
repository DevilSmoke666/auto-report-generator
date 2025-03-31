# 📄 Auto Report Generator

Автоматичний генератор PDF-звітів на основі даних із Google Sheets.  
Ідеально підходить для SEO-аудитів, технічних оновлень, статусів проектів та іншого клієнтського фідбеку.

---

## 🚀 Можливості

- 🔗 Підключення до Google Sheets (API)
- 📥 Зчитування даних про клієнтів, задачі, статуси, дати, коментарі
- 📄 Автоматичне формування індивідуальних PDF-звітів
- 🖋️ Гнучкий HTML-шаблон для кастомного стилю
- 📂 Групування звітів у директорії `reports/`

---

## 🛠️ Технології

- Python 3.10+
- [gspread](https://github.com/burnash/gspread)
- [WeasyPrint](https://weasyprint.org/)
- [Jinja2](https://jinja.palletsprojects.com/)

---

## 📦 Встановлення

```bash
git clone https://github.com/yourusername/auto-report-generator.git
cd auto-report-generator
pip install -r requirements.txt
