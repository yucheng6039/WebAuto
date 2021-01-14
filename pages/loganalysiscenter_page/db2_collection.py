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
    key1 = El("ip/主机名", x="//input[@placeholder='输入主机名/IP']")
    key2 = El("输入端口", x="//input[@placeholder='输入端口']")
    key3 = El("输入数据库", x="//input[@placeholder='输入数据库名']")
    key4 = El("输入用户名", x="//input[@placeholder='输入数据库用户名']")
    key5 = El("输入密码", x="//input[@placeholder='输入数据库密码']")
    key6 = El("任务名", x="//input[@placeholder='请输入任务名称']")
    key7 = El("sql语句", css=".mr-10 > .el-input__inner")
    key8 = El("采集周期", x="//input[contains(@placeholder,'输入5位')]")
    # 也可以封装个函数 传侧边栏的名称
    def click_sidebar_element(self, v):
        self.click(x=f"//span[text()='{v}']")

        return self

    def sidebar_text(self,v):
        text = self.find_element_by_xpath(f"//span[text()='{v}']").text
        return text

    def click_element(self,v):
         self.click(x=v)
         return self

    def click_css_element(self,v):
         self.click(css=v)
         return self

    def return_name(self,v):
        key = El("任务名称", x=f"//a[text()='{v}']")
        return key

    def random_str(self,num=6):
        uln = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
        rs = random.sample(uln, num)  # 生成一个 指定位数的随机字符串
        a = uuid.uuid1()  # 根据 时间戳生成 uuid , 保证全球唯一
        b = ''.join(rs + str(a).split("-"))  # 生成将随机字符串 与 uuid拼接
        return b  # 返回随机字符串

# if __name__ == "__main__":
#     # te =LogHome(Page(Chrome(Driver_Path)))
#     # print(te.sidebar_element)
#     pass



