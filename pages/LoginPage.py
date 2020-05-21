from common.po_base import El
from common.po_base import Page


class LoginPage(Page):

    username = El("用户名输入框", x="//*[@placeholder='请输入账号']")
    passwd = El("密码输入框", css="[placeholder='请输入密码']")
    logbtn = El("登陆按钮", x="//*[@type='submit']")


    def login(self, username, passwd):
        self.username.send_keys(username)
        self.passwd.send_keys(passwd)
        self.logbtn.click()
        return self.pm("IndexPage")(self)

    def is_login(self):
        return "192.168.21.41" in self.driver.current_url
