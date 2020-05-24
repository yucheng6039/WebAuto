import allure
import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

from common.page_manage import pm
from common.po_base import Page
from config import Driver_Path

page = None

""" 
此方法是每次都清除浏览器缓存的
@pytest.fixture(scope="session")
def login_as(browser):
    def _login_as(a,p):
        with allure.step("登陆"):
            _page = pm("LoginPage")(browser)
            _page._clear_cache()
            return _page.login(a,p)
    return _login_as
"""

@pytest.fixture(scope="session")
def login_as(browser):
    def _login_as(a,p):
        with allure.step("登陆"):
            _page = pm("LoginPage")(browser)
            _page._clear_cache()
            return _page.login(a,p)
    return _login_as


@pytest.fixture(scope='session')
def browser():
    global page
    if page is None:
        options = Options()
        # options.add_argument('--headless')
        options.add_argument('--start-maximized')
        options.add_argument('--ignore-certificate-errors')  # 忽略https报错
        options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
        options.add_experimental_option("excludeSwitches", ['enable-automation'])
        with Chrome(Driver_Path, options=options) as browser:
            page = Page(browser)
            yield page


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    hook函数失败用例截图添加
    @param item:
    @param call:
    @return:
    """
    global page
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    # we only look at actual failing test calls, not setup/teardown
    if rep.failed:
        # 失败时进行错误截图添加
        if page is not None:
            page.screenshot_in_allure("错误截图")
