
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import geckodriver_autoinstaller
import time

tele = input('Entrez votre numéro de téléphone : ')
mot_passe = input('Entrez votre mot de passe : ')
post = input('Entez votre poste: ')

geckodriver_autoinstaller.install()
driver = webdriver.Firefox()
wait = WebDriverWait(driver, 30)  # Increase the timeout if necessary
driver.get('https://m.facebook.com/')

password_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="pass"]')))
password_input.send_keys(mot_passe)

tele_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="email"]')))
tele_input.send_keys(tele)

login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]')))
login_btn.click()
whats_on_your_mind = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "بم تفكر يا Cmt؟")]')))

whats_on_your_mind.click()

post_text_area = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@aria-label="بم تفكر يا Cmt؟"]')))
for char in post:
    post_text_area.send_keys(char)
    time.sleep(0.1)

post_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[2]/div/div/div[1]/div/span/span')))
driver.execute_script("arguments[0].click();", post_btn)

time.sleep(5)

wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Your post is now published.')]")))
print('Post published successfully!')

driver.quit()

