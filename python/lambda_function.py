from selenium import webdriver
from selenium.webdriver.chrome import service as fs
import boto3
import tokyo_gas


def get_parameter(name):
    ssm_client = boto3.client('ssm')
    response = ssm_client.get_parameter(
        Name=name,
        WithDecryption=True
    )

    return response['Parameter']['Value']


# def lambda_handler(event, context):


def lambda_handler():

    chrome_service = fs.Service(executable_path='./chromedriver')
    driver = webdriver.Chrome(service=chrome_service)

    mail_address = get_parameter('mail-address')
    tokyo_gas_password = get_parameter('tokyo-gas-password')

    tokyo_gas.get_gas_cost(driver, mail_address, tokyo_gas_password)


if __name__ == "__main__":
    lambda_handler()
