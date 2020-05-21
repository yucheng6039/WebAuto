from pages.IndexPage import IndexPage


class TestLogin:

    def test_login(self, login_as):
        page = login_as("admin", "admin123")
        page: IndexPage

        assert "夏洛克" in page.title
