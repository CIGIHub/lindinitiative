from django.test import TestCase

from .models import Design


class DesignTestCase(TestCase):
    def test_str(self):
        design = Design(name="My Awesome Design")
        self.assertEqual("My Awesome Design", str(design))
