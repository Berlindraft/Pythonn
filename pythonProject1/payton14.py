# pillow library caught my attention that allows to navigate in image files
import re

email = input('Enter email: ').strip()

username, domain = email.split("@")

if re.search("@", email):
    print('valid')
else:
    print('invalid')

'''
HAGBONG SA REGEX
HAGBONG SA REGEX
HAGBONG SA REGEX
HAGBONG SA REGEX
HAGBONG SA REGEX
HAGBONG SA REGEX
HAGBONG SA REGEX
HAGBONG SA REGEX
HAGBONG SA REGEX
HAGBONG SA REGEX
'''