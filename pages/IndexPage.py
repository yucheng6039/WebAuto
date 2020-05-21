from selenium.webdriver.common.keys import Keys

from common.po_base import Page, El


class IndexPage(Page):

    is_login = True

    index_platfrom = El("点击统一门户的平台",c=".portal>div.content>ul>li")

    def click_platform(self,v):
        self.click(x=f"//*[text()='{v}']")
        return self









