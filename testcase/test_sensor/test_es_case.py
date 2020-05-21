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
def to_ec(login_as):
    page=login_as("admin","admin123")
    page.click_platform("指标解析中心")
    yield page
@allure.feature("创建ES数据源")
class TestEsCase:

    def test_tt(self):
        a= 5
        assert a==5

    def test_login_success(self, to_ec):
        # page = login_as("admin", "admin123")
        # page: IndexPage
        # page.click_platform("指标解析中心")
        # page.screenshot_in_allure()
        print(to_ec)
        sleep(10)

        page: IndexPage







    # def test_creat(self,login_as):
    #     page = login_as("admin", "admin123")
    #     pass
    #     #
    #     # # page:   这里
    #     # page.click_platform("指标解析中心")
    #     # return CreateEsPage.click_source()
    #     pass

