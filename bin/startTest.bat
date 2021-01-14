py.test -s  ../testcase/test_loganalysiscenter/test_user/ --alluredir ../report/ --clean-alluredir
allure generate ../report/ -o ../report/report --clean

rem allure open -h localhost -p 12347 ../report/report