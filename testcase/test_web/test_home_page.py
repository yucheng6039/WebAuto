import allure
import pytest

from pages.web_page.home_page import LogHome
from common.po_base import El
from common.po_base import Page
from pages.IndexPage import IndexPage
from common.page_manage import pm
from pages.LoginPage import LoginPage
from time import sleep
from selenium.webdriver.common.keys import Keys
import random
from selenium.webdriver import ActionChains
import pyautogui
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
    def test_home(self,browser):
        page = pm("LoginPage")(browser)
        page._clear_cache()
        page = LogHome(page)
        sleep(3)
        # with allure.step("step1:点击接受cookie"):
        #     page.key1.click()
        #     sleep(3)
        page.key1.send_keys("850197943@qq.com")
        sleep(1)
        page.key2.send_keys("123456789")
        sleep(1)
        page.key3.click()
        sleep(2)
        # for i in range(58,100):
        #     page.key4.click()
        #     page.key5.send_keys(i)
        #     sleep(1)
        #     pyautogui.click(x=400, y=652, button='left')
        #     sleep(1)
        #     pyautogui.click(x=506, y=286, button='left')
        #     sleep(5)
        #     pyautogui.click(x=97, y=296, button='left')
        #     sleep(1)
        #     pyautogui.click(x=290, y=154, button='left')
        #     sleep(1)
        #     pyautogui.click(x=1035, y=698, button='left')
        #     sleep(1)
        #     pyautogui.click(x=489, y=389, button='left')
        #     sleep(90)
        #     pyautogui.click(x=759, y=700, button='left')
        #     sleep(2)
        # #page.key5.send_keys(Keys.ENTER)
        # #ActionChains(page.driver).move_by_offset(400,652).perform()
        # #$ActionChains(page.driver).click(on_element=None).perform()
        # #ActionChains(page.driver).move_by_offset(400,652).click().perform()
        #
        # #page.key6.sendkeys("C:\\Users\\Yu Chengcheng\\Desktop\\Experiment_1108.zip")
        # sleep(5)
        #with allure.step("点击Fluorescent"):
            #try:
                #page.driver.find_element_by_css_selector("#source > div:nth-child(70000)")
                #ActionChains(page.driver).double_click(page.driver.find_element_by_css_selector("#source > div:nth-child(7)")).perform()
            #except:
                #assert 1==2,"未找到页面元素"
        #ActionChains(self.driver).drag_and_drop(page.key1, page.key1).perform()
        # sleep(5)
        # page.click_element("//*[contains(text(), 'Create Experiment')]")
        # sleep(5)
        # page.switch_to_new_window()
        # page.click_element("//*[text()='Next']")
        # page.click_element("//*[text()='Group']")
        # sleep(50)
        #page: IndexPage
        #page.click_element("//*[@id='accept-cookies-button']")
        #page = LogHome(sign_in)
        # page.click_element("//*[@title='Tube_002']")
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