import glob
import shutil
from selenium import webdriver
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.chrome.options import Options
import boto3
import sys
import os
import requests
import tokyo_gas
import tokyo_suido
import next_power
import chromedriver_binary
import datetime

LINE_NOTIFY_TOKEN_PARAMETER_NAME = os.environ["LINE_NOTIFY_TOKEN_PARAMETER_NAME"]
URL = "https://notify-api.line.me/api/notify"


def get_parameter(name):
    ssm_client = boto3.client('ssm')
    response = ssm_client.get_parameter(
        Name=name,
        WithDecryption=True
    )

    return response['Parameter']['Value']


def lambda_handler(event, context):

    now = datetime.datetime.now()

    options = Options()
    options.add_argument('--headless')
    options.add_argument("--no-sandbox")
    options.add_argument("--single-process")
    options.add_argument('--disable-dev-shm-usage')
    options.binary_location = "/opt/headless-chromium"
    options.add_argument("--disable-gpu")
    options.add_argument("--hide-scrollbars")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--window-size=880x996")
    options.add_experimental_option("w3c", True)

    driver = webdriver.Chrome('./chromedriver', chrome_options=options)

    message = ''

    if now.day == 1:
        mail_address = get_parameter('mail-address')
        tokyo_gas_password = get_parameter('tokyo-gas-password')
        message = tokyo_gas.get_gas_cost(driver, mail_address, tokyo_gas_password)

    if now.day == 20 and now.month % 2 != 0:
        tokyo_suido_id = get_parameter('tokyo-suido-id')
        tokyo_suido_pawssword = get_parameter('tokyo-suido-password')
        message = tokyo_suido.get_suido_cost(driver, tokyo_suido_id, tokyo_suido_pawssword)

    # next_power_id = get_parameter('next-power-id')
    # next_power_password = get_parameter('next-power-password')
    # message = next_power.get_electricity_cost(driver, next_power_id, next_power_password)

    if message != '':
        headers = {"Authorization": "Bearer %s" % get_parameter(LINE_NOTIFY_TOKEN_PARAMETER_NAME)}
        data = {'message': message}
        response = requests.post(URL, headers=headers, data=data)


if __name__ == "__main__":
    lambda_handler()
