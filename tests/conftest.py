import pytest
from system.mail import Email

@pytest.fixture()
def normal_email():
    return Email(
        name ='Леонардо Ди Каприо',
        sender_email='leonardodicaprio@company.ru',
        theme ='Не работает принтер',
        content="""
Добрый день, коллеги!
Принтер не печатает уже второй день.
""",
        path ="normal_email.txt"
    )

@pytest.fixture()
def urgent_email():
    return Email(
        name ='Сабрина Карпентер',
        sender_email='it-support@company.ru',
        theme='Срочно! Взлом аккаунта',
        content="""
Срочно!
Мой аккаунт был взломан, срочно помогите восстановить доступ!""",
        path = "urgent_email.txt",
    )

@pytest.fixture()
def spam_email():
    return Email(
        name='Рекламная рассылка',
        sender_email='winprize@gmail.com',
        theme='Вы стали победителем!',
        content="""
Уважаемый пользователь,
Вы стали победителем нашего розыгрыша и выиграли 1.000.000 рублей! 
Чтобы получить свой приз, пожалуйста, перейдите по ссылке ниже и заполните форму с вашими данными.
[Получить приз](http://67easywin.com/prize)
""",
        path="spam_email.txt",
        )

@pytest.fixture()
def monitoring_email():
    return Email(
        name='System Monitoring',
        sender_email='system@company.ru',
        theme='WARNING',
        content ="""Сервис: API Gateway
CPU usage: 85%
""",
        path="monitoring_email.txt"
    )

@pytest.fixture()
def upper_case_email():
    return Email(
        name='Брэд Питт',
        sender_email='brad@company.ru',
        theme='СРОЧНО! ВЗЛОМ АККАУНТА',
        content=""" ТРЕБУЕТСЯ НЕОТЛОЖНАЯ ПОМОЩЬ!""",
        path="upper_case_email.txt"
    )


@pytest.fixture()
def email_with_attachments():
    return Email(
        name='Ким Йена',
        sender_email='kim@company.ru',
        theme='Важные документы',
        content='Здравствуйте,\nНаправляю документы для ознакомления и согласования.',
        path='email_with_attachments.txt',
        attachments=['трудовой_договор.pdf', 'политика_безопасности.docx']
    )

# ТЕСТЫ MAILHANDLER

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