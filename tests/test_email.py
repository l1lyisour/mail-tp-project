import pytest

@pytest.fixture()
def email_without_theme():
    return """От кого: Элл Вудс

Не работает компьютер, не могу войти в систему.
"""

@pytest.fixture()
def email_only_theme():
    return """От кого: Владимир Братишкин
Тема: Ошибка браузера
"""

@pytest.fixture()
def multi_category_email():
    return """От кого: Илья Мазеллов
Тема: Срочно! 

Обнаружена утечка данных.
Также действует скидка на услуги.
"""

@pytest.fixture()
def urgent_unknown_email():
    return """От кого: Иван Бессмертных
Тема: Срочно

Просто хотел уточнить вопрос по проекту.
"""

@pytest.fixture()
def empty_email():
    return """От кого: noreply@monitoring.internal
"""

@pytest.fixture()
def blank_mail():
    return ""

@pytest.fixture()
def non_utf8_email():
    return b"\xff\xfe\xff\xfe"