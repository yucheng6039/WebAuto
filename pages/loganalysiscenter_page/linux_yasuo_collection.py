import random
import uuid

from common.po_base import El
from common.po_base import Page
from common.page_action import PageAction
from selenium.webdriver import Chrome
from config import Driver_Path


class LogHome(Page):
    # 可以这么写单个元素
    sidebar_element = El("侧边栏菜单", x="//span[text()='首页']")
    key1 = El("任务名", x="//input[@placeholder='请输入任务名称']")
    key2 = El("输入主机名、IP", x="//input[@placeholder='输入主机名、IP地址或类型']")
    key3 = El("路径",x="//input[@placeholder=\"请填写文件路径，多路径以';'间隔\"]")

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

    def click_css_element(self,v):
         self.click(css=v)
         return self

    def random_str(self,num=6):
        uln = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
        rs = random.sample(uln, num)  # 生成一个 指定位数的随机字符串
        a = uuid.uuid1()  # 根据 时间戳生成 uuid , 保证全球唯一
        b = ''.join(rs + str(a).split("-"))  # 生成将随机字符串 与 uuid拼接
        return b  # 返回随机字符串

    def return_name(self,v):
        key4 = El("任务名称", x=f"//a[text()='{v}']")
        return key4

# if __name__ == "__main__":
#     # te =LogHome(Page(Chrome(Driver_Path)))
#     # print(te.sidebar_element)
#     pass