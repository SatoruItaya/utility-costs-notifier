from selenium.webdriver.common.by import By
from time import sleep

import datetime


def transition_to_previous_year(driver):
    previous_year_btn = driver.find_element(By.XPATH, '//*[@id="lbPre"]')
    previous_year_btn.click()
    sleep(5)


def get_monthly_detail(month, driver):
    if month <= 6:
        usage_amount = driver.find_element(By.XPATH, '//*[@id="Tbl_MonthTable"]/tbody/tr[' + str(month + 1) + ']/td[2]/div').text

        # If there is no data
        if usage_amount == '0.0':
            usage_amount = '-'
            billing_amount = ''
        else:
            billing_amount = driver.find_element(By.XPATH, '//*[@id="Tbl_MonthTable"]/tbody/tr[' + str(month + 1) + ']/td[3]/div').text
    else:
        usage_amount = driver.find_element(By.XPATH, '//*[@id="Tbl_MonthTable"]/tbody/tr[' + str(month - 6 + 1) + ']/td[5]/div').text

        # If there is no data
        if usage_amount == '0.0':
            usage_amount = '-'
            billing_amount = ''
        else:
            billing_amount = driver.find_element(By.XPATH, '//*[@id="Tbl_MonthTable"]/tbody/tr[' + str(month - 6 + 1) + ']/td[6]/div').text

    return usage_amount, billing_amount


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

    base_month = 0
    base_year = 0

    # get details in target month
    if now.month == 1:
        base_month = 12
        base_year = now.year - 1
        transition_to_previous_year(driver)
    else:
        base_month = now.month - 1
        base_year = now.year

    usage_amount, billing_amount = get_monthly_detail(base_month, driver)

    mom_usage_amount, _ = get_monthly_detail(base_month - 1, driver)

    # transition to previous year to get year-on-year data
    transition_to_previous_year(driver)
    yoy_usage_amount, _ = get_monthly_detail(base_month, driver)

    message = '\n' + str(base_year) + '年' + str(base_month) + '月電気使用量\n\n'
    message += '当月使用量(kWh):' + usage_amount + '\n'
    message += '金額(円):' + billing_amount + '\n'
    message += '前月使用量(kWh):' + mom_usage_amount + '\n'
    message += '前年同月使用量(kWh):' + yoy_usage_amount

    # TODO delete
    print(message)

    return message
