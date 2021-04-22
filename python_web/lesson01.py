


"""
web自动化
代码python   ---浏览器驱动 ----浏览器

selenium库：第三方库  1）安装pip   2）导入
1、ide：录制脚本   ----实际使用不多
2、RC
3、webdriver   利用浏览器原生API，直接操作浏览器页面的元素---重点掌握
4、分布式

2、浏览器驱动
1）下载对应浏览器版本的驱动
2）解压后得到后缀exe的文件，放到python的安装目录下

3、等待方式
time.sleep()  强制等待，没有完成等待时间，不往下执行
隐式等待：可以设置一个等待时间，在这个等待时间还没结束之前元素找到了，不继续等待，继续执行下面的代码
    注意：一个session会话里面值需要调用一次
4、元素定位  ——获取页面元素，进行接下来的操作，例如输入，点击等等  ===掌握重点
八种元素定位：id、name、xpath、css、class、tag、link_text、partial_link_text
1)id:当前整个html（页面唯一，类比身份证信息（进行元素定位的首选，动态id不做考虑）

2）xpath：
⑴、绝对路径/相对路径
标签名+属性 = //标签名[@属性名=属性值]
//input[@id="username"] --xpath表达方式
a、绝对路径 ---基本不用 /html/body/div[1]/aside/div/section/div[1]/div[2]/p   （一旦页面发生修改，元素定位就失效了）
b、相对路径 ---//input[@id="username"]  #定位获取登录账号   （有属性名）
           ---//p             #定位获取登录用户信息  （无属性名）
⑵、层级定位
//标签名[@属性名=属性值]//标签名[@属性名=属性值]
-//div[@class="login-logo"]//b

⑶、文本属性定位：//标签名[text()="柠檬班ERP"]

⑷、包含属性值：//标签名[contains(@属性名/text(),属性值]
---//input[contains(@class,"username")]




5、前端基础知识：web页面=html(语言)+css(页面布局)+javascript(脚本交互)
"""
#web页面的常用操作
#1、打开浏览器
#dviver = webdriver.Chrome()
#dviver.get("http://erp.lemfix.com/login.html")

#2、最大化浏览器
#driver.maximize_window()

#3、前进、后退和刷新操作
#driver.back()  #返回到上一个页面
#driver.forward()  #前进到下一个页面
#driver.refresh()  #刷新页面

#4、关闭浏览器
#关闭Chromedriver服务：driver.quit()
#关闭当前窗口：driver.close()



from selenium import webdriver   #从selenium库中导入webdriver功能
import time       #导入time功能

#启动谷歌浏览器，打开一个网址
# driver = webdriver.Chrome()
# driver.get('http://erp.lemfix.com/login.html')
# # driver.get('https://www.dota2.com.cn/')
# time.sleep(2)
#浏览器窗口最大化
# driver.maximize_window()


#后退、前进、刷新
# time.sleep(2)
# driver.back()#返回到上一个页面
# time.sleep(2)
# driver.forward()#前进到下一个页面
# time.sleep(2)
# driver.refresh()  #刷新页面

#关闭浏览器
# driver.close()   #关闭当前浏览器
# driver.quit()    #退出dviver，关闭所有关联浏览器窗口


#用例1：打开一个ERP网址
driver = webdriver.Chrome()
driver.get('http://erp.lemfix.com/login.html')
driver.maximize_window()
time.sleep(1)
#driver.implicitly_wait(10)   #隐式等待，默认等待10S

#用例2：输入正确的用户和密码，点击登录
driver.find_element_by_id('username').send_keys('13916686542')
driver.find_element_by_id('password').send_keys('lemon123')
driver.find_element_by_id('btnSubmit').click()
time.sleep(2)

#用例3：判断页面登录用户信息 是否正常
login_user = driver.find_element_by_xpath('//p').text
if login_user =='13916686542':
    print('这个登录用户名是{}'.format(login_user))
else:
    print('这条登录用户名不正确!')
# print(login_user)

#用例4：点击 零售出库
driver.find_element_by_xpath('//span[text()="零售出库"]').click()
time.sleep(2)

#用例5：单据编号框输入806
'''
在一个固定的地方可以切换多个页面，并且其他的内容不变（左侧树，右侧内容，顶部导航等）
整个html页面下面嵌套了一个html页面——iframe框架设计

1、识别是否有子页面的方式，页面层级路径中出现iframe，就需要切换iframe，才可以进行元素定位
2、怎么去切换？     driver.switch_to.frame()
1）id或name去切换
2）xpath来切换
3）通过iframe下标来定位：从0开始，第一个iframe=0，第二个iframe=1,。。。。；
driver.switch_to.frame(1)
'''

#1、通过ID切换iframe
#driver.switch_to.frame("tabpanel-0a8b47c0e6-frame")  报错无法进行读取tabpanel-0a8b47c0e6-frame

#2、通过xpath切换iframe
driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@src="/pages/materials/retail_out_list.html"]'))

#3、通过iframe下标切换
#driver.switch_to.frame(1)



driver.find_element_by_id('searchNumber').send_keys('806')
#点击搜索
driver.find_element_by_id('searchBtn').click()
time.sleep(3)
#判断查询结果，是否包含806
num = driver.find_element_by_xpath('//tr[@id="datagrid-row-r1-2-0"]//td[@field="number"]/div').text
if "806" in num:
    print('查询结果正确')
else:
    print('查询结果错误，用例不通过')