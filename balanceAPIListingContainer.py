import requests,messagebird
import clicksend_client
from clicksend_client import SmsMessage
from clicksend_client.rest import ApiException


def messageBirdApiBalanceGateway(credentials):
    balance = ''
    try:
        client = messagebird.Client(credentials['access_key'])
        balance = client.balance()
        balance = str(balance.amount)  + ' ' + str(balance.type)
    except:
        balance =  'Not Available'
    return balance


def twilioApiBalanceGateway(credentials):  
    balance = ''
    try:
        from twilio.rest import Client 
        account_sid =  credentials['account_sid']
        auth_token =  credentials['auth_token']
        balance = Client(account_sid, auth_token).balance.fetch()
        balance = f'{balance.balance} {balance.currency}'
        print(balance)
    except:
        balance =  'Not Available'
    return balance


def d7networksApiBalanceGateway(credentials): 
    balance = ''
    try:
        url = f'https://http-api.d7networks.com/balance?username={credentials["username"]}&password={credentials["password"]}'
        balance = requests.get(url).json()
        balance = f'{balance["balance"]} {balance["sms_count"]}'
    except:
        balance =  'Not Available'
    return balance