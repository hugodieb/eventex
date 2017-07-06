from unittest.mock import Mock

from django.test import TestCase
from eventex.subscriptions.admin import SubscriptionModelAdmin, Subscription, admin

class SubscriptionModelAdminTest(TestCase):

    def setUp(self):
        Subscription.objects.create(name='Hugo Dieb', cpf='12345678909',
                                    email='hugodieb@mailinator.com', phone='12-12340987')
        self.model_admin = SubscriptionModelAdmin(Subscription, admin.site)

    def test_has_action(self):
        """Action mark_as_paid shoud be instalad"""
        model_admin = SubscriptionModelAdmin(Subscription, admin.site)
        self.assertIn('mark_as_paid', self.model_admin.actions)


    def test_mark_all(self):
        """It should mark all selected subscription as paid"""
        self.call_actions()

        self.assertEqual(1, Subscription.objects.filter(paid=True).count())

    def test_message(self):
        """It should send message to the user"""
        mock = self.call_actions()
        mock.assert_called_once_with(None, '1 inscrição foi marcada como paga.')



    def call_actions(self):
        queryset = Subscription.objects.all()
        mock = Mock()
        old_message_user = SubscriptionModelAdmin.message_user
        SubscriptionModelAdmin.message_user = mock
        self.model_admin.mark_as_paid(None, queryset)
        SubscriptionModelAdmin.message_user = old_message_user

        return mock
