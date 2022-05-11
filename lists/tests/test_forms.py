from django.test import TestCase
from lists.forms import ItemForm, EMPTY_LIST_ERROR


class ItemFormTest(TestCase):

    def test_form_renders_item_text_input(self):
        form = ItemForm()
        self.assertIn('placeholder="작업 아이템 입력"', form.as_p())
        self.assertIn('class="form-control input-lg"', form.as_p())
        self.fail(form.as_p())  # 폼을 HTML으로 렌더링

    # 폼 유효성 검증(공백)
    def test_form_validation_for_blank_items(self):
        form = ItemForm(data={'text': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'], [EMPTY_LIST_ERROR])
        form.save()