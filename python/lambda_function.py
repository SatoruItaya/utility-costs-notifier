from selenium import webdriver
from selenium.webdriver.chrome import service as fs
import boto3
import tokyo_gas
import tokyo_suido
import next_power


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

    #tokyo_gas.get_gas_cost(driver, mail_address, tokyo_gas_password)

    tokyo_suido_id = get_parameter('tokyo-suido-id')
    tokyo_suido_pawssword = get_parameter('tokyo-suido-password')

    #tokyo_suido.get_suido_cost(driver, tokyo_suido_id, tokyo_suido_pawssword)

    next_power_id = get_parameter('next-power-id')
    next_power_password = get_parameter('next-power-password')

    next_power.get_electricity_cost(driver, next_power_id, next_power_password)


if __name__ == "__main__":
    lambda_handler()
