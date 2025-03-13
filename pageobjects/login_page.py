# from warnings import resetwarnings
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class LoginPage:
    #locators
    ib_userid_xpath = "//input[@name='uid']"
    ib_password_xpath = "//input[@name='password']"
    button_login_xpath = "//input[@name='btnLogin']"
    button_reset_xpath = "//input[@name='btnReset']"
    link_here_xpath = "//a[normalize-space()='here']"
    txt_confirmmsg_xpath = "//marquee[@class='heading3']"

    def __init__(self,driver):
        self.driver=driver

    def setuserid(self,userid):
        self.driver.find_element(By.XPATH,self.ib_userid_xpath).send_keys(userid)

    def setpassword(self,pwd):
        self.driver.find_element(By.XPATH,self.ib_password_xpath).send_keys(pwd)

    def clickreset(self):
        self.driver.find_element(By.XPATH,self.button_reset_xpath).click()

    def clicklogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def alerttextread(self):
        return self.driver.switch_to.alert.text

    def aceptalert(self):
        self.driver.switch_to.alert.accept()

    def confirmationmsgdisplay(self):
        return self.driver.find_element(By.XPATH,self.txt_confirmmsg_xpath).text





