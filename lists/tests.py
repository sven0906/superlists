import re
from django.http import HttpRequest
from django.test import TestCase
from django.shortcuts import render
# from django.core.urlresolvers import resolve ->
from django.urls import reverse
from django.template.loader import render_to_string
from lists.views import home_page


class SmokeTest(TestCase):

    # def test_bad_maths(self):
    #     self.assertEqual(1 + 1, 3)

    def remove_csrf(self, origin):
        csrf_regex = r'<input[^>]+csrfmiddlewaretoken[^>]+>'
        return re.sub(csrf_regex, '', origin)

    # def test_root_url_resolves_to_home_page_view(self):
    #     found = reverse('/')
    #     self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()  # HttpRequest 객체를 생성한다.

        response = home_page(request)  # home_page 뷰에 전달해서 응답을 가져온다.
        # self.assertTrue(response.content.startswith(b'<html>'))
        # self.assertIn(b'<title>To-Do lists</title>', response.content)
        # self.assertTrue(response.content.endswith(b'</html>'))
        expected_html = self.remove_csrf(render_to_string('home.html', request=request))
        response_decode = self.remove_csrf(response.content.decode())
        self.assertEqual(response_decode, expected_html)

    def test_home_page_can_save_a_post_request(self):
        """ 설정(Setup) """
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = '신규 작업 아이템'

        """ 처리(Exercise) """
        response = home_page(request)

        """ 어설션(Assert) """
        self.assertIn('신규 작업 아이템', response.content.decode())
        expected_html = self.remove_csrf(render_to_string(
            'home.html',
            {'new_item_text': '신규 작업 아이템'},
            request=request
        ))
        response_decode = self.remove_csrf(response.content.decode())
        self.assertEqual(response_decode, expected_html)
