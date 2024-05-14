import os
import pyperclip
import re
import requests
import shutil
import time


input('Press Enter to paste the adress')
s = str(pyperclip.paste())
r = requests.get(s)
pattern = r'href=\"(.+?\.png|.+?\.jpg|.+?\.gif)\"'
time1 = time.strftime('%H-%M-%S', time.localtime())
path1 = os.path.join(os.getcwd(), time1)
os.mkdir(path1)
os.chdir(path1)
images = re.findall(pattern, r.text)
for image in images:
	r1 = requests.get('https://2ch.hk/' + image, stream=True)
	if r1.status_code == 200:
		(dirname, filename) = os.path.split(image)
		with open(filename, 'wb') as file:
			r1.raw.decode_content = True
			shutil.copyfileobj(r1.raw, file)
