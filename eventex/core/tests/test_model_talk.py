from django.test import TestCase
from eventex.core.models import Talk

class TalkModelTest(TestCase):
    def setUp(self):
        self.talk = Talk.objects.create(
            title = 'Título da palestra',
            start = '10:00',
            description = 'Descrição da palestra'
        )

    def test_create(self):
        self.assertTrue(Talk.objects.exists())

    def test_has_speakers(self):
        """Talks has many Speakers and vice-verse"""
        self.talk.speakers.create(
            name='Hugo Dieb',
            slug='hugo-dieb',
            website='hugo@dieb.net'
        )
        self.assertEqual(1, self.talk.speakers.count())