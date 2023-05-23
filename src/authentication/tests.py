from rest_framework.test import APIRequestFactory

from django.test import TestCase


from .models import User

from . import views


class AuthTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(
            username="test", 
            password="test", 
            email="test@example.com")
        user.save()

    def test_user_create(self):
        factory = APIRequestFactory()

        request = factory.post("/api/auth/register/", {
            "username": "sample",
            "password": "sample",
            "email": "sample@example.com",
            "first_name": "sample",
            "last_name": "sample",
        })

        view = views.RegisterView.as_view()
        response = view(request)
        response.render()

        self.assertEqual(response.status_code, 200)
