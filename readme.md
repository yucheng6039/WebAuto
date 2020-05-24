# 自动化测试文档

## 怎么运行

1. 下载镜像

    [淘宝WebDriver镜像](http://npm.taobao.org/mirrors/chromedriver/)
    
2. 执行命令

    ```shell script
    pip install -r requirements.txt
    cd bin
    ./startTest.sh
    # or ./startTest.bat
    ```

## 目录结构参数

- common 通用类
- pages po对象
- testcase 存放测试用例
- utils 存放工具类
- config.py 配置文件
- conftest.py pytest存放feature的位置
- static 静态文件目录
    - test_page.html 测试用的html文件
    - chromedriver.exe
- requirements.txt 项目依赖文件

## Page

```python

from common.po_base import Page
from common.po_base import El


class LoginPage(Page):

    username = El("用户名输入框", name="username")
    passwd = El("密码输入框", name="pwd")
    logbtn = El("登陆按钮", css="button")

    def login(self, username, passwd):
        self.username.send_keys(username)
        self.username.send_keys(passwd)
        self.logbtn.click()
        return self.pm("IndexPage")(self)

```

## 参考资料

poium库（作者：虫师）`pip isntall poium`


