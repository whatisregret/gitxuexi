from utils.element_utils.element_utils import *

driver = open_Chrome()
get_Chrome(driver,"https://www.baidu.com/")
du = WaitElemXpath(driver,"xpath",'//*[@id="su"]').text
print(du)


