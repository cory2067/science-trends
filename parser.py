#Construct sqlite database from bibtex

import sqlite3
import os
import sys
import bibtexparser

conn = sqlite3.connect('records3.db')
c = conn.cursor()

files = os.listdir("/home/cor/Desktop/science-trends/records")
for name in files:
	print(name)
	with open("records/" + name) as f:
		try:	
			db = bibtexparser.load(f)
		except:
			print("Something exploded")
			continue
	
	for entry in db.entries:
		#garbage error handling
		issn =''
		try:
			issn = entry['issn'].replace('-', '')
		except KeyError:
			print("no issn")
		
		doi =''
		try:
			doi = entry['doi']
		except KeyError:
			print("no doi")
				
		title =''
		try:
			title = entry['title']
		except KeyError:
			print("no title")

		cited = 0
		try:
			cited = int(entry['times-cited'])
		except KeyError:
			print("no cites")

		abstract =''
		try:
			abstract = entry['abstract']
		except KeyError:
			print("no abstract")

		journal =''
		try:
			journal = entry['journal']
		except KeyError:
			print("no journal")

		keywords = ''
		try:
			keywords = entry['keyword']
		except KeyError:
			print("no keywords")
		try:
			keywords = entry['keywords-plus']
		except KeyError:
			print("no plus keywords")
	
		vals = (entry['ID'][4:], title, int(entry['year']), doi, issn, cited, journal, keywords, abstract)
		
		c.execute("INSERT INTO entries VALUES (?,?,?,?,?,?,?,?,?)", vals)
	conn.commit()
conn.close()
