import pytest
from selenium import webdriver

@pytest.fixture(scope="module")
def driver():
    # Configurar las opciones de Chrome
    chrome_options = webdriver.ChromeOptions()

    # Establecer la resolución deseada
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument('--ignore-ssl-errors=yes')
    chrome_options.add_argument('--ignore-certificate-errors')

    driver = webdriver.Remote(
        command_executor='http://selenium-server:4444/wd/hub',
        options=chrome_options
    )
    yield driver
    driver.quit()