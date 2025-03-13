# from warnings import resetwarnings
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class HomePage:
    #locators
    link_newcustomer_xpath = "//a[normalize-space()='New Customer']"
    link_editcustomer_xpath = "//a[normalize-space()='Edit Customer']"
    link_deletecustomer_xpath = "//a[normalize-space()='Delete Customer']"
    link_changepwd_xpath = "//a[normalize-space()='Change Password']"
    link_logout_xpath = "//a[normalize-space()='Log out']"

    def __init__(self,driver):
        self.driver = driver

    def addingnewcustomer(self):
        self.driver.find_element(By.XPATH,self.link_newcustomer_xpath).click()

    def updatecutomerinfo(self):
        self.driver.find_element(By.XPATH,self.link_editcustomer_xpath).click()

    def deletecustomer(self):
        self.driver.find_element(By.XPATH,self.link_deletecustomer_xpath).click()

    def changepwd(self):
        self.driver.find_element(By.XPATH,self.link_changepwd_xpath).click()

    def logout(self):
        self.driver.find_element(By.XPATH,self.link_logout_xpath).click()


