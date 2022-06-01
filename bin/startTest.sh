#!/bin/bash
# 本人是用allure做的报告 pytest-html只是用来作为这个项目的示例
#pytest ../ --html=../report/report.html --self-contained-html


#allure generate ../report/xml -o ../report/xml/ --clean
#pytest ../testcase/test_web/
#
#
#allure serve -h 0.0.0.0 -p 12346 ../report/xml/

# run 日志精析平台的test_log_home.pyiota
#py.test "../testcase/test_web/"
#allure serve -h 0.0.bin/startTest.sh:130.0 -p 12349 ../report/xml/


py.test --count=40 --repeat-scope=session -s  ../testcase/test_loganalysiscenter/test_user/* --alluredir ../report/xml --clean-alluredir

allure serve -h 0.0.0.0 -p 12347 ../report/xml/
