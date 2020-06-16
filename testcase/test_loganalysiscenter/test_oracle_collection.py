import allure
import pytest
from pages.loganalysiscenter_page.oracle_collection import LogHome
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
@allure.feature("oracle数据库采集")
class TestLogHome(object):
    @allure.title("创建oracle采集任务")
    def test_home(self,sign_in):
        page = LogHome(sign_in)
        page.click_sidebar_element('全局')
        page.click_sidebar_element("数据接入")
        page.switch_to_frame()
        page.click_element("//a[text()='数据接入']")
        page.click_element("//button[text()=' 创建']")
        page.click_element("//li[text()='关系型数据库']")
        page.click_element("//span[text()='Oracle']")
        page.key1.send_keys("192.168.32.37")
        page.key2.send_keys("49161")
        page.key3.send_keys("xe")
        page.key4.send_keys("system")
        page.key5.send_keys("oracle")
        name=page.random_str()
        page.key6.send_keys(name)
        page.click_css_element(".select .el-input__inner")  # 点击预估日流量
        page.click_element("//li/span[text()='200']")  # 点击200G
        page.click_css_element(".select .el-input__inner")
        page.click_element("//li/span[text()='1']")  # 点击1G
        sleep(1)
        page.click_element("//button[text()='连接测试']")
        sleep(1)
        page.key7.send_keys("select * from \"user\"")
        page.click_element("//button[text()='数据预览']")
        sleep(2)
        page.click_element("//span[text()='全量同步']")
        page.click_element("//input[@placeholder='选择关键字']")
        page.click_element("//ul[@id='el-autocomplete-9']/li[1]")
        page.key8.send_keys('*/1 * * * *')
        page.click_element("//button[text()='保存']")
        sleep(1)
        assert page.return_name(name) !='',"任务不存在"
        sleep(1)


# if __name__ =="__main__":
#     pytest.main("testcase/test_loganalysiscenter/test_mysql_collection.py","-s")