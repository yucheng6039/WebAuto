# Name:         test_log_home
# Description:  
# Author:       slm
# Date:         2020/5/22
import allure
import pytest
from pages.loganalysiscenter_page.LogHome import LogHome
from common.po_base import El
from common.po_base import Page
from pages.IndexPage import IndexPage
from common.page_manage import pm
from pages.LoginPage import LoginPage
from time import sleep
from pages.sensor_page.CreateEsPage import CreateEsPage
@pytest.fixture(scope="module")
def sign_in(login_as):
    page=login_as("yuchengcheng5","yu123456")
    page.click_platform("日志精析中心")
    yield page
@allure.feature("操作侧边栏")
class TestLogHome(object):
    @allure.title("这是测试日志首页的功能")
    @allure.link("https://zentao.eoitek.net/index.php?m=testcase&f=view&caseID=14525&version=1")
    def test_home(self,sign_in):
        page = LogHome(sign_in)
        page.click_sidebar_element('全局')
        page.click_sidebar_element("数据接入")
        page.switch_to_frame()
        page.click_element("//a[text()='数据接入']")
        page.click_element("//button[text()=' 创建']")
        page.click_element("//li[text()='关系型数据库']")
        page.key1.send_keys("192.168.31.187")

        page.click_element("//input[@placeholder='请输入任务名称']")
        page.click_element("//input[@placeholder='输入主机名/IP']")
        #page.click_element("//input[@placeholder='输入端口']").sendkeys()

        sleep(5)


if __name__ =="__main__":
    pytest.main("testcase/test_loganalysiscenter/test_log_home.py","-s")