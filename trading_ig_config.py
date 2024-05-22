import configparser

# Read credentials from the configuration file
config = configparser.ConfigParser()
config.read('ig.cfg')

username = config.get('demo', 'username')
password = config.get('demo', 'password')
api_key = config.get('demo', 'api_key')
acc_type = config.get('demo', 'api_key')
acc_number = config.get('demo', 'api_key')

# username = config.get('live', 'username')
# password = config.get('live', 'password')
# api_key = config.get('live', 'api_key')
# acc_type = config.get('live', 'api_key')
# acc_number = config.get('live', 'api_key')

class config(object):
    username = "your_username"
    password = "your_password"
    api_key = "your_api_key"
    acc_type = "DEMO"
    acc_number = "your_account_number"