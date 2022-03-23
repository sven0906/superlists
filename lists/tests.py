import re
from django.http import HttpRequest
from django.test import TestCase
from django.shortcuts import render
# from django.core.urlresolvers import resolve ->
from django.urls import reverse
from django.template.loader import render_to_string
from lists.views import home_page
from lists.models import Item


class HomePageTest(TestCase):

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
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, '신규 작업 아이템')

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

        # 더 이상 response.content가 템플릿에 의해 렌더링 되지 않음
        # self.assertIn('신규 작업 아이템', response.content.decode())
        # expected_html = self.remove_csrf(render_to_string(
        #     'home.html',
        #     {'new_item_text': '신규 작업 아이템'},
        #     request=request
        # ))
        # response_decode = self.remove_csrf(response.content.decode())
        # self.assertEqual(response_decode, expected_html)

    def test_home_page_only_saves_items_when_necessary(self):
        request = HttpRequest()
        home_page(request)
        self.assertEqual(Item.objects.count(), 0)


class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = '첫 번째 아이템'
        first_item.save()

        second_item = Item()
        second_item.text = '두 번째 아이템'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, '첫 번째 아이템')
        self.assertEqual(second_saved_item.text, '두 번째 아이템')
