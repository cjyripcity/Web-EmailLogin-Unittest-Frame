import time
import selenium
from selenium import webdriver
from lxml import etree

# 登录业务函数
def Login(email, password):
    driver = webdriver.Chrome()
    driver.get('https://mail.163.com/')
    # 登录框是采用iframe形式
    iframe = driver.find_element_by_xpath('//*[@scrolling="no"]')
    # 进入iframe框架 才能定位元素
    driver.switch_to.frame(iframe)
    # 输入框的元素定位
    driver.find_element_by_name("email").send_keys(email)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_id("dologin").click()

    # source = etree.HTML(driver.page_source)
    # display = source.xpath('//*[@id="nerror"]')
    # for index in range(len(display)):
    #     print(display[index].tag)
    #     print(display[index].attrib)
    #     print(display[index].text)

    time.sleep(2)      # 强制等待2s 否则后面登录显示信息显示不出

    display = driver.find_element_by_id('nerror')      # 获取登录失败报错信息display
    # print(display.get_attribute('title'))            # 和测试用例数据信息对比
    # driver.quit()

    return display.text



