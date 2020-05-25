#!/bin/bash
# 本人是用allure做的报告 pytest-html只是用来作为这个项目的示例
#pytest ../ --html=../report/report.html --self-contained-html


##allure generate ../report/xml -o ../report/xml/ --clean
#pytest ../testcase --alluredir ../report/xml  --html=../report/report.html --self-contained-html

#allure serve -h 0.0.0.0 -p 12349 ../report/xml/

# run 日志精析平台的test_log_home.py
py.test "../testcase/test_oganalysiscenter/test_log_home.py" --alluredir ../report/xml  --html=../report/report.html --self-contained-html
allure serve -h 0.0.0.0 -p 12349 ../report/xml/