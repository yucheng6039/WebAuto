// py.test -s  ../testcase/test_web --alluredir ../report/ --clean-alluredir
// allure generate ../report/ -o ../report/report --clean

rem allure open -h localhost -p 12347 ../report/report
// --repeat-scope=session
py.test  -s  ../testcase/test_web/test_home_page.py --alluredir ../report/xml --clean-alluredir
