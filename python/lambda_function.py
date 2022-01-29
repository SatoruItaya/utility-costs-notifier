from selenium import webdriver
import os
from time import sleep

# def lambda_handler(event, context):


def lambda_handler():

    driver = webdriver.Chrome('./chromedriver')

    # login page
    driver.get('https://members.tokyo-gas.co.jp/')
    login_page_link = driver.find_element_by_class_name('mtg-button-cta').get_attribute('href')
    driver.get(login_page_link)

    login_id = driver.find_element_by_xpath('//input[@name="loginId"]')
    login_id.send_keys(os.environ['GASS_ID'])

    password = driver.find_element_by_xpath('//input[@name="password"]')
    password.send_keys(os.environ['GASS_PASSWORD'])

    # top page
    submit_btn = driver.find_element_by_id('submit-btn')
    submit_btn.click()

    sleep(5)

    # total page
    total_page_link = driver.find_element_by_class_name('mtg-content-number-link').get_attribute('href')
    driver.get(total_page_link)

    sleep(5)

    # detail page
    detail_page_link = driver.find_element_by_class_name('mtg-button-link').get_attribute('href')
    driver.get(detail_page_link)

    sleep(5)


if __name__ == "__main__":
    lambda_handler()
