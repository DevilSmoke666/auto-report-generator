from jinja2 import Environment, FileSystemLoader


# 🧩 Функція для генерації PDF з HTML-шаблону
def generate_pdf(context, output_path):
    # ⬇️ Імпортуємо WeasyPrint лише при необхідності (щоб уникнути помилок у середовищі без libgobject)
    from weasyprint import HTML

    # Підключаємо шаблон із папки templates
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("report_template.html")

    # Генеруємо HTML з контексту
    html_out = template.render(context)

    # Створюємо PDF-файл
    HTML(string=html_out).write_pdf(output_path)
