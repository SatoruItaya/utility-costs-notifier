from selenium.webdriver.common.by import By
from time import sleep


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

    usage_term = driver.find_element(By.XPATH, '//*[@id="vi"]/table[6]/tbody/tr/td[2]').text
    # TODO 半角にする
    billing_amount = driver.find_element(By.XPATH, '//*[@id="vi"]/table[9]/tbody/tr[5]/td[2]').text
    # TODO 半角にする
    usage_amount = driver.find_element(By.XPATH, '//*[@id="vi"]/table[7]/tbody/tr[5]/td[3]/font/span[1]').text

    try:
        yoy = driver.find_element(By.XPATH, '//*[@id="vi"]/table[7]/tbody/tr[6]/td[3]/span').text
    except:
        yoy = None

    mom = driver.find_element(By.XPATH, '//*[@id="vi"]/table[7]/tbody/tr[5]/td[6]/span').text

    print('使用期間:' + usage_term)
    print('請求額:' + billing_amount)
    print('使用量:' + usage_amount + 'm^3')

    if yoy is not None:
        print('前年同期:' + yoy + 'm^3')

    print('前回:' + mom + 'm^3')

    sleep(5)
