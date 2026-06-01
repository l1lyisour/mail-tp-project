import pytest
from system.mail import Email

def test_email_creation():
    email = Email(
        name='Иван Иванов',
        sender_email='ivanov@company.ru',
        content='Привет',
        theme='Тема',
        path='file.txt'
    )

    assert email.name == 'Иван Иванов'
    assert email.content == 'Привет'
    assert email.theme == 'Тема'
    assert email.path == 'file.txt'
    assert email.is_urgent == False
    assert email.attachments == []

def test_email_with_attachments():
    email = Email(
        name = 'HR',
        theme='Docs',
        content='...',
        path='file.txt',
        attachments=['a.pdf','b.docx']
    )
    assert email.attachments == ['a.pdf','b.docx']

def test_email_without_attachments():
    email = Email(
        name = 'HR',
        theme='Docs',
        content='...',
        path='file.txt'
    )
    assert email.attachments == []

def test_email_str():
    email = Email(
        name='Иван Иванов',
        theme='Тема',
        content='Привет',
        path='file.txt',
    )

    res = str(email)

    assert 'Иван' in res
    assert 'Тема' in res

