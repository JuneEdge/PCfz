from selenium import webdriver
import unittest
import time


# 执行测试的类
class CustomerTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)  # 设置网页加载时间
        self.url = 'http://192.168.0.122:8001'
        self.driver.get(self.url)
        # 输入正常手机号
        phone = self.driver.find_element_by_css_selector(".log-content .login-view .login-form .el-input__inner")
        phone.send_keys('15555555555')
        # 输入对应验证码
        validation = self.driver.find_elements_by_class_name("el-input__inner")[1]
        validation.send_keys('0000')
        # 点击登录按钮
        self.driver.find_element_by_css_selector(".log-content .login-view .login-form .reg .reg_btn").click()
        time.sleep(3)
        print("test start")

    # 新建人民币客户
    def Test_add_customer(self):

        # 定位供需管理——客户管理tabs
        self.driver.find_elements_by_class_name("el-submenu__title")[1].click()
        time.sleep(5)
        self.driver.find_elements_by_css_selector(".el-menu-item:first-child")[2].click()
        time.sleep(5)
        # 定位新建客户按钮
        self.driver.find_elements_by_class_name("el-button--small")[0].click()
        time.sleep(2)
        self.driver.find_elements_by_class_name("el-input__inner")[1].send_keys("五芳斋猪肉粽大公司")
        time.sleep(5)
        self.driver.find_elements_by_class_name("el-rate__item")[2].click()
        time.sleep(5)
        # self.driver.find_elements_by_class_name("el-input__inner")[3].click()
        # time.sleep(5)
        # self.driver.find_elements_by_class_name("el-select-dropdown__item")[2].click()
        # time.sleep(5)
        self.driver.find_elements_by_class_name("el-input__inner")[8].send_keys("李安")
        self.driver.find_elements_by_class_name("el-input__inner")[9].send_keys("13025265236")
        time.sleep(2)
        self.driver.find_elements_by_class_name("el-button--mini")[2].click()
        time.sleep(2)
        self.driver.find_elements_by_class_name("el-button--primary")[2].click()








    def tearDown(self):
        print("test end")


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(CustomerTest("Test_add_customer"))
    runner = unittest.TextTestRunner()
    runner.run(suite)