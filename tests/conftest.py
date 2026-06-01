import pytest
from system.mail import Email

@pytest.fixture()
def normal_email():
    return Email(
        name = 'Леонардо Ди Каприо',
        theme = 'Не работает принтер',
        content="""
Добрый день, коллеги!
Принтер не печатает уже второй день.""",
        path = "normal_email.txt"
    )

@pytest.fixture()
def urgent_email():
    return Email(
        name = 'Сабрина Карпентер',
        
Кому: it-support@company.ru
Тема: Срочно! Взлом аккаунта

Срочно!
Мой аккаунт был взломан, срочно помогите восстановить доступ!
"""
    )

@pytest.fixture()
def spam_email():
    return """От кого: Рекламная рассылка
Тема: Вы стали победителем!

Уважаемый пользователь,
Вы стали победителем нашего розыгрыша и выиграли 1.000.000 рублей! 
Чтобы получить свой приз, пожалуйста, перейдите по ссылке ниже и заполните форму с вашими данными.
[Получить приз](http://67easywin.com/prize)
"""

@pytest.fixture()
def monitoring_email():
    return """От кого: System Monitoring <system@company.ru>
Тема: WARNING

Сервис: API Gateway
CPU usage: 85%
"""

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
def non_utf8_email():
    return b"\xff\xfe\xff\xfe"

@pytest.fixture()
def blank_mail():
    return ""

@pytest.fixture()
def upper_case_email():
    return """От кого: Брэд Питт 
Тема: СРОЧНО! ВЗЛОМ АККАУНТА

ТРЕБУЕТСЯ НЕОТЛОЖНАЯ ПОМОЩЬ!
"""

@pytest.fixture()
def email_with_attachments():
    return """От кого: Ким Йена
Кому: all@company.ru
Тема: Важные документы

Здравствуйте,
Направляю документы для ознакомления и согласования.

Прикрепил: трудовой_договор.pdf, политика_безопасности.docx, должностная_инструкция.pdf
"""