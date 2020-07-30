from selenium import webdriver
import unittest
import time


# 执行测试的类
class LoginTest(unittest.TestCase):

    def setUp(self):
        # 测试前需执行的操作
        self.driver = webdriver.Chrome()  # 创建浏览器对象
        # self.driver.maximize_window()  # 设置窗口最大化
        self.driver.implicitly_wait(10)  # 设置网页加载时间
        self.url = 'http://192.168.0.122:8001'  # 定义url(setUp创建时首次执行的url)
        print("test start")

    # 正常登录成功，跳转的页面是否能定位到用户名
    def Test_login_right(self):
        self.driver.get(self.url)
        # 输入正常手机号
        phone = self.driver.find_element_by_css_selector(".log-content .login-view .login-form .el-input__inner")
        phone.send_keys('15555555555')
        # 输入对应验证码
        validation = self.driver.find_elements_by_class_name("el-input__inner")[1]
        validation.send_keys('0000')
        # 点击登录按钮
        self.driver.find_element_by_css_selector(".log-content .login-view .login-form .reg .reg_btn").click()
        time.sleep(1)
        try:
            self.driver.find_element_by_class_name("user_data")
            print("True")
        except Exception as e:
            print("False", format(e))

    # 异常登录
    # 手机号长度偏长,点击验证码输入框是否会报“请确认手机号的提示”
    def Test_login_error_len_long(self):
        self.driver.get(self.url)
        phone = self.driver.find_element_by_css_selector(".log-content .login-view .login-form .el-input__inner")
        phone.send_keys('157158598361')
        self.driver.find_elements_by_class_name("el-input__inner")[1].click()
        try:
            self.driver.find_element_by_class_name("el-form-item__error")
            print("True")
        except Exception as e:
            print("False", format(e))

    # 验证码不匹配
    def Test_login_error_validation(self):
        self.driver.get(self.url)
        phone = self.driver.find_element_by_css_selector(".log-content .login-view .login-form .el-input__inner")
        phone.send_keys('15715859836')
        validation = self.driver.find_elements_by_class_name("el-input__inner")[1]
        validation.send_keys('3333')
        self.driver.find_element_by_css_selector(".log-content .login-view .login-form .reg .reg_btn").click()
        time.sleep(1)
        try:
            self.driver.find_element_by_class_name("el-message__content")
            print("True")
        except Exception as e:
            print("False", format(e))

    def tearDown(self):
        # 测试用例执行完后所执行的操作
        print("test end")


if __name__ == '__main__':

    suite = unittest.TestSuite()
    suite.addTest(LoginTest("Test_login_right"))
    suite.addTest(LoginTest("Test_login_error_len_long"))
    suite.addTest(LoginTest("Test_login_error_validation"))

    runner = unittest.TextTestRunner()
    runner.run(suite)