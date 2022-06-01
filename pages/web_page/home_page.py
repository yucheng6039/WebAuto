import random
import uuid

from common.po_base import El
from common.po_base import Page
from common.page_action import PageAction
from selenium.webdriver import Chrome
from config import Driver_Path


class LogHome(Page):
    # 可以这么写单个元素
    key1 = El("点击邮箱", x="/html/body/app-root/div/div/app-login/div/div/mat-card/mat-card-content/form/div[1]/mat-form-field/div/div[1]/div/input")
    key2 = El("输入密码", x="/html/body/app-root/div/div/app-login/div/div/mat-card/mat-card-content/form/div[2]/mat-form-field/div/div[1]/div/input")
    key3 = El("登录",x="/html/body/app-root/div/div/app-login/div/div/mat-card/mat-card-content/form/button")
    key4 = El("显示名",x="//*[@id='topButton']/button/span[1]/span/span")
    key5 = El("输入",x="/html/body/div[2]/div[2]/div/mat-dialog-container/app-dialog/div[1]/mat-form-field/div/div[1]/div/input")
    key6= El("上传",x="/html/body/app-root/div/div[2]/app-upload-files/form/file-upload/label/input")
    key7 = El("点击",x="document.querySelector('#mat-dialog-1 > app-dialog > div.mat-dialog-actions > button:nth-child(2) > span.mat-button-wrapper')")




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
        str1=b[0:5]
        return str1 # 返回随机字符串

    def return_name(self,v):
        key4 = El("任务名称", x=f"//a[text()='{v}']")
        return key4

# if __name__ == "__main__":
#     # te =LogHome(Page(Chrome(Driver_Path)))
#     # print(te.sidebar_element)
#     pass