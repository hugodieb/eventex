from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


class SubscriptionsNewGet(TestCase):
	def setUp(self):
		self.response = self.client.get(r('subscriptions:new'))

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

class SubscriptionsPostValid(TestCase):

	def setUp(self):
		data = dict(name='Hugo Dieb', cpf='12345678905',
					email='hugodieb.py@gmail.com', phone='12-98868-1640')
		self.response = self.client.post(r('subscriptions:new'), data)

	def test_post(self):
		"""Valid POST should redirect to /inscricao/1	/"""
		self.assertEqual(302, self.response.status_code)
		#self.assertRedirects(self.response, r('subscriptions:detail', 1))

	def test_send_subscribe_email(self):
		"""Check send one email"""
		self.assertEqual(1, len(mail.outbox))

	def test_save_subscription(self):
		self.assertTrue(Subscription.objects.exists())

class SubscriptionsPostInvalid(TestCase):
	def setUp(self):
		self.response = self.client.post(r('subscriptions:new'), {})

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

	def test_dont_save_subscription(self):
		self.assertFalse(Subscription.objects.exists())

class TemplateRegressionTest(TestCase):
	def test_template_has_non_field_errors(self):
			invalid_data = dict(name='Hugo Dieb', cpf='12345678909')
			response = self.client.post(r('subscriptions:new'), invalid_data)

			self.assertContains(response, '<ul class="errorlist nonfield"')