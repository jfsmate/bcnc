from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home_page import HomePage
from pages.who_we_are_page import WhoWeArePage
import time
import pytest


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

def test_home_page(driver):
    home_page = HomePage(driver)
    home_page.go()
    assert "BCNC" in home_page.get_title()
    try:
        time.sleep(10)
        
        driver.find_element(By.LINK_TEXT, "HOME").click()
        
        driver.implicitly_wait(5)
        
        divs_text = driver.find_elements(By.CSS_SELECTOR, "div.text")
        for div_text in divs_text:
            paragraphs = div_text.find_elements(By.TAG_NAME, "p")
            for paragraph in paragraphs:
                print(f"Section: HOME\nText paragraph: {paragraph.text}\n")
    
    except Exception as e:
        print(f"Error in HOME: {str(e)}")

def test_who_we_are_page(driver):
    who_we_are_page = WhoWeArePage(driver)
    who_we_are_page.go()
    assert "BCNC" in who_we_are_page.get_title()
    try:
        time.sleep(10)
        
        driver.find_element(By.LINK_TEXT, "WHO WE ARE").click()
        
        driver.implicitly_wait(5)
        
        divs_text = driver.find_elements(By.CSS_SELECTOR, "div.text")
        for div_text in divs_text:
            paragraphs = div_text.find_elements(By.TAG_NAME, "p")
            for paragraph in paragraphs:
                print(f"Section: WHO WE ARE\nText paragraph: {paragraph.text}\n")
    
    except Exception as e:
        print(f"Error in WHO WE ARE: {str(e)}")