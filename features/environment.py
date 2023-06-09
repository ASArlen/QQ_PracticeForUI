from features.browser import Browser
from selenium import webdriver
from features.function.Log import logger
from features.pages.test1_page import test1



def before_all(context):
    context.browser = Browser()

def before_feature(context,feature):
    options = webdriver.ChromeOptions()
    # options.add_argument("force-device-scale-factor=0.9")
    # options.add_argument("high-dpi-support=0.75")
    driver = webdriver.Chrome(r"C:\TEMP\chromedriver.exe", options=options)
    options.binary_location = r'C:\ProgramFiles\Google\Chrome\Application\chrome.exe'
    driver.maximize_window()
    # driver.implicitly_wait(30)
    # driver.execute_script("document.body.style.transform='scale(0.75)';")
    context.browser.reset_driver(driver)
    context.driver = driver

    context.test1_page = test1()
    context.test1_page.reset_driver(driver)


# def after_all(context):
#     try:
#         context.browser.close()
#     except BaseException:
#         pass





