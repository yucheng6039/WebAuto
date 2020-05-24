#-------------------------------------------------------------------------------
# Name:         test_es_case
# Description:  
# Author:       slm
# Date:         2020/5/15
#-------------------------------------------------------------------------------

import allure
import pytest
from pages.IndexPage import IndexPage
from common.page_manage import pm
from pages.LoginPage import LoginPage
from time import sleep
from pages.sensor_page.CreateEsPage import CreateEsPage
@pytest.fixture(scope="module")
def sign_in(login_as):
    page=login_as("admin","admin123")
    page.click_platform("指标解析中心")
    yield page
@allure.feature("创建ES数据源")
class TestEsCase:

    def test_tt(self):
        a= 5
        assert a==5

    def test_login_success(self, sign_in):
        # page.screenshot_in_allure()

        print("打印添加数据源-----0---")
        # page: CreateEsPage
        page=CreateEsPage(sign_in)
        page.click_source()
        page.click_add()

        # CreateEsPage().click_source()
        sleep(5)









    # def test_creat(self,login_as):
    #     page = login_as("admin", "admin123")
    #     pass
    #     #
    #     # # page:   这里
    #     # page.click_platform("指标解析中心")
    #     # return CreateEsPage.click_source()
    #     pass

