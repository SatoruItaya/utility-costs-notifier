from selenium.webdriver.common.by import By
from time import sleep


def get_gas_cost(driver, mail_address, password):

    # login page
    driver.get('https://members.tokyo-gas.co.jp/')
    login_page_link = driver.find_element(By.CLASS_NAME, 'mtg-button-cta').get_attribute('href')
    driver.get(login_page_link)

    login_id_element = driver.find_element(By.XPATH, '//input[@name="loginId"]')
    login_id_element.send_keys(mail_address)

    password_element = driver.find_element(By.XPATH, '//input[@name="password"]')
    password_element.send_keys(password)

    # top page
    submit_btn = driver.find_element(By.ID, 'submit-btn')
    submit_btn.click()

    sleep(5)

    # total page
    total_page_link = driver.find_element(By.CLASS_NAME, 'mtg-content-number-link').get_attribute('href')
    driver.get(total_page_link)

    sleep(5)

    # detail page
    detail_page_link = driver.find_element(By.CLASS_NAME, 'mtg-button-link').get_attribute('href')
    driver.get(detail_page_link)

    sleep(5)

    usage_term = driver.find_element(By.XPATH, '//*[@id="gas"]/div[2]/div[1]/div/div[3]/p[2]/span[1]').text
    usage_days = driver.find_element(By.XPATH, '//*[@id="gas"]/div[2]/div[1]/div/div[3]/p[2]/span[2]').text
    billing_amount = driver.find_element(By.XPATH, '//*[@id="gas"]/div[2]/div[2]/div[1]/div[1]/p[2]/span').text
    usage_amount = driver.find_element(By.XPATH, '//*[@id="gas"]/div[2]/div[2]/div[2]/div[1]/p[2]/span').text
    yoy = driver.find_element(By.XPATH, '//*[@id="gas"]/div[2]/div[2]/div[2]/div[2]/p/span').text
    yoy_days = driver.find_element(By.XPATH, '//*[@id="gas"]/div[2]/div[2]/div[2]/div[2]/div/p[2]').text
    mom = driver.find_element(By.XPATH, '//*[@id="gas"]/div[2]/div[2]/div[2]/div[3]/p/span').text
    mom_days = driver.find_element(By.XPATH, '//*[@id="gas"]/div[2]/div[2]/div[2]/div[3]/div/p[2]').text

    print('使用期間:' + usage_term)
    print('使用日:' + usage_days)
    print('請求額:' + billing_amount)
    print('使用量:' + usage_amount)
    print('前年同月:' + yoy + '(' + yoy_days + ')')
    print('前月:' + mom + '(' + mom_days + ')')
