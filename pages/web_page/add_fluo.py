import random
import uuid

from common.po_base import El
from common.po_base import Page
from common.page_action import PageAction
from selenium.webdriver import Chrome
from config import Driver_Path


class LogHome(Page):
    # 可以这么写单个元素
    key1 = El("点击邮箱",
              x="/html/body/app-root/div/div/app-login/div/div/mat-card/mat-card-content/form/div[1]/mat-form-field/div/div[1]/div/input")
    key2 = El("输入密码",
              x="/html/body/app-root/div/div/app-login/div/div/mat-card/mat-card-content/form/div[2]/mat-form-field/div/div[1]/div/input")
    key3 = El("登录", x="/html/body/app-root/div/div/app-login/div/div/mat-card/mat-card-content/form/button")
    key4 = El("create new",
              x="/html/body/app-root/div/div/app-framework-container/div/div/div[1]/app-panels/div[2]/mat-toolbar/mat-toolbar-row/div/app-button-primary[1]/button")
    key5 = El("NEXT BUTTON", x="/html/body/app-root/div/div/app-panel/div[2]/div[2]/span/app-button-primary/button")
    key6 = El("next button", x="/html/body/app-root/div/div/app-panel/div[2]/div[2]/span/app-button-primary/button/span[1]")
    key7 = El("点击",
              x="/html/body/app-root/div/div/app-panel/div[1]/mat-tab-group/div/mat-tab-body[1]/div/div/div[3]/div[2]/app-radio-card/mat-card/div[1]")
    key8 = El("点击",
              x="/html/body/app-root/div/div/app-panel/div[1]/mat-tab-group/div/mat-tab-body[2]/div/div/form/div[1]/mat-form-field/div/div[1]/div/input")

    key9 = El("NEXT BUTTON", x="//td[@role='cell']")
    key10 = El("NEXT BUTTON", x="/html/body/app-root/div/div/app-panel/div[1]/mat-tab-group/div/mat-tab-body[3]/div/div/div[2]/div/app-button-secondary/button")


    # 也可以封装个函数 传侧边栏的名称
    def click_sidebar_element(self, v):
        self.click(x=f"//span[text()='{v}']")

        return self

    def sidebar_text(self, v):
        text = self.sidebar_element.find_element_by_xpath(f"//span[text()='{v}']").text
        return text

    def click_element(self, v):
        self.click(x=v)
        return self

    def click_css_element(self, v):
        self.click(css=v)
        return self

    def random_str(self, num=6):
        uln = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
        rs = random.sample(uln, num)  # 生成一个 指定位数的随机字符串
        a = uuid.uuid1()  # 根据 时间戳生成 uuid , 保证全球唯一
        b = ''.join(rs + str(a).split("-"))  # 生成将随机字符串 与 uuid拼接
        str1 = b[0:5]
        return str1  # 返回随机字符串

    def return_name(self, v):
        key4 = El("任务名称", x=f"//a[text()='{v}']")
        return key4

    def isElementExist(self, v):
        flag = True
        try:
            self.find_element_by_xpath(v)
            return flag
        except:
            flag = False
            return flag

# if __name__ == "__main__":
#     # te =LogHome(Page(Chrome(Driver_Path)))
#     # print(te.sidebar_element)
#     pass