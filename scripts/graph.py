#!/usr/bin/python
import cgi
import sqlite3
import math

print "Content-type: text/html\n"

conn = sqlite3.connect("records.db")
c = conn.cursor()

args = cgi.FieldStorage()

if 'abstract' in args and args['abstract'].value != '':
	query = "select year, cited from entries where abstract like '%{}%'".format(args['abstract'].value)
elif 'keyword' in args and args['keyword'].value != '':
	query = "select year, cited from entries where keyword like '%{}%'".format(args['keyword'].value)
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

out = ''

for year in sorted(score):
	out += '{x:' + str(year) + ", y:" + str(score[year]) +'},'
out = out[:-1]

with open("graph.html.py", "r") as f:
	data = f.read()

print data.format(data=out,query=query,total=num)
