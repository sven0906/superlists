from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 사용자A가 웹 사이트에 접속한다.
        self.browser.get(url='http://localhost:8000')

        # 웹 페이지 타이틀과 헤더가 'To-Do'를 표시하고 있다.
        # assert 'To-do' in browser.title, "Brower title was " + browser.title
        # self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the Test!')

        # 사용자A는 바로 작업을 추가한다.
        # "공작깃털 사기"라고 텍스트 상자에 입력한다.

        # 엔터키를 치면 페이지가 갱신되고 작업목록에
        # "1: 공작깃털 사기" 아이템이 추가된다.

        # 추가 아이템을 입력할 수 있는 여분의 텍스트 상자가 존재한다.
        # 다시 "공작깃털을 이용해서 그물 만들기"라고 입력한다.

        # 페이지는 다시 갱신되고, 두개 아이템이 목록에 보인다.
        # 사용자A는 사이트가 입력한 목록을 저장하고 있는지 궁금하다
        # 사이트는 사용자A를 위해 특정 URL을 생성해준다
        # 이때 URL에 대한 설명도 함께 제공된다.

        # 해당 URL 에 접속하면 작업 목록이 그대로 있는 것을 확인할 수 있다.

        # browser.quit()


if __name__ == '__main__':
    unittest.main(warnings='ignore')
