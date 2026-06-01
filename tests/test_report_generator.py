from system.stats import ReportGenerator

def test_add_new_category():
    report = ReportGenerator()
    report.add("security", True)
    assert report.stats == {"security": {"total": 1, "urgent": 1}}

def test_add_urgent_email():
    report = ReportGenerator()
    report.add('security',True)

    assert report.stats['security']['total'] == 1
    assert report.stats['security']['urgent'] == 1

def test_add_multiple_emails():
    report = ReportGenerator()

    report.add('spam',False)
    report.add('spam',True)

    assert report.stats['spam']['total'] == 2
    assert report.stats['spam']['urgent'] == 1

def test_multiple_categories():
    report = ReportGenerator()

    report.add('spam',False)
    report.add('security',True)

    assert len(report.stats) == 2
    assert report.stats['spam']['total'] == 1
    assert report.stats['security']['urgent'] == 1