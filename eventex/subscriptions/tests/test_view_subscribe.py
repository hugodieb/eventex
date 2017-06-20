from django.core import mail
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscribeGet(TestCase):
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
		tags = (('<form', 1),
				('<input', 6),
				('type="text"', 3),
				('type="email"', 1),
				('type="submit"', 1))

		for text, count in tags:
			with self.subTest():
				self.assertContains(self.response, text, count)

	def test_csrf(self):
		"""Html must contain csrf"""
		self.assertContains(self.response, 'csrfmiddlewaretoken')

	def test_has_form(self):
		"""Context must have subscription form"""
		form = self.response.context['form']
		self.assertIsInstance(form, SubscriptionForm)

class SubscribePostValid(TestCase):

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

class SubscribePostInavalid(TestCase):
	def setUp(self):
		self.response = self.client.post('/inscricao/', {})

	def test_post(self):
		"""Invalid POST should not redirect"""
		self.assertEqual(200, self.response.status_code)

	def test_template(self):
		"""Must use subscriptions/subscription_form.html"""
		self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')

	def test_has_form(self):
		form = self.response.context['form']
		"""Check context in form"""
		self.assertIsInstance(form, SubscriptionForm)

	def test_has_error(self):
		form = self.response.context['form']
		"""Check errors in form context"""
		self.assertTrue(form, SubscriptionForm)

class SubscribeSuccessMessage(TestCase):
	def test_message(self):
		data = dict(name='Hugo Dieb', cpf='12345678901',
				email='hugo@dieb.net', phone='12-98867-1232')

		response = self.client.post('/inscricao/', data, follow=True)
		self.assertContains(response, 'Inscrição realizada com sucesso')
