from .base import FunctionalTest
from unittest import skip

class LayoutAndStylingTest(FunctionalTest):
    @skip
    def test_layout_and_styling(self):
        # 에디스는 메인 페이지를 방문한다.
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 748)

        # 그녀는 입력 상자가 가운데 배치된 것을 본다
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )

