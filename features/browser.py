"""
此类中对一些Selenium基础方法做了封装，所有脚本均继承Browser类。
"""
import time
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from features.function.Log import logger
from features.function.YamlHandler import yaml_data



class Browser(object):
    driver = webdriver.Chrome
    # global py_web_driver
    # py_web_driver = driver
    environment = yaml_data.environment
    yaml_config = yaml_data[environment]


    # url = yaml_config.url
    url = "https://leetcode.cn/problemset/all/"

    # conn = pymssql.connect(server = )

    def reset_driver(self,driver):
        # self.driver = driver
        global py_web_driver
        py_web_driver = driver

    def close(self):
        py_web_driver.quit()

    def get_elements(self,locator,wait_time=60,polling_time=1):
        """
        显示等待获取元素
        :param locator: 定位元素xpath
        :param wait_time: 最长等待时间
        :param polling_time: 轮询查询元素时间
        :return:
        """
        time.sleep(2)
        for i in range(2):
            try:
                return WebDriverWait(py_web_driver, wait_time,polling_time).until(EC.element_to_be_clickable((By.XPATH, locator)))
            except Exception as e:
                logger.info(f'Through {locator} to find this element error')
                if 1 == 1:
                    raise e
                continue


    def click_element(self,locator,js_flag=False,wait_time=60,polling_time=1):
        """
        单机元素
        :param locator: 元素定位xpth
        :param js_flag: 是否使用js点击，使用则传为true，默认false
        :param wait_time: 最长等待时间
        :param polling_time: 轮询元素定位时间
        :return:
        """
        if not js_flag:
            ele = self.get_elements(locator, wait_time, polling_time)
            try:
                ele.click()
            except ElementClickInterceptedException:
                py_web_driver.execute_script("arguments[0].click();",ele)
        else:
            py_web_driver.execute_script("$(arguments[0]).click();",self.get_elements(locator,wait_time,polling_time))

    def input_keys(self,locator,text='auto test',wait_time=60,polling_time=1):
        """
        文本框输入
        :param locator:
        :param text:
        :param wait_time:
        :param polling_time:
        :return:
        """
        ele = self.get_elements(locator,wait_time,polling_time)
        ele.clear()
        ele.send_keys(text)

    def get_element_text(self,locator,wait_time=60,polling_time=1):
        """
        获取文本框中元素
        :param locator:
        :param wait_time:
        :param polling_time:
        :return:
        """
        return self.get_elements(locator,wait_time,polling_time).text

    def high_light_ele(self, locator, roll_back_flag=True, wait_time=60, polling_time=1):
        """
        调用js方法高亮选择的ele
        """
        element = self.get_element(locator, wait_time, polling_time)
        border = element.value_of_css_property('border')
        # background = element.value_of_css_property('background')
        py_web_driver.execute_script('arguments[0].style.border="5px solid red";', element)
        # self._driver.execute_script('arguments[0].style.background="green";', value)
        if roll_back_flag:
            time.sleep(2)
            py_web_driver.execute_script(f'arguments[0].style.border="{border}";', element)
            # self._driver.execute_script(f'arguments[0].style.background="{background}";', va

    def get_screen_shot(self, file_path):
        """
        将当前窗口的屏幕截图保存到图像文件中.
        """
        self.driver.get_screenshot_as_file(file_path)
        logger.info("✅ 将当前窗口的屏幕截图保存到图像文件中：{} ".format(file_path))


    def window_scroll_to(self, left='0', top='0'):
        """
        控制浏览器滚动条的位置
        :param left: 水平的左边距
        :param top: 垂直的上边距
        Usage:
            window_scroll_to(100, 0)  #右滑
            execute_script("window.scrollTo(document.body.scrollWidth, 0)");
            window_scroll_to(0, 100)  #下滑
            execute_script("window.scrollTo(0, document.body.scrollHeight)");
        """
        scroll = "window.scrollTo(%s, %s);" % (left, top)
        self.js(scroll)
        logger.info("✅ 控制浏览器向右滑动{}，向下滑动{} ".format(left, top))

    def accept_alert(self):
        """
        接受警告框
        """
        self.driver.switch_to.alert.accept()
        logger.info("✅ 确认弹框 ")

    def dismiss_alert(self):
        """
        忽略弹框
        """
        self.driver.switch_to.alert.dismiss()
        logger.info("✅ 取消弹框 ")

    def get_alert_text(self):
        """
        得到弹框的文本.
        """
        text = self.driver.switch_to.alert.text
        logger.info("✅ 弹框的文本为：{} ".format(text))
        return text

    def js(self, script):
        """
        执行JavaScript脚本.
        用法: driver.js("window.scrollTo(200,1000);")
        :param script: JavaScript脚本
        :return:
        """
        try:
            self.driver.execute_script(script)
            logger.info(f"执行js脚本：{script} ")
        except Exception as e:
            error_msg = "未能正确执行js脚本：{} ".format(script)
            logger.error(error_msg)
            return e