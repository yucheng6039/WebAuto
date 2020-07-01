import allure
import pytest
from pages.loganalysiscenter_page.create_user import LogHome
from common.po_base import El
from common.po_base import Page
from pages.IndexPage import IndexPage
from common.page_manage import pm
from pages.LoginPage import LoginPage
from time import sleep
from pages.sensor_page.CreateEsPage import CreateEsPage
@pytest.fixture(scope="module")
def sign_in(login_as):
    page=login_as("EOIadmin","admin123")
    #page.click_platform("日志精析中心")
    yield page
@allure.feature("aix文件采集")
class TestLogHome(object):
    @allure.title("创建aix文件采集任务")

    @allure.step("这是一个aix文件采集步骤")
    def test_home(self,sign_in):
        page = LogHome(sign_in)
        page.click_element("//button[text()='创建']")
        name = page.random_str()
        page.key1.send_keys(name)
        page.key2.send_keys("yu123456")
        page.key3.send_keys("yu123456")
        page.click_element("//ul[@class='product-box']/li[2]/label/span[@class='el-checkbox__input']")
        page.key4.send_keys("yucc")
        page.click_element("//button[text()='确定']")
        sleep(2)
        f = open('/Users/yucc/Desktop/itoauser.txt', 'a')
        f.write(name+",3A5DF20B164E15AF29F9A15C844F5D2C\r\n")
        f.close()