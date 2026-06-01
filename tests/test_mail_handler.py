from system.handler import MailHandler
from system.stats import ReportGenerator
def test_file_not_found(tmp_path):
    handler = MailHandler(
        str(tmp_path / "inbox"),
        str(tmp_path / "processed")
    )

    mock_stats = ReportGenerator()

    result = handler.handle_one("no_such_file.txt",mock_stats)

    assert result is None

def test_non_utf8_email(non_utf8_email, tmp_path):
    inbox = tmp_path / "inbox"
    processed = tmp_path / "processed"

    inbox.mkdir()
    processed.mkdir()
    (processed / "unknown").mkdir()
    file = inbox / "bad.txt"

    with open(file, "wb") as f:
        f.write(non_utf8_email)
    
    handler = MailHandler(str(inbox), str(processed))

    mock_stats = ReportGenerator()
    
    res = handler.handle_one(str(file),mock_stats)

    assert res == ('unknown', False)

def test_blank_mail(blank_mail, tmp_path):
    inbox = tmp_path / "inbox"
    processed = tmp_path / "processed"

    inbox.mkdir()
    processed.mkdir()

    file = inbox / "blank.txt"
    file.write_text(blank_mail, encoding="utf-8")

    handler = MailHandler(str(inbox), str(processed))
    mock_stats = ReportGenerator()

    res = handler.handle_one(str(file),mock_stats)

    assert res is None or res == ('unknown', False)

def test_security_email(tmp_path):
    inbox = tmp_path / "inbox"
    processed = tmp_path / "processed"

    inbox.mkdir()
    processed.mkdir()
    (processed / "security").mkdir()
    
    file = inbox / "mail.txt"

    file.write_text("""От кого: User
Тема: Взлом аккаунта
                    
Обнаружена утечка данных""", 
    encoding="utf-8"
    )

    handler = MailHandler(str(inbox),str(processed))
    mock_stats = ReportGenerator()

    handler.handle_one(str(file),mock_stats)

    assert not file.exists()