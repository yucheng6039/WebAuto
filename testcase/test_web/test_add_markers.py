import allure
from pages.web_page.home_page import LogHome
from common.page_manage import pm
from time import sleep
import pyautogui


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
        sleep(50)
        pyautogui.click(x=746, y=352, button='left')
        with allure.step("step2:点击create panel按钮"):
            page.key4.click()
        with allure.step("step3:点击下一步"):
            page.key5.click()
            sleep(5)
        with allure.step("step3:点击下一步"):
            page.key6.click()
        # id定位方式获取整个表格对象
        #table = page.find_element_by_id("/html/body/app-root/div/div/app-panel/div[1]/mat-tab-group/div/mat-tab-body[3]/div/div/div[2]/table")
        # 通过标签名获取表格中所有行
        trlist = page.find_elements_by_tag_name("tr")
        print(len(trlist))
        for row in trlist:
            #遍历行对象，获取每一个行中所有的列对象
            tdlist = row.find_elements_by_tag_name("td")
            for col in tdlist:
                print(col.text +"\t",end="\'\'")
                print("\'n\'")