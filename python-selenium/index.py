import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://bcncgroup.com/")


sections = ["HOME", "WHO WE ARE"]

def extract_paragraphs(section):
    try:
        time.sleep(10)
        
        driver.find_element(By.LINK_TEXT, section).click()
        
        driver.implicitly_wait(5)
        
        divs_text = driver.find_elements(By.CSS_SELECTOR, "div.text")
        for div_text in divs_text:
            paragraphs = div_text.find_elements(By.TAG_NAME, "p")
            for paragraph in paragraphs:
                print(f"Section: {section}\nText paragraph: {paragraph.text}\n")
    
    except Exception as e:
        print(f"Error in {section}: {str(e)}")

for section in sections:
    extract_paragraphs(section)

driver.quit()
