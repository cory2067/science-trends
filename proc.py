#Calculate graph data from the database

import sqlite3
import math

conn = sqlite3.connect("records2.db")
c = conn.cursor()

s_abs = True
s_key = False
abstract = "tokamak"
keyword = "tokamak"
if s_abs:
	query = "select year, cited from entries where abstract LIKE '%{}%'".format(abstract)
elif s_key:
	query = "select year, cited from entries where keyword LIKE '%{}%'".format(keyword)
else:
	query = "select year, cited from entries"
c.execute(query)

score = {}
num = 0
total = 0
for entry in c.fetchall():
	total += entry[1]
	num += 1
	if entry[0] in score:
		score[entry[0]] += 6 + 1*entry[1]
	else:
		score[entry[0]] = 6 + 1*entry[1]

print(total/num)
print("total: " + str(num))
out = ''
for year,pt in score.items():
	out += str(year) + "," + str(pt) +'\n'

with open("data.csv", 'w+') as f:
	f.write(out)

conn.close()

