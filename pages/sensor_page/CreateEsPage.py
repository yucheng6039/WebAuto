# Name:         create_es_page
# Description:  
# Author:       slm
# Date:         2020/5/20

from common.po_base import El
from common.po_base import Page


class CreateEsPage(Page):
    create_source = El("点击数据源",x ="//label[contains(text(),'数据源')]")
    create_css = El("点击创建数据源按钮", c=".el-icon-plus")
    input_source_name_css = El("数据源的输入框", c="[placeholder='20个字符以内，包含英文字母、数字、中文或_，非数字开头']")
    input_es_address_css = El("数据源IP地址输入框", c ="[placeholder='请输入ES IP地址（IP:PORT）']")
    # side_menu=El()
    #
    #
    # def select_menu(self,mune_name):
    #     self.side_menu.find_element_by_xpath(f".//*[text()='{mune_name}']")
    #     return self
    def click_source(self):
        # self.create_source.click()
        self.create_source.click()
        return self.pm("HomePage")(self)

    def click_add(self):
        return self.create_css.click()