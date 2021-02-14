from selenium.webdriver import Chrome as ChromeWebdriver
from selenium.webdriver.chrome.options import Options
import os

class WebDriver(ChromeWebdriver):

    def __init__(self, b360bin=None, executable_path="chromedriver", port=0,
                 chrome_options=None, service_args=None,
                 desired_capabilities=None, service_log_path=None):
        if b360bin:
            self.bin = b360bin
        else:
            self.bin = r'%s\360Chrome\Chrome\Application\360chrome.exe' % os.getenv('LOCALAPPDATA')  ##你也可以读注册表来获取360的安装位置
        chrome_options = Options()
        chrome_options.binary_location = self.bin
        ChromeWebdriver.__init__(self, executable_path, port,
                    chrome_options, service_args,
                    desired_capabilities, service_log_path)