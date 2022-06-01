import os

BaseDir = os.path.dirname(os.path.abspath(__file__))

# http://npm.taobao.org/mirrors/chromedriver/     请在镜像库下载webdriver
Driver_Path = os.path.join(BaseDir, "static/driver/chromedriver")



Start_Url = "https://panelbuilderdev.azurewebsites.net/#/login"

Step_Time = 0.2  # 每一步间隔
DefaultTimeOut = 5  # 默认等待时间
