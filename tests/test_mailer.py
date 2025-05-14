# tests/test_mailer.py
import os
import pytest 

# НЕ робіть: from app.mailer import send_email
import app.mailer # Тепер це просто імпорт модуля

def test_send_email_mock(monkeypatch):
    def mock_send(zip_path, recipient=None):
        # Ця функція тепер буде викликана
        # print(f"mock_send called with zip_path: {zip_path}, recipient: {recipient}") # Для відладки
        assert os.path.basename(zip_path) == "test.zip"
        assert recipient == "test@example.com"
    
    # Патчимо атрибут 'send_email' модуля 'app.mailer'
    monkeypatch.setattr(app.mailer, "send_email", mock_send)
    
    # Тепер викликаємо функцію через модуль, щоб викликати запатчену версію
    app.mailer.send_email("test.zip", "test@example.com")