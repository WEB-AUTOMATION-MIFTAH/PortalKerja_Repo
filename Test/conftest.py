import os
import sys
import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service
from Config.dataconfig import TestData
import pytest
from platform import python_version, system
import platform

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="dev")

def pytest_html_report_title(report):
    report.title = "["+report.config.getoption("--url") + " env] "+"Automation Testing Report of WEB HRMS"

print(pytest.Config.getoption('--url'))

@pytest.hookimpl(tryfirst=True)
def pytest_metadata(metadata):
    keys_to_remove = ['Python', 'Platform', 'Packages', 'JAVA_HOME', 'Plugins']
    for key in keys_to_remove:
        if key in metadata:
            del metadata[key]

    metadata['Test Environment'] = url_value
    metadata['Python Ver.'] = python_version()
    metadata['Pytest Framework Ver.'] = pytest.__version__
    metadata['Platform OS'] = "{} {} {} {}".format(system(), platform.release(), platform.version(), platform.machine())

'''Fixture untuk scope : TEST FUNCTION'''
@pytest.fixture()
def setup_scope_function(request):
    web_driver = None
    browser = request.config.getoption("browser")
    url = request.config.getoption("url")

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])  # for chrome only
        options.add_experimental_option("detach", True)
        options.add_argument("--disable-notifications")  # for chrome only
        options.add_argument("--start-maximized")
        options.add_argument('--log-level=3')
        options.add_argument('--headless')
        web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    elif browser == "edge":
        web_driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

    web_driver.maximize_window()

    if url == "dev":
        web_driver.get(TestData.BASE_URL_DEV)
    elif url == "staging":
        web_driver.get(TestData.BASE_URL_STAGING)
    elif url == "prod":
        web_driver.get(TestData.BASE_URL_PROD)

    request.cls.driver = web_driver
    yield
    time.sleep(1.5)
    web_driver.quit()

'''Fixture untuk scope : TEST CLASS'''
@pytest.fixture(scope="class")
def setup_scope_class(request):
    web_driver = None
    browser = request.config.getoption("browser")
    url = request.config.getoption("url")

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])  # for chrome only
        options.add_experimental_option("detach", True)
        options.add_argument("--disable-notifications")  # for chrome only
        options.add_argument("--start-maximized")
        options.add_argument('--log-level=3')
        options.add_argument('--headless')
        web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    elif browser == "edge":
        web_driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

    web_driver.maximize_window()

    if url == "dev":
        web_driver.get(TestData.BASE_URL_DEV)
    elif url == "staging":
        web_driver.get(TestData.BASE_URL_STAGING)
    elif url == "prod":
        web_driver.get(TestData.BASE_URL_PROD)

    request.cls.driver = web_driver
    yield
    time.sleep(1.5)
    web_driver.quit()