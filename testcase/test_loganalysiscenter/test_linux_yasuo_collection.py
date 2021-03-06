import allure
import pytest
from pages.loganalysiscenter_page.linux_yasuo_collection import LogHome
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
@allure.feature("linux文件采集")
class TestLogHome(object):
    @allure.title("创建linux文件采集任务")

    @allure.step("这是一个linux文件采集步骤")
    def test_home(self,sign_in):
        page = LogHome(sign_in)
        page.click_sidebar_element('全局')
        page.click_sidebar_element("数据接入")
        page.switch_to_frame()
        page.click_element("//a[text()='数据接入']")
        page.click_element("//button[text()=' 创建']")
        #page.click_element()
        page.click_element("//li[text()='文件和目录']")
        name = page.random_str()
        page.key1.send_keys(name)
        page.click_element("//a[text()='高级配置 ']")
        page.click_element("//span[text()=' Windows ']")
        page.click_element("//span[text()=' AIX ']")
        page.click_element("//span[text()=' Linux ']")
        page.key2.send_keys('192.168.31.189')
        page.click_element("//span[text()='归档文件']")
        page.click_element("//tbody/tr[1]/td[1]/div/label/span/span")
        page.key3.send_keys("/root/wmk/yasuo")
        page.click_element("//button[text()='添加采集']")
        page.click_element("//button[text()='保存']")
        sleep(3)
        assert page.return_name(name) != '',"任务不存在"
        sleep(3)