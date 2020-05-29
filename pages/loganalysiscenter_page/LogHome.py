# Name:         log
# Description:  
# Author:       slm
# Date:         2020/5/22
from common.po_base import El
from common.po_base import Page
from common.page_action import PageAction
from selenium.webdriver import Chrome
from config import Driver_Path


class LogHome(Page):
    # 可以这么写单个元素
    sidebar_element = El("侧边栏菜单", x="//span[text()='首页']")
    key1 = El("ip/主机名", x="//input[@placeholder='输入主机名/IP']")



    # 也可以封装个函数 传侧边栏的名称
    def click_sidebar_element(self, v):
        self.click(x=f"//span[text()='{v}']")

        return self

    def sidebar_text(self,v):
        text = self.sidebar_element.find_element_by_xpath(f"//span[text()='{v}']").text
        return text

    def click_element(self,v):
         self.click(x=v)
         return self


if __name__ == "__main__":
    # te =LogHome(Page(Chrome(Driver_Path)))
    # print(te.sidebar_element)
    pass


