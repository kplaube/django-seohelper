from django.test import TestCase

from seohelper.models import Document


class DocumentModelTests(TestCase):
    fixtures = ['seohelper_testdata.json', ]

    def test_repr(self):
        """
        Ensures it's casting to string.
        """
        document = Document.objects.get(pk=1)
        self.assertEquals(str(document), 'Home page')
