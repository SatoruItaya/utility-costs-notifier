from selenium.webdriver.common.by import By
import unicodedata
from time import sleep

import datetime


def get_suido_cost(driver, id, password):

    # login page
    driver.get('https://suidonet.waterworks.metro.tokyo.lg.jp/inet-service/members/login')

    login_id_element = driver.find_element(By.XPATH, '//*[@id="userName"]')
    login_id_element.send_keys(id)

    password_element = driver.find_element(By.XPATH, '//*[@id="password"]')
    password_element.send_keys(password)

    # top page
    submit_btn = driver.find_element(By.XPATH, '//*[@id="loginForm"]/table/tbody/tr[4]/td/input')
    submit_btn.click()

    detail_page_link = driver.find_element(By.XPATH, '//*[@id="main"]/div[1]/div[2]/div[1]/a').get_attribute('href')
    driver.get(detail_page_link)

    usage_term = driver.find_element(By.XPATH, '//*[@id="vi"]/table[6]/tbody/tr/td[4]').text.replace('（検針日）', '')
    billing_amount = driver.find_element(By.XPATH, '//*[@id="vi"]/table[9]/tbody/tr[5]/td[2]').text
    usage_amount = driver.find_element(By.XPATH, '//*[@id="vi"]/table[7]/tbody/tr[5]/td[3]/font/span[1]').text

    try:
        yoy = driver.find_element(By.XPATH, '//*[@id="vi"]/table[7]/tbody/tr[6]/td[3]/span').text
    except:
        yoy = '-'

    mom = driver.find_element(By.XPATH, '//*[@id="vi"]/table[7]/tbody/tr[5]/td[6]/span').text

    now = datetime.datetime.now()

    message = '\n' + str(now.year) + '年' + str(now.month - 1) + '~' + str(now.month) + ' 月 水道使用量・料金\n\n'
    message += '使用期間:' + usage_term + '\n'
    message += '請求額(円):' + unicodedata.normalize('NFKC', billing_amount) + '\n'
    message += '使用量(m^3):' + unicodedata.normalize('NFKC', usage_amount) + '\n'
    message += '前月使用量(m^3):' + mom + '\n'
    message += '前年同月使用量(m^3):' + yoy

    # TODO delete
    print(message)

    return message
