import allure
from pages.web_page.add_fluo import LogHome
from common.page_manage import pm
from selenium.webdriver.support.select import Select
from time import sleep
import pyautogui
from selenium.webdriver.common.keys import Keys
import xlrd
import random

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
        sleep(3)
        page.key7.click()
        sleep(3)
        with allure.step("step3:点击下一步"):
            page.key5.click()
            sleep(3)
        text= random.sample("adfghhjjiuiytrew123qwertyuio",10)
        sleep(1)
        pyautogui.click(700,280)
        pyautogui.typewrite(text)
        sleep(3)
        with allure.step("step3:点击下一步"):
            page.key6.click()
        # id定位方式获取整个表格对象
        sleep(5)
        page.driver.find_element_by_xpath("//*[contains (text(),'Add Marker')]").click()
        sleep(1)
        tdlist = page.driver.find_elements_by_xpath("//*[@role='combobox']")
        tdlist[0].click()
        sleep(3)
        tdlist[0].send_keys(Keys.CONTROL + "a")
        sleep(3)
        tdlist[0].send_keys("CD10")
        sleep(1)
        page.driver.find_element_by_xpath("//*[text()='Select Fluorescent Tags']").click()
        wb = xlrd.open_workbook('D:\\auto_test\\test_fluo.xls')


        # 按工作簿定位工作表
        sh = wb.sheet_by_name('Sheet1')
        for i in range(sh.nrows):
            file = open(r'D:\\auto_test\\test1.txt', mode='a', encoding='utf - 8')
            page.driver.find_elements_by_xpath("//*[@role='combobox']")[0].send_keys(Keys.CONTROL + "a")
            sleep(3)
            page.driver.find_elements_by_xpath("//*[@role='combobox']")[0].send_keys(sh.row_values(i)[0])
            sleep(3)
            pyautogui.click(539,442)
            sleep(3)
            assert page.driver.find_element_by_xpath("/html/body/app-root/div/div/app-panel/div[1]/mat-tab-group/div/mat-tab-body[4]/div/div/div[1]/table/tbody/tr/td[2]/div/mat-form-field/div/div[1]/div/input").get_attribute("value") ==""
            sleep(2)
            file.write(str(i + 1) + '\n')
            file.close()

            sleep(3)
