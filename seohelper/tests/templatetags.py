from django.test import TestCase
from seohelper.models import Document
from seohelper.templatetags.seo_helper import SeoHelperNode


class SeohelperTemplatetagsTests(TestCase):
    fixtures = ['seohelper_testdata.json', ]

    def test_seo_helper(self):
        """
        Should bring a document from database with url as parameter.
        """
        url = '/'
        document = Document.objects.get(url=url)

        # Successful parse
        context = {'url': url + '?q=1'}
        node = SeoHelperNode('url', 'meta')
        node.render(context)
        self.assertEquals(context['meta'], document)
