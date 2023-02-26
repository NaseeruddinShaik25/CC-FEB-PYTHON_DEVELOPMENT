import pyshorteners
long_url = input("Enter the URL to shorten: ")
type_tiny = pyshorteners.Shortener()
short_url = type_tiny.tinyurl.short(long_url)
 
print("The Shortened URL is: " + short_url)

import pyshorteners
long_url = input("Enter the URL to shorten: ")
 
#TinyURL shortener service
type_tiny = pyshorteners.Shortener()
short_url = type_tiny.tinyurl.short(long_url)
 
print("The Shortened URL is: " + short_url)

type_bitly = pyshorteners.Shortener(api_key='01b6c587cskek4kdfijsjce4cf27ce2')
short_url = type_bitly.bitly.short('https://www.google.com')

import pyshorteners
long_url = input("Enter the URL to shorten: ")
 
#Bitly shortener service
type_bitly = pyshorteners.Shortener(api_key='01b6c587cskek4kdfijsjce4cf27ce2')
short_url = type_bitly.bitly.short('https://www.google.com')
 
print("The Shortened URL is: " + short_url)

expand_url = type_bitly.bitly.expand('https://bit.ly/TEST')
print (expand_url) # gives the url in expand or original form
 
count = type_bitly.bitly.total_clicks('https://bit.ly/TEST') #gives total no. of clicks.


import pyshorteners
s = pyshorteners.Shortener()
 
#Chilp.it
s.chilpit.short('http://www.google.com')    # gives output -> 'http://chilp.it/TEST'
s.chilpit.expand('http://chilp.it/TEST')
 
# Adf.ly
s = pyshorteners.Shortener(api_key='YOUR_KEY', user_id='USER_ID', domain='test.us', group_id=12, type='int')
s.adfly.short('http://www.google.com')    # gives output -> 'http://test.us/TEST'
 
#Git.io
s = pyshorteners.Shortener(code='12345')
s.gitio.short('https://github.com/TEST')     # gives output -> 'https://git.io/12345'
s.gitio.expand('https://git.io/12345')
 
#and many more services are supported

