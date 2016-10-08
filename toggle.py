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
	print('attempting to get list of devices...')
	resp = requests.get('https://wifiplugapi.co.uk:3081/zcloud/api/device_query?token=%s' % token)
	deviceIds = []
	for device in resp.json()['deviceList']:
		id = device['id']
		print('found device - id=%s' % id)
		deviceIds.append(id)
	
	return deviceIds

def deviceControl(token, device, status):
	print('turning the device %s' % status)
	payload = {
		'token': token,
		'device_id': device,
		'on': status,
	}
	resp = requests.post('https://wifiplugapi.co.uk:3081/zcloud/api/device_control', data=payload)
	print(resp.json())

if __name__ == "__main__":
	username = sys.argv[1]
	password = sys.argv[2]
	status = sys.argv[3]
	token = login(username, password)
	devices = getDevices(token)
	for device in devices:
		deviceControl(token, device, status)
