import pprint
import bsg_restapi as api

# from examples.settings import API_KEY
API_KEY = 'live_fmUXxusYDiufPlwoZjLJ'

client = api.SMSAPI(config={'api_key': API_KEY})
result = client.send(message=api.SMSMessage(body='Hello from bsg'), recipients=api.Recipient('447920498128'))
print('Result of SMS sending:\n{}'.format(pprint.pformat(result)))
# getting status of SMS
# status = client.get_status(result['reference'])
# print('Current SMS status result for reference {}: \n{}'.format(result['reference'], pprint.pformat(status, indent=4)))