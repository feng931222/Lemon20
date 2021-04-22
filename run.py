



#调用查询函数，传参
from python_web import lesson02
from test_data import test_data
from selenium import webdriver

driver = webdriver.Chrome()
# driver.implicitly_wait(10)


#取出传参的实参
url = test_data.url['url']
user = test_data.user_info['username']
pwd = test_data.user_info['password']
s_key = test_data.s_key['s_key']
print(url,user,pwd,s_key)

#调用查询函数，传参
result_num = lesson02.search_key(url=url,driver=driver,username=user,password=pwd,s_key=s_key)
if s_key in result_num:
    print('查询结果正确')
else:
    print('查询结果错误，用例不通过')