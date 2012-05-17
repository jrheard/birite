import datetime
import urllib2

from flask import Flask
from pyquery import PyQuery as pq


app = Flask(__name__)

@app.route('/')
def soft_serve():
	html = pq(urllib2.urlopen('http://www.biritecreamery.com/icrecream').read())
	days = html("#primary .column-right ul")[3].findall("li")
	flavors = days[datetime.date.today().weekday()].text_coontent
	return flavors.split(': ')[1]


if __name__ == '__main__':
	app.run()
