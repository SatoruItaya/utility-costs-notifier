from selenium.webdriver.common.by import By
from time import sleep

import datetime


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

    now = datetime.datetime.now()
    driver.switch_to.frame(driver.find_element(By.TAG_NAME, 'iframe'))

    if now.month == 1:
        previous_year_btn = driver.find_element(By.XPATH, '//*[@id="lbPre"]')
        previous_year_btn.click()
        sleep(5)
        usage_amount = driver.find_element(By.XPATH, '//*[@id="Tbl_MonthTable"]/tbody/tr[7]/td[5]/div').text
        billing_amount = driver.find_element(By.XPATH, '//*[@id="Tbl_MonthTable"]/tbody/tr[7]/td[6]/div').text
    else:
        previous_month = now.month - 1
        if previous_month <= 6:
            usage_amount = driver.find_element(By.XPATH, '//*[@id="Tbl_MonthTable"]/tbody/tr[' + str(previous_month + 1) + ']/td[2]/div').text
            billing_amount = driver.find_element(By.XPATH, '//*[@id="Tbl_MonthTable"]/tbody/tr[' + str(previous_month + 1) + ']/td[3]/div').text
        else:
            usage_amount = driver.find_element(By.XPATH, '//*[@id="Tbl_MonthTable"]/tbody/tr[' + str(previous_month - 6 + 1) + ']/td[5]/div').text
            billing_amount = driver.find_element(By.XPATH, '//*[@id="Tbl_MonthTable"]/tbody/tr[' + str(previous_month - 6 + 1) + ']/td[6]/div').text

    print(usage_amount)
    print(billing_amount)

    sleep(5)

    # TODO
    # componentを関数に
    # 前年遷移
    # usage_amountとbilling_amountを取得
