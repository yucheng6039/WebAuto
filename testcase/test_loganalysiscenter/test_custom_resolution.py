import allure
import pytest

from conftest import set_options
from pages.loganalysiscenter_page.custom_resolution import LogHome
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
@allure.feature("自定义解析")
class TestLogHome(object):

    @allure.title("创建一个自定义解析")
    def test_home(self,sign_in):
        page = LogHome(sign_in)
        page.click_sidebar_element('全局')
        page.click_sidebar_element("数据接入")
        page.switch_to_frame()
        page.click_element("//a[text()='数据接入']")
        page.click_element("//a[text()='数据处理']")
        page.click_element("//button[text()=' 创建']")
        page.click_element("//li[text()='数据解析']")
        page.click_element("//a[@class='main-content pointer custom']") #点击自定义解析
        name = page.random_str()
        page.key1.send_keys(name)  #输入任务名字
        page.click_css_element(".el-select__input")  #选择任务源
        sleep(1)
        page.click_element("//span[text()='yucc_0628_02(文件和目录)']")  #点击任务源
        # page.click_element("//ul[@class='el-scrollbar__view el-select-dropdown__list']/li[40]")  #选取某个
        sleep(1)
        page.click_element("//button[text()='预览结果']")  #点击预览结果
        page.click_element("//span[text()='数据输出']")
        page.click_css_element(".select .el-input__inner") #点击预估日流量
        page.click_element("//li/span[text()='200']")  #点击200G
        page.click_css_element(".select .el-input__inner")
        page.click_element("//li/span[text()='1']") #点击1G
        sleep(1)
        page.click_element("//*[@id='app']/div[2]/div[2]/div[2]/div[2]/div/div/div/div/form/div[1]/div[1]/div[1]/div[1]/div/input")  #选择解析方式
        sleep(1)
        page.click_element("//ul[@class='el-scrollbar__view el-select-dropdown__list']/li[2]/span[text()='数据解构']") #选择解构
        page.key3.send_keys("@message")
        page.key4.send_keys("%{a},%{b},%{c},%{d},%{e},%{f},%{g}")
        page.click_element("//button[text()='预览结果']")
        page.click_element("//button[text()='保存']")
        sleep(3)
        assert page.return_name(name) != '', "任务不存在"
        sleep(1)