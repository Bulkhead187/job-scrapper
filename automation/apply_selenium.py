from selenium import webdriver
from selenium.webdriver.common.by import By

def apply_to_indeed_job(job_url, cv_path, cover_letter):
    driver = webdriver.Chrome()
    driver.get(job_url)
    
    # Login-Logik hier einfügen (falls nötig)
    driver.find_element(By.ID, "apply-button").click()
    driver.find_element(By.NAME, "resume").send_keys(cv_path)
    driver.find_element(By.NAME, "cover_letter").send_keys(cover_letter)
    driver.find_element(By.ID, "submit-application").click()
    
    driver.quit()