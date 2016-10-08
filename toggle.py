import sys
import requests

def login(username, password):
	credentials = {
		'username': username,
		'password': password,
	}

	resp = requests.post('https://wifiplugapi.co.uk:3081/zcloud/api/user_login', data=credentials)
	token = resp.json()['token']
	print('login success! token: %s' % token)
	return token

def getDevices(token):
	print('blah')	

if __name__ == "__main__":
	username = sys.argv[1]
	password = sys.argv[2]
	token = login(username, password)
