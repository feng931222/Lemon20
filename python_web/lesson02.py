
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.implicitly_wait(10)


#打开网页封装成函数
def open_url(url,driver):
    driver.get(url)
    driver.maximize_window()


#登录封装成函数
def login(username,password,driver):
    driver.find_element_by_id('username').send_keys(username)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_id('btnSubmit').click()
    time.sleep(2)

#查询零售出库

def search_key(url,driver,username,password,s_key):
    open_url(url,driver)
    login(username,password,driver)
    driver.find_element_by_xpath('//span[text()="零售出库"]').click()
    time.sleep(2)
    #2、通过xpath切换iframe，输入查询单据信息
    driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@src="/pages/materials/retail_out_list.html"]'))
    driver.find_element_by_id('searchNumber').send_keys(s_key)

    #点击搜索按钮
    driver.find_element_by_id('searchBtn').click()
    time.sleep(3)
    #判断查询结果，是否包含806
    num = driver.find_element_by_xpath('//tr[@id="datagrid-row-r1-2-0"]//td[@field="number"]/div').text
    if s_key in num:
        print('查询结果正确')
    else:
        print('查询结果错误，用例不通过')