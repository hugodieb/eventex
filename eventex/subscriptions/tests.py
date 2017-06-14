from django.core import mail
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscribeTest(TestCase):
	def setUp(self):		
		self.response = self.client.get('/inscricao/')
		
	def test_get(self):
		"""GET /inscricao/ must return status_code 200"""
		self.assertEqual(200, self.response.status_code)
	
	def test_template(self):
		"""Must use subscriptions/subscription_form.html"""
		self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')

	def test_html(self):
		"""Html must contain input tags"""
		self.assertContains(self.response, '<form')
		self.assertContains(self.response, '<input', 6)
		self.assertContains(self.response, 'type="text"', 3)
		self.assertContains(self.response, 'type="email"')
		self.assertContains(self.response, 'type="submit"')

	def test_csrf(self):
		"""Html must contain csrf"""
		self.assertContains(self.response, 'csrfmiddlewaretoken')

	def test_has_form(self):
		"""Context must have subscription form"""
		form = self.response.context['form']
		self.assertIsInstance(form, SubscriptionForm)

	def test_form_has_fields(self):
		"""Form must have 4 fields"""
		form = self.response.context['form']
		self.assertSequenceEqual(['name', 'cpf', 'email', 'phone'], list(form.fields))

class SubscribePostTest(TestCase):

	def setUp(self):
		data = dict(name='Hugo Dieb', cpf='12345678905',
					email='hugodieb.py@gmail.com', phone='12-98868-1640')
		self.response = self.client.post('/inscricao/', data)

	def test_post(self):
		"""Valid POST should redirect to /inscricao/"""
		self.assertEqual(302, self.response.status_code)

	def test_send_subscribe_email(self):
		"""Check send one email"""
		self.assertEqual(1, len(mail.outbox))

	def test_subscription_email_subject(self):
		email = mail.outbox[0]
		expect = 'Confirmação de inscrição'
		"""Check description subject email"""
		self.assertEqual(expect, email.subject)

	def test_subscription_email_from(self):
		email = mail.outbox[0]
		expect = 'contato@eventex.com.br'
		"""Check description from email"""
		self.assertEqual(expect, email.from_email)

	def test_subscription_email_to(self):
		email = mail.outbox[0]
		expect = ['contato@eventex.com.br', 'hugodieb.py@gmail.com']
		"""Check description email to"""
		self.assertEqual(expect, email.to)

	def test_subscription_email_body(self):
		email = mail.outbox[0]
		"""Check completed form fields"""
		self.assertIn('Hugo Dieb', email.body)
		self.assertIn('12345678905', email.body)
		self.assertIn('hugodieb.py@gmail.com', email.body)
		self.assertIn('12-98868-1640', email.body)


