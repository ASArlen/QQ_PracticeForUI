import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from features.browser import Browser
from features.function.CommonFunction import switch_cur_handle
from features.function.Log import logger
from features.function import CommonFunction
from features.function.globalValues import globalValues


class test1(Browser):
    def reset_driver(self,driver):
        global py_web_driver
        py_web_driver = driver
        # self.CommonFunction =CommonFunction(py_web_driver)

    def __init__(self):
        global py_web_driver
        py_web_driver = self.driver
        global test_url
        test_url = self.url

    def test_0605(self,condiction1,condiction2):
        py_web_driver.get(test_url)
        logger.info(f'page：{condiction1},position:{condiction2}')
        for i in range(int(condiction1)):
            #下一页
            WebDriverWait(py_web_driver,60).until(EC.element_to_be_clickable((By.XPATH,'//*[@class="mb-6 md:mb-0 flex flex-nowrap items-center space-x-2"]/button[last()]'))).click()
            time.sleep(1)
        WebDriverWait(py_web_driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="border-b border-divider-border-2 dark:border-dark-divider-border-2"]/following-sibling::div/div[1]'))).click()
        CommonFunction.switch_cur_handle(py_web_driver)
        try:
            WebDriverWait(py_web_driver, 60).until(EC.element_to_be_clickable((By.XPATH,'<span>确定</span>'))).click()
        except:
            pass
        WebDriverWait(py_web_driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="question-detail-main-tabs"]/div[1]/div/div[2]/a/div/span/div'))).click()
        text = WebDriverWait(py_web_driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="css-19v6ljb-DiscussContent ei9q7no2"]/div[2]/div[2]'))).text
        logger.info(f'text:{text}')





