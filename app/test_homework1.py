import pytest
from appium import webdriver


class TestHomework1:

    def setup_method(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.WwMainActivity"
        caps["noReset"] = "true"
        caps["dontStopAppOnReset"] = "true"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        self.driver.back()

    @pytest.mark.parametrize(('user', 'msg'), [
        ('testname1', '测试code'),
        ('testname2', '测试code'),
        ('testname3', '测试code')
    ])
    def testhomework1(self, user, msg):
        # 点击搜索按钮
        self.driver.find_element_by_id("com.tencent.wework:id/gq_").click()
        # 搜索联系人
        self.driver.find_element_by_id("com.tencent.wework:id/ffq").send_keys(user)
        # 点击联系人
        self.driver.find_element_by_id("com.tencent.wework:id/czs").click()
        # 输入消息内容
        self.driver.find_element_by_id("com.tencent.wework:id/dtv").send_keys(msg)
        # 点击发送
        self.driver.find_element_by_id("com.tencent.wework:id/dtr").click()
