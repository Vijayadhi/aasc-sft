# tests.py

from django.test import TestCase
from django.core import mail
from django.urls import reverse
from .models import CustomUser

class EmailSendingTestCase(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser',
            email='venerablevignesh@gmail.com',
            password='password'
        )

    def test_send_password_reset_email(self):
        """
        Test sending a password reset email.
        """
        response = self.client.post(reverse('password_reset'), {
            'email': self.user.email
        }, follow=True)  # Follow redirects

        # Check that the response status code is 200 OK
        self.assertEqual(response.status_code, 200)

        # Check that one email was sent
        self.assertEqual(len(mail.outbox), 1)

        # Get the email message
        email = mail.outbox[0]

        # Verify the email subject
        self.assertEqual(email.subject, 'Password reset on testserver')

        # Verify the email body contains the password reset link
        self.assertIn('http://testserver/reset/', email.body)

        # Verify the email recipient
        self.assertEqual(email.to, [self.user.email])
