from pages.IndexPage import IndexPage

import pytest
class TestLogin:

    def test_login(self, login_as):
        page = login_as("admin", "admin123")
        page: IndexPage
        assert "夏洛克AIOps运营平台" in page.title


if __name__ =="__main__":
    pytest.main["-s","../demo.py"]

