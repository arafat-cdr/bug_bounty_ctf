import requests

url = 'https://imgs.xkcd.com/comics/python.png'

r = requests.get( url )

with open('my_img.png', 'wb') as f: # W = Writing; B = Binary Mode
	f.write(r.content)

if(r.ok):
	print('---Img Downloaded Successfully---')
else:
	print('--Server Error--')