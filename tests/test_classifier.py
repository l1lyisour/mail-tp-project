import pytest
from system.classifier import Classifier
from system.mail import Email

def test_urgent_security_email(urgent_email,classifier):
    email = make_email(urgent_email)
