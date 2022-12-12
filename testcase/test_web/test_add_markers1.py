import allure
from pages.web_page.add_markers import LogHome
from common.page_manage import pm
from time import sleep
import pyautogui
from selenium.webdriver.common.keys import Keys
@allure.feature("创建predesigned panel")
class TestLogHome(object):
    @allure.title("登录并点击创建panel")
    def test_home(self,browser):
        page = pm("LoginPage")(browser)
        page._clear_cache()
        page = LogHome(page)
        sleep(3)
        with allure.step("step1:输入账号，密码，点击登录"):
            page.key1.send_keys("850197943@qq.com")
            sleep(1)
            page.key2.send_keys("123456")
            page.key3.click()
        sleep(30)
        pyautogui.click(x=746, y=352, button='left')
        with allure.step("step2:点击create panel按钮"):
            page.key4.click()
        sleep(5)
        page.key7.click()
        sleep(3)
        with allure.step("step3:点击下一步"):
            page.key5.click()
            sleep(5)
        page.key8.send_keys("abc90")
        with allure.step("step3:点击下一步"):
            page.key6.click()
        # id定位方式获取整个表格对象
        sleep(5)
        page.key10.click()
        sleep(1)
        page.key10.click()
        sleep(1)
        page.key10.click()
        sleep(5)
        #table = page.find_element_by_id("/html/body/app-root/div/div/app-panel/div[1]/mat-tab-group/div/mat-tab-body[3]/div/div/div[2]/table")
        # 通过标签名获取表格中所有行
        #trlist = page.driver.find_elements_by_xpath("//tr[@class='mat-row cdk-row ng-star-inserted']")
        #print(len(trlist))
        #for row in trlist:
            #遍历行对象，获取每一个行中所有的列对象
        #tdlist = page.driver.find_elements_by_xpath("//td[@role='cell']")
        tdlist = page.driver.find_elements_by_xpath("//*[@role='combobox']")
        i=0
        for col in tdlist:

            sleep(1)
            if(i==0):
                col.send_keys("CD1")
                sleep(1)
                i+=1
            elif (i==1):
                col.click()
                col.send_keys(Keys.TAB)
                col.send_keys(Keys.TAB)
                col.send_keys(Keys.TAB)
                i=0




        sleep(1)