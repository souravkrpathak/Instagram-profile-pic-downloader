import urllib.request, urllib.parse, urllib.error
import requests 
from bs4 import BeautifulSoup 
import os


insta_username = input("Enter username: ")
url = "https://www.instagram.com/" + insta_username

try:
	html = urllib.request.urlopen(url).read()


	soup = BeautifulSoup(html, features = 'lxml')

	img_url = soup.find("meta", attrs= {'property':'og:image'})
	img_url = img_url['content']


	print("\n \n downloading..........") 
	urllib.request.urlretrieve(img_url, insta_username + ".jpg")


	print("\ndownloading completed ..............")
except urllib.error.HTTPError:
	print("Username not found !")


