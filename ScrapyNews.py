# Import libraries
from bs4 import BeautifulSoup
import requests
import csv

# Set and connect to the URL you want to webscrape from
source = requests.get('https://exeleratingonline.nl/').text

# Parse HTML and save to BeautifulSoup object¶
soup = BeautifulSoup(source,"html.parser")

# initialize csv file
csv_file = open('c:/News_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'link'])

# To download the news data set, let's do a for loop through all div tags with specific class
for container in soup.find_all('div',attrs = {'class':'entry-content'}):
    #print(container)
    headline = container.h4.a.text
    print(headline)

    summary = container.p.text
    #print(summary)
    yt_link = container.h4.a['href']
    #print(yt_link)


    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()