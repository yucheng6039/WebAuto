# Name:         test_log_home
# Description:  
# Author:       slm
# Date:         2020/5/22
import allure
import pytest
from pages.oganalysiscenter_page.LogHome import LogHome
from pages.IndexPage import IndexPage
from common.page_manage import pm
from pages.LoginPage import LoginPage
from time import sleep
from pages.sensor_page.CreateEsPage import CreateEsPage
@pytest.fixture(scope="module")
def sign_in(login_as):
    page=login_as("admin","admin123")
    page.click_platform("日志精析中心")
    yield page
@allure.feature("操作侧边栏")
class TestLogHome(object):
    @allure.title("这是测试日志首页的功能")
    @allure.link("https://zentao.eoitek.net/index.php?m=testcase&f=view&caseID=14525&version=1")
    def test_home(self,sign_in):
        page = LogHome(sign_in)
        page.sidebar_element.click() # 点击首页
        page.el_find_element().click()
        # page.click_sidebar_element("业务墙")
        # page.click_sidebar_element("Eoi")
        # with allure.step("点击超级用户"):
        #     page.click_sidebar_element("test超级用户")
        # with allure.step("点击数据接入"):
        #     page.click_sidebar_element("数据接入")
        page.screenshot_in_allure()
        assert page.sidebar_text("首页") == "首页"


    def test_case(self,sign_in):
        page = LogHome(sign_in)
        page.click_sidebar_element("业务墙")
        page.click_sidebar_element("Eoi")



if __name__ =="__main__":
    pytest.main("testcase/test_oganalysiscenter/test_log_home.py","-s")