import allure
import pytest
from pages.loganalysiscenter_page.create_user import LogHome
from common.po_base import El
from common.po_base import Page
from pages.IndexPage import IndexPage
from common.page_manage import pm
from pages.LoginPage import LoginPage
from time import sleep
from selenium.webdriver import ActionChains
from pages.sensor_page.CreateEsPage import CreateEsPage
from common.page_action import PageAction
from selenium.webdriver.remote.webdriver import WebDriver

# @pytest.fixture(scope="module")
# def sign_in(login_as):
#     page=login_as("EOIadmin","admin123")
#     #page.click_platform("日志精析中心")
#     yield page
@allure.feature("首页测试")
class TestLogHome(object):

    @allure.title("首页测试")
    @allure.step("清除缓存并打开主页")
    def test_home(self,browser):
        page = pm("LoginPage")(browser)
        page._clear_cache()
        page = LogHome(page)
        sleep(3)
        page.key1.click()
        sleep(3)
        ActionChains(page.driver).double_click(page.driver.find_element_by_css_selector("#source > div:nth-child(7)")).perform()
        #ActionChains(self.driver).drag_and_drop(page.key1, page.key1).perform()
        sleep(5)
        #page: IndexPage
        #page.click_element("//*[@id='accept-cookies-button']")
        #page = LogHome(sign_in)
        # page.click_element("//button[text()='创建']")
        # name = page.random_str()
        # page.key1.send_keys(name)
        # page.key2.send_keys("yu123456")
        # page.key3.send_keys("yu123456")
        # #page.click_element("//ul[@class='product-box']/li[2]/label/span[@class='el-checkbox__input']")
        # page.click_element("//ul[@class='product-box']/li[9]/label/span[@class='el-checkbox__input']")
        # page.key4.send_keys("yucc")
        # page.click_element("//button[text()='确定']")
        # sleep(2)
        # f = open('/Users/yucc/Desktop/itoauser.txt', 'a')
        # f.write(name+",3A5DF20B164E15AF29F9A15C844F5D2C\r\n")
        # f.close()