from django.test import TestCase

from .models import MicroPage


class MicroPageTestCase(TestCase):
    def test_str(self):
        micro = MicroPage(title="This is a Micro Page")
        self.assertEqual("This is a Micro Page", str(micro))
