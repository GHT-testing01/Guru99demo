import time

from pageobjects.login_page import LoginPage
from testcases.conftest import setup
from pageobjects.home_page import HomePage
from utilities.logger import LogGen
from utilities.readdata import ReadData


#001- validate text message after success login
#002- validate user able to reset the login credentials
#003- validate the alert text msg when user enter invalid credentials
#004 - Add New Customer success
#005 - Reset New customer page
#006 - Edit Customer Info
#007 - Delete the customer
#008 - Change Password
#009 - Logout

class TestLoginPage:
    #baseurl = "https://demo.guru99.com/V4/"
    looger = LogGen.loggen()
    baseurl = ReadData.getbaseurl()
    userid= ReadData.getuserid()
    pwd=ReadData.getpwd()

#001 - validate text message after success login
    def test_login_success_001(self,setup):
        self.looger.info("******** Login_Success_Flow_Starting ********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        self.lp=LoginPage(self.driver)
        #self.lp.setuserid('mngr26593')
        #self.lp.setpassword('123Abc@')
        self.lp.setuserid(self.userid)
        self.lp.setpassword(self.pwd)
        self.lp.clicklogin()
        self.hpmsg = self.lp.confirmationmsgdisplay()
        time.sleep(10)
        self.driver.close()
        if "Welcome To Manager's Page of Guru99 Bank" in self.hpmsg:
            assert True
        else:
            assert False
        self.looger.info("******** Login_Success_Flow_Completed ********")

# 002- validate user able to reset the login credentials
    def test_reset_success_002(self,setup):
        self.looger.info("******** Reset_Login_Credential ********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        self.lp = LoginPage(self.driver)
        self.lp.setuserid('mngr26593')
        self.lp.setpassword('123Abc@')
        self.lp.clickreset()

        time.sleep(10)
        self.driver.close()
        self.looger.info("******** Reset_Login_Credential_Completed ********")
# 003- validate the alert text msg when user enter invalid credentials
    def test_alert_display_003(self,setup):
        self.looger.info("******** Verifying Alert without enter Password ********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        self.lp = LoginPage(self.driver)
        self.lp.setuserid('mngr26593')
        #self.lp.setpassword('123Abc@')
        self.lp.clicklogin()
        #self.alertmsg = self.lp.alerttextread()
        self.lp.aceptalert()

        if "user or password is not valid" in self.lp.alerttextread():
            assert True
        else:
            assert False
        time.sleep(10)
        self.driver.close()
        self.looger.info("******** Alert Displayed ********")
    # 009 - Logout Customer
    def test_logout_009(self,setup):
        self.looger.info("******** Verifying Alert As Logout success ********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        self.lp = LoginPage(self.driver)
        self.lp.setuserid('mngr26593')
        self.lp.setpassword('123Abc@')
        self.lp.clicklogin()

        self.hp=HomePage(self.driver)
        self.hp.logout()

        loalertmsg = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()

        if "Logged Out!!" in loalertmsg:
            assert True
        else:
            assert False

        self.looger.info("******** Logout Success Alert Displayed!!! ********")

#004 - Add New Customer success


#005 - Reset New customer page