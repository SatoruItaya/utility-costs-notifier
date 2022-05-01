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

LINE_NOTIFY_TOKEN_PARAMETER_NAME = os.environ["LINE_NOTIFY_TOKEN_PARAMETER_NAME"]
URL = "https://notify-api.line.me/api/notify"


def get_parameter(name):
    ssm_client = boto3.client('ssm')
    response = ssm_client.get_parameter(
        Name=name,
        WithDecryption=True
    )

    return response['Parameter']['Value']

# def lambda_handler():


def lambda_handler(event, context):

    options = Options()
    options.add_argument('--headless')
    options.add_argument("--no-sandbox")
    options.add_argument("--single-process")
    options.add_argument('--disable-dev-shm-usage')
    options.binary_location = "/opt/headless-chromium"

    print('--------configure chrome driver----------------')
    chrome_service = fs.Service(executable_path='./chromedriver')
    print('--------define driver----------------')
    driver = webdriver.Chrome(service=chrome_service, options=options)
    print('--------end define driver----------------')

    mail_address = get_parameter('mail-address')
    tokyo_gas_password = get_parameter('tokyo-gas-password')

    #message = tokyo_gas.get_gas_cost(driver, mail_address, tokyo_gas_password)

    tokyo_suido_id = get_parameter('tokyo-suido-id')
    tokyo_suido_pawssword = get_parameter('tokyo-suido-password')

    print('--------call suido----------------')
    message = tokyo_suido.get_suido_cost(driver, tokyo_suido_id, tokyo_suido_pawssword)

    next_power_id = get_parameter('next-power-id')
    next_power_password = get_parameter('next-power-password')

    #message = next_power.get_electricity_cost(driver, next_power_id, next_power_password)

    headers = {"Authorization": "Bearer %s" % get_parameter(LINE_NOTIFY_TOKEN_PARAMETER_NAME)}
    data = {'message': message}
    response = requests.post(URL, headers=headers, data=data)


if __name__ == "__main__":
    lambda_handler()
