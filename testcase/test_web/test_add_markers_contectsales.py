import allure
from pages.web_page.add_markers1 import LogHome
from common.page_manage import pm
from selenium.webdriver.support.select import Select
from time import sleep
import pyautogui
from selenium.webdriver.common.keys import Keys
import xlrd
import random

from selenium.webdriver.common.action_chains import ActionChains

@allure.feature("创建predesigned panel")
class TestLogHome(object):
    @allure.title("登录并点击创建panel")
    def test_home(self,browser):
        page = pm("LoginPage")(browser)
        page._clear_cache()
        page = LogHome(page)
        sleep(2)
        with allure.step("step1:输入账号，密码，点击登录"):
            page.key1.send_keys("ccyu@cytekbio.com.cn")
            sleep(1)
            page.key2.send_keys("123456123456")
            page.key3.click()
        sleep(10)
        pyautogui.click(x=746, y=352, button='left')
        with allure.step("step2:点击create panel按钮"):
            page.key4.click()
        sleep(2)
        page.key7.click()
        sleep(2)
        with allure.step("step3:点击下一步"):
            page.key5.click()
            sleep(2)
        page.key8.send_keys(random.sample("adfghhjjiuiytrew123qwertyuioplknmbbcxcxz",10))
        sleep(2)
        with allure.step("step3:点击下一步"):
            page.key6.click()
        # id定位方式获取整个表格对象
        sleep(5)
        wb = xlrd.open_workbook('D:\\auto_test\\test1.xls')

        # 按工作簿定位工作表
        sh = wb.sheet_by_name('Sheet1')
        for i in range(sh.nrows):
            file = open(r'D:\\auto_test\\test1.txt', mode='a', encoding='utf - 8')
            page.driver.find_element_by_xpath("//*[contains (text(),'Add Marker')]").click()
            sleep(2)
            tdlist = page.driver.find_elements_by_xpath("//*[@role='combobox']")
            if(sh.row_values(i)[3]==''):
                tdlist[0].click()
                sleep(2)
                tdlist[0].send_keys(Keys.CONTROL + "a")
                sleep(2)
                tdlist[0].send_keys(sh.row_values(i)[0])
            else:
                tdlist[0].click()
                sleep(2)
                tdlist[0].send_keys(Keys.CONTROL + "a")
                sleep(2)
                tdlist[0].send_keys(sh.row_values(i)[3])
            sleep(2)
            tdlist[1].click()
            sleep(2)
            if(sh.row_values(i)[1]=="Mouse" or sh.row_values(i)[1]=="Human/Mouse"):
                test= page.driver.find_element_by_xpath("//*[text()='All']/..").get_attribute("id")
                test=test[:-1]
                page.driver.find_element_by_xpath("//*[@id='"+test+"1']").click()
                sleep(1)

                #pyautogui.click(540,440)
            elif(sh.row_values(i)[1]=="Human"):
                #pyautogui.click(540, 399)
                test = page.driver.find_element_by_xpath("//*[text()='All']/..").get_attribute("id")
                test = test[:-1]
                page.driver.find_element_by_xpath("//*[@id='" + test + "0']").click()
                sleep(1)

            page.driver.find_element_by_xpath("//*[@id='CloneInput-0']").click()
            sleep(3)
            pyautogui.hotkey('ctrl','a')
            sleep(2)
            if(type(sh.row_values(i)[2])==float):
                if((sh.row_values(i)[2]-int(sh.row_values(i)[2]))>0):
                    pyautogui.typewrite(str(sh.row_values(i)[2]))
                else:
                    pyautogui.typewrite(str(int(sh.row_values(i)[2])))
            else:
                pyautogui.typewrite(sh.row_values(i)[2])
            sleep(2)
            page.driver.find_element_by_xpath("//*[text()='Select Fluorescent Tags']").click()
            sleep(2)
            page.driver.find_elements_by_xpath("//*[@role='combobox']")[0].send_keys(Keys.CONTROL + "a")
            sleep(2)
            page.driver.find_elements_by_xpath("//*[@role='combobox']")[0].send_keys(sh.row_values(i)[6])
            sleep(2)
            page.key6.click()
            #page.driver.find_element_by_xpath("//*[text()='Review Panel']").click()
            sleep(3)
            assert page.driver.find_elements_by_xpath("//*[@type ='text']")[1].get_attribute("value") ==sh.row_values(i)[5]

            page.driver.find_element_by_xpath("//*[@class ='ng-select-container ng-has-value']").click()
            sleep(2)
            #page.driver.execute_script("arguments[0].click;",page.driver.find_elements_by_xpath("//*[text()=' 25 Tests']/..")[0])
            page.driver.find_elements_by_xpath("//*[text()=' "+sh.row_values(i)[7]+"']/..")[0].click()
            sleep(2)
            if(sh.row_values(i)[4][-1]=='\xa0'):
                assert page.driver.find_elements_by_xpath("//*[@type ='text']")[3].get_attribute("value") == sh.row_values(i)[4][:-1]
            else:
                assert page.driver.find_elements_by_xpath("//*[@type ='text']")[3].get_attribute("value") == sh.row_values(i)[4]
            sleep(2)
            file.write(str(i+1)  + '\n')
            file.close()
            page.driver.find_element_by_xpath("//*[text()='Select Markers']").click()
            sleep(2)

        # for col in tdlist:
        #
        #     sleep(1)
        #     if(i==0):
        #         col.send_keys("CD1")
        #         sleep(1)
        #         i+=1
        #     elif (i==1):
        #         col.click()
        #         col.send_keys(Keys.TAB)
        #         col.send_keys(Keys.TAB)
        #         col.send_keys(Keys.TAB)
        #         i=0
            # //*[text()='Human' and @class=ng-option ng-option-selected ng-star-inserted]
