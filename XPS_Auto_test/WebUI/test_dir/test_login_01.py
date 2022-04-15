import seldom
from seldom.Bean_seldom.SeldomConfig import SeldomConfig
from XPS_Auto_test.pages.IndexPage import IndexPage


class Login_test(seldom.TestCase):
    """XPS login test case"""

    def test_case_01(self):
        """a simple test case """

        page = IndexPage(SeldomConfig.driver)
        page.open("http://191.168.0.151/")
        page.account = "admin"
        page.password = "123456"
        page.login_but.click()
        self.assertTrue(page.index_logout.is_displayed())


if __name__ == '__main__':
    seldom.main(debug=True)
