#!/Users/liamward/.rye/shims/python

import json
import csv

input = 'chacon.json'
output = 'chacon.csv'

with open('chacon.json', 'r') as file:
   data = json.load(file)

with open ('chacon.csv', 'a', newline='') as csvfile:
   csv_writer = csv.writer(csvfile)

if csvfile.tell() == 0:
   csv_writer.writerow(['name','html_url','updated_at','visibility'])

for i, item in enumerate(data[0:5]):
	name = item.get('name', '')
	html_url = item.get('html_url', '')
	updated_at = item.get('updated_at', '')
	visibility = item.get('visibility', '')
	csv_writer.writerow([name, html_url, updated_at, visibility])

print(out)
