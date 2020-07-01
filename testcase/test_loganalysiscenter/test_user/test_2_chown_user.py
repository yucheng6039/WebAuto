import allure
import pytest
from pages.loganalysiscenter_page.chown_user import LogHome
from common.po_base import El
from common.po_base import Page
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
@allure.feature("aix文件采集")
class TestLogHome(object):
    @allure.title("创建aix文件采集任务")

    @allure.step("这是一个aix文件采集步骤")
    def test_home(self,sign_in):
        page = LogHome(sign_in)
        page.click_sidebar_element("系统设置")
        page.click_element("//a[text()='用户管理']")
        page.switch_to_frame()
        page.click_element("//tr[@class='el-table__row'][1]/td[4]/div/span")
        page.click_css_element("#el-popover-2 .el-select__caret")
        page.click_element("/html/body/div[3]/div[1]/div/ul/li[1]/span")
        sleep(1)
        page.click_element("//*[@id='el-popover-2']/div[2]/button[2]")
        sleep(3)
