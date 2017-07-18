from django.core.exceptions import ValidationError
from django.test import TestCase
from eventex.core.models import Speaker, Contact

class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Hugo Dieb',
            slug='hugo-dieb',
            photo='http://hd.link/hd-pic'
        )

    def test_email(self):
        contact = Contact.objects.create(speaker=self.speaker,
                                         Kind=Contact.EMAIL,
                                         value='hugo@dieb.net'
                                         )
        self.assertTrue(Contact.objects.exists())

    def test_phone(self):
        contact = Contact.objects.create(speaker=self.speaker,
                                         Kind=Contact.PHONE,
                                         value='12-98890978'
                                         )
        self.assertTrue(Contact.objects.exists())

    def test_choices(self):
        """Contact Kind should be limited E or P"""
        contact = Contact(speaker=self.speaker, Kind='A', value='b')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact(speaker=self.speaker,
                          Kind=Contact.EMAIL,
                          value='hugo@dieb.net'
                          )
        self.assertEqual('hugo@dieb.net', str(contact))