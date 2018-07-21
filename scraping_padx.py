# import libraries
import urllib2
from bs4 import BeautifulSoup
import csv
import os
import time
import io
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

print "scraping start..."
# specify the url
monster_book = 'http://puzzledragonx.com/en/monsterbook.asp';

#query the website and return the html
page = urllib2.urlopen(monster_book)

# parse the html using beautifulsoup
soup = BeautifulSoup(page, 'html.parser')

print "getting monster names..."
all_monsters = []
# box_tags = soup.find_all('div', attrs={'class': 'indexframe'}, limit=20)
box_tags = soup.find_all('div', attrs={'class': 'indexframe'})
for tag in box_tags:
    monster_name = tag.a.img['title']
    href = tag.a['href']
    monster_id = href.split("=")[1]
    tup = (monster_id, monster_name)
    all_monsters.append(tup)

print "adding monsters to csv..."
os.remove('all_monsters.csv')
with open('all_monsters.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['monster_id', 'monster_name'])
    for row in all_monsters:
        writer.writerow(row)

print "finished"
