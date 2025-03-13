from selenium.webdriver.common.by import By

class RegistrationPage:
    #locators
    ib_customername_xpath ="//input[@name='name']"
    ib_genderM_xpath = "//input[@value='m']"
    ib_genderF_xpath = "//input[@value='f']"
    ib_calender_xpath = "//input[@id='dob']"
    ib_address_xpath = "//textarea[@name='addr']"
    ib_city_xpath = "//input[@name='city']"
    ib_state_xpath ="//input[@name='state']"
    ib_pin_xpath="//input[@name='pinno']"
    ib_mobile_xpath="//input[@name='telephoneno']"
    ib_email_xpath="//input[@name='emailid']"
    ib_password_xpath="//input[@name='password']"
    btn_submit_xpath="//input[@name='sub']"
    btn_reset_xpath="//input[@name='res']"
    link_home_xpath="//a[normalize-space()='Home']"

    #constructor
    def __init__(self,driver):
        self.driver=driver

    def setcustomername(self,customername):
        self.driver.find_element(By.XPATH,self.ib_customername_xpath).sendkeys(customername)

    def selectgender(self):
        self.driver.find_element(By.XPATH,self.ib_genderF_xpath).click()

    def clickreset(self):
        self.driver.find_element(By.XPATH,self.btn_reset_xpath).click()



