# from django.core.urlresolvers import resolve
from django.test import TestCase
from blog.views import blog_index
from django.urls import resolve

# Create your tests here.
class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/blog/')
        self.assertEqual(found.func, index)