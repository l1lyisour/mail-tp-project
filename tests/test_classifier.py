import pytest
from system.classifier import Classifier
from system.mail import Email

@pytest.fixture
def classifier():
    return Classifier()

def test_spam(classifier, spam_email):
    assert classifier.classify(spam_email) == "spam"

def test_urgent(classifier, urgent_email):
    res = classifier.classify(urgent_email)
    assert res == 'security' 
    assert urgent_email.is_urgent is True

def test_monitoring(classifier, monitoring_email):
    assert classifier.classify(monitoring_email) == "technical"

def test_upper_case(classifier, upper_case_email):
    res = classifier.classify(upper_case_email)

    assert res == "security"
    assert upper_case_email.is_urgent is True

# ТЕСТЫ БЕЗ ФИКСТУР

def test_security(classifier):
    email = Email(
        name='User',
        sender_email='hack@company.ru',
        theme='Взлом аккаунта',
        content='Обнаружена утечка данных, срочно помогите!',
        path='security_email.txt'
    )
    res = classifier.classify(email)
    assert res == "security"
    assert email.is_urgent is True

def test_unknown_email(classifier):
    email = Email(
        name='User1',
        sender_email='test@company.ru',
        theme='Привет',
        content='Просто хотел сказать привет.',
        path='unknown_email.txt'
    )
    res = classifier.classify(email)
    assert res == "unknown"
    assert email.is_urgent is False

def test_multi_category_email(classifier):
    email = Email(
        name='User2',
        sender_email='test@company.ru',
        theme='Срочно! Взлом и скидка',
        content='Скидка и утечка данных',
        path='multi_category_email.txt'
    )
    res = classifier.classify(email)
    assert res == "security"

def test_finance_email(classifier):
    email = Email(
        name='Бухгалтерия',
        sender_email='finance@company.ru',
        theme='Оплата счета',
        content='Пожалуйста, оплатите счет до 30 июня.',
        path='finance_email.txt'
    )
    res = classifier.classify(email)
    assert res == "finance"

def test_documents_email(classifier):
    email = Email(
        name='Офис',
        sender_email='docs@company.ru',
        theme='Согласование отчёта',
        content='Пожалуйста, согласуйте отчёт до конца недели.',
        path='documents_email.txt'
    )
    res = classifier.classify(email)
    assert res == "documents"

def test_access_email(classifier):
    email = Email(
        name='ИТ отдел',
        sender_email='it@company.ru',
        theme='Инструкция по доступу',
        content='Прикрепляю инструкцию по восстановлению доступа.',
        path='access_email.txt'
    )
    res = classifier.classify(email)
    assert res == "access"

def test_aho_email(classifier):
    email = Email(
        name='Закупки',
        sender_email='aho@company.ru',
        theme='Заявка на оборудование',
        content='Пожалуйста, оформите заявку на новую гарнитуру.',
        path='aho_email.txt'
    )
    res = classifier.classify(email)
    assert res == "aho"

def test_hr_email(classifier):
    email = Email(
        name='HR',
        sender_email='hr@company.ru',
        theme='Отпуск',
        content='Напоминаем о необходимости согласовать отпуск.',
        path='hr_email.txt'
    )
    res = classifier.classify(email)
    assert res == "hr"

def test_events_email(classifier):
    email = Email(
        name='Организатор',
        sender_email='events@company.ru',
        theme='Приглашение на мероприятие',
        content='Приглашаем вас на корпоративное мероприятие в пятницу.',
        path='events_email.txt'
    )
    res = classifier.classify(email)
    assert res == "events"