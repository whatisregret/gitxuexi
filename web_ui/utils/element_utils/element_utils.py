import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.log_utils.logs_utils import INFO
from config.setting import ConfigHandler


# 打开谷歌浏览器
def open_Chrome():
    driver = webdriver.Chrome(ConfigHandler.web_path)
    return driver


# 输入网址
def get_Chrome(driver, url):
    driver.get(url)


# 关闭谷歌浏览器
def close_Chrome(driver):
    time.sleep(3)
    driver.quit()


# 静态等待传入元素选择器和元素
def WaitElemXpath(driver, tp, locator):
    try:
        if tp == 'xpath':
            elem = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, locator)))
            return elem
        elif tp == 'id':
            elem = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, locator)))
            return elem
        elif tp == 'css':
            elem = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
            return elem
        elif tp == 'class':
            elem = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, locator)))
            return elem
        elif tp == 'name':
            elem = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.NAME, locator)))
            return elem
        elif tp == 'tag':
            elem = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.TAG_NAME, locator)))
            return elem
        # 超链接字符串定位元素
        elif tp == 'link':
            elem = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, locator)))
            return elem
        else:
            INFO.logger.info("请输入正确的元素选择器,当前选择器为:" + tp)
            return None
    except Exception as e:
        INFO.logger.info(e)
        return "查询元素失败" + str(e)


# 隐性等待
def implicitly_wait(driver):
    driver.implicitly_wait(30)


if __name__ == '__main__':
    pass
