from selenium.webdriver.common.by import By
from time import sleep


def get_electricity_cost(driver, id, password):

    # login page
    driver.get('https://np-smartmansion.ipps.co.jp/login')

    login_id_element = driver.find_element(By.XPATH, '//*[@id="edit-name"]')
    login_id_element.send_keys(id)

    password_element = driver.find_element(By.XPATH, '//*[@id="edit-pass"]')
    password_element.send_keys(password)

    # top page
    submit_btn = driver.find_element(By.ID, 'edit-submit')
    submit_btn.click()

    sleep(5)

    # monthly usage page
    driver.get('https://np-smartmansion.ipps.co.jp/electricity-usage-monthly')

    sleep(5)

    driver.switch_to.frame(driver.find_element(By.TAG_NAME, 'iframe'))
    value = driver.find_element(By.XPATH, '//*[@id="Tbl_MonthTable"]/tbody/tr[3]/td[3]/div').text
    print(value)

    sleep(5)
