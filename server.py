from flask import Flask
from flask import render_template
import sqlite3
import math
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/view")
def view():
	abstract = request.args.get('abstract', '')
	keyword = request.args.get('keyword', '')
	conn = sqlite3.connect("records.db")
	c = conn.cursor()

	if abstract != '':
		query = "select year, cited from entries where abstract like '%{}%'".format(abstract)
	elif keyword != '':
		query = "select year, cited from entries where keyword like '%{}%'".format(keyword)
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
	return render_template("graphs.html", data=out, query=query, total=num)

if __name__ == "__main__":
	app.run()
