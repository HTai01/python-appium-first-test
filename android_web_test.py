import unittest
from appium import webdriver
import os


class TestWebsiteAndroidChrome(unittest.TestCase):
    dc = {}
    test_name = 'Test Mobile Website on Android Chrome'
    # if you have configured an access key as environment variable,
    # use the line below. Otherwise, specify the key directly.
    accessKey = os.environ['SEETEST_IO_ACCESS_KEY']
    projectName = os.environ['PROJECT_NAME']
    driver = None

    def setUp(self):
        self.dc['testName'] = self.test_name
        self.dc['accessKey'] = self.accessKey
        self.dc['projectName'] = self.projectName
        self.dc['platformName'] = 'android'
        self.dc['browserName'] = 'chrome'
        self.driver = webdriver.Remote('https://stage.experitest.com:443/wd/hub', self.dc)

    def testUntitled(self):
        self.driver.get('https://google.com')
        self.driver.find_element_by_xpath("//*[@name='q']").send_keys('mobile automation testing')
        self.driver.find_element_by_xpath("//*[@name='btnG']").click()

    def tearDown(self):
        if self.driver is not None:
            print(self.driver.capabilities.get("reportUrl"))
            self.driver.quit()

    if __name__ == '__main__':
        unittest.main()

