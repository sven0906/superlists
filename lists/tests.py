from django.test import TestCase
# from django.core.urlresolvers import resolve ->
from django.urls import reverse
from lists.views import home_page


class SmokeTest(TestCase):

    # def test_bad_maths(self):
    #     self.assertEqual(1 + 1, 3)

    def test_root_url_resolves_to_home_page_view(self):
        found = reverse('/')
        self.assertEqual(found.func, home_page)