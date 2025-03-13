import os.path
from datetime import datetime

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture()
def setup(browser):
    if browser == 'edge':
        service = Service(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service)
        print('Launching Edge browser')
    else:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        print('Launching Chrome browser')

    return driver
    #driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


############## PYTEST HTML REPORT ##############
# def pytest_configure(config):
#     config.metdata['projectname'] = 'Guru99'
#     config.metdata['ModuleName']='CusstomerRegistration'
#     config.metdata['Tester']='Dinesh'
#
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME",None)
#     metadata.pop("Plugins",None)
#
# @pytest.hookimpl(tryfirst=True)
# def pytest_configur(config):
#     config.option.htmlpath = os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%d-%m-%y %H-%M-%S")+".html"



