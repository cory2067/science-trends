import os 
from time import sleep

f = set(os.listdir("/home/cor/Downloads"))
record = 400001

while True:
	sleep(0.25)
	files = set(os.listdir("/home/cor/Downloads"))
	added = files - f
	f = files
	for file in added:
		if '.bib' in file and not (".crdownload" in file):
			print("Found records " + str(record) + " - " + str(record + 500))
			os.rename("/home/cor/Downloads/" + file, "/home/cor/Desktop/records/" + str(record) + " - " + str(record + 499))
			record += 500
