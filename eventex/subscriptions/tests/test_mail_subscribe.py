from django.core import mail
from django.shortcuts import resolve_url as r
from django.test import TestCase

class SubscribePostValid(TestCase):

    def setUp(self):
        data = dict(name='Hugo Dieb', cpf='12345678905',
                    email='hugodieb.py@gmail.com', phone='12-98868-1640')
        self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        """Check description subject email"""
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):

       expect = 'contato@eventex.com.br'
       """Check description from email"""
       self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):

        expect = ['contato@eventex.com.br', 'hugodieb.py@gmail.com']
        """Check description email to"""
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):

        """Check completed form fields"""
        contents = ['Hugo Dieb',
                    '12345678905',
                    'hugodieb.py@gmail.com',
                    '12-98868-1640']

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)