# tests/test_context_builder.py
from app.context_builder import build_context

def mock_translate(key, lang="ua", **kwargs):
    """Проста мок-функція для перекладу."""
    translations_ua = {
        "client": "Клієнт",
        "task": "Завдання",
        "status": "Статус",
        "date": "Дата",
        "comments": "Коментарі",
        "summary": "Резюме",
        "footer": "Підвал",
        "title": "Тестовий Заголовок Звіту" # Приклад заголовка
    }
    # Додайте інші мови та ключі за потреби
    if lang == "ua":
        return translations_ua.get(key, f"TR_{key}_{lang}")
    return f"TR_{key}_{lang}"

def test_build_context(mocker):
    """
    Тестує функцію build_context з мокуванням generate_summary та tr.
    """
    record = {
        'client': 'Client A', # Це значення НЕ використовується для ctx['client'] напряму
        'task': 'SEO Audit',
        'status': 'Pending',
        'date': '2024-05-01',
        'comments': 'Initial draft'
    }

    # Мокуємо функцію generate_summary
    # Шлях 'app.context_builder.generate_summary' коректний, оскільки
    # build_context імпортує generate_summary з gpt_writer у свій неймспейс.
    mocked_generate_summary = mocker.patch('app.context_builder.generate_summary')
    expected_summary_text = "Це резюме, згенероване моком для тестування."
    mocked_generate_summary.return_value = expected_summary_text

    # Мокуємо функцію tr, яку використовує build_context
    # Шлях 'app.context_builder.tr' коректний, оскільки
    # build_context імпортує tr з .lang у свій неймспейс.
    mocked_tr = mocker.patch('app.context_builder.tr', side_effect=mock_translate)

    # Викликаємо build_context. Мова за замовчуванням "ua".
    ctx = build_context(record)

    # Перевіряємо, що змоковані функції були викликані
    mocked_generate_summary.assert_called_once()
    # mocked_tr викликається багато разів, тому перевіряємо конкретні важливі виклики, якщо потрібно,
    # або просто факт виклику (mocker.ANY можна використати для аргументів)
    # Наприклад, перевіримо, що tr викликалася для 'client'
    mocked_tr.assert_any_call("client", "ua")
    mocked_tr.assert_any_call("title", "ua")


    # Перевіряємо вміст контексту (ctx)
    assert 'title' in ctx
    assert ctx['title'] == mock_translate("title", "ua") # "Тестовий Заголовок Звіту"

    assert 'client' in ctx
    # ctx['client'] буде результатом tr("client", "ua"), оскільки record не має 'client_name'
    assert ctx['client'] == mock_translate("client", "ua") # "Клієнт"

    assert 'task' in ctx
    assert ctx['task'] == record['task'] # 'SEO Audit'

    assert 'status' in ctx
    assert ctx['status'] == record['status'] # 'Pending'

    assert 'date' in ctx
    assert ctx['date'] == record['date'] # '2024-05-01'

    assert 'comments' in ctx
    assert ctx['comments'] == record['comments'] # 'Initial draft'

    assert 'summary' in ctx
    assert ctx['summary'] == expected_summary_text

    assert 'labels' in ctx
    assert isinstance(ctx['labels'], dict)
    assert ctx['labels']['client'] == mock_translate("client", "ua") # "Клієнт"
    assert ctx['labels']['task'] == mock_translate("task", "ua")     # "Завдання"
    # ... і так далі для інших міток, якщо потрібно детально перевіряти

    assert 'lang' in ctx
    assert ctx['lang'] == "ua"
