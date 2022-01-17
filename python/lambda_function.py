from selenium import webdriver
import os
from time import sleep

# def lambda_handler(event, context):


def lambda_handler():

    driver = webdriver.Chrome('./chromedriver')

    driver.get('https://members.tokyo-gas.co.jp/')

    login_button = driver.find_element_by_link_text('ログイン')
    login_button.click()

    login_id = driver.find_element_by_xpath('//input[@name="loginId"]')
    login_id.send_keys(os.environ['GASS_ID'])

    password = driver.find_element_by_xpath('//input[@name="password"]')
    password.send_keys(os.environ['GASS_PASSWORD'])

    submit_btn = driver.find_element_by_id('submit-btn')
    submit_btn.click()

    sleep(10)
    # search_bar = driver.find_element_by_name("q")
    # search_bar.send_keys("python")

    # search_bar.submit()


if __name__ == "__main__":
    lambda_handler()
