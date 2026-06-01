import pytest
from system.classifier import Classifier
from system.mail import Email

def test_spam(classifier, spam_email):
    assert classifier.classify(spam_email) == "spam"

def test_urgent(classifier, urgent_email):
    res = classifier.classify(urgent_email)
    assert res == 'security' 
    assert urgent_email.is_urgent == True

def test_monitoring(classifier, monitoring_email):
    assert classifier.classify(monitoring_email) == "monitoring"