import pytest
from django.contrib import admin
from django.contrib.auth.models import User


def test_every_model_is_registered_in_admin():
    assert admin.site.is_registered(User)


@pytest.mark.django_db
def test_database_roundtrip():
    User.objects.create_user(username='alice', password='not-a-real-password')
    assert User.objects.filter(username='alice').exists()
