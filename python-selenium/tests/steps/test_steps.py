from selenium.webdriver.common.by import By
from pages.home_page import HomePage
from pages.who_we_are_page import WhoWeArePage
import time
from behave import given, when, then


@given("que estoy en la página de inicio")
def test_home_page(driver):
    home_page = HomePage(driver)
    home_page.go()
    time.sleep(10)
    assert "BCNC" in home_page.get_title()

@when('hago clic en el enlace "{link}"')
def click_on_menu_button(driver, link):
    try:

        driver.find_element(By.LINK_TEXT, link).click()
        
        driver.implicitly_wait(5)
    
    except Exception as e:
        print(f"Error in {link}: {str(e)}")

@then('debería ver los párrafos en la sección "{section}"')
def check_pharagraphs(driver, section):
    try:
        divs_text = driver.find_elements(By.CSS_SELECTOR, "div.text")
        for div_text in divs_text:
            paragraphs = div_text.find_elements(By.TAG_NAME, "p")
            for paragraph in paragraphs:
                print(f"Section: {section}\nText paragraph: {paragraph.text}\n")

    except Exception as e:
        print(f"Error in HOME: {str(e)}")

# def test_who_we_are_page(driver):
#     who_we_are_page = WhoWeArePage(driver)
#     who_we_are_page.go()
#     assert "BCNC" in who_we_are_page.get_title()
#     try:
#         time.sleep(10)
        
#         driver.find_element(By.LINK_TEXT, "WHO WE ARE").click()
        
#         driver.implicitly_wait(5)
        
#         divs_text = driver.find_elements(By.CSS_SELECTOR, "div.text")
#         for div_text in divs_text:
#             paragraphs = div_text.find_elements(By.TAG_NAME, "p")
#             for paragraph in paragraphs:
#                 print(f"Section: WHO WE ARE\nText paragraph: {paragraph.text}\n")
    
#     except Exception as e:
#         print(f"Error in WHO WE ARE: {str(e)}")