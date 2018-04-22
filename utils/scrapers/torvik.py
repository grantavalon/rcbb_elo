import re
import requests
import pandas as pd
from bs4 import BeautifulSoup


def main(year):
	url = 'http://barttorvik.com/trank.php?year={}'.format(year)
	html = requests.get(url).content
	soup = BeautifulSoup(html, 'lxml')
	print soup.findall('table')


if __name__ == "__main__":
	main(year='2019')