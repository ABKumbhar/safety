from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from industry.models import *
# Create your views here.
toi_r = requests.get("https://timesofindia.indiatimes.com/briefs")
toi_soup = BeautifulSoup(toi_r.content, 'html5lib')

toi_headings = toi_soup.find_all('h2')

toi_headings = toi_headings[0:-13] # removing footers

toi_news = []

for th in toi_headings:
    toi_news.append(th.text)



#Getting news from Hindustan times

ht_r = requests.get("https://www.osha.gov/dts/osta/oshasoft/")
ht_soup = BeautifulSoup(ht_r.content, 'html5lib')
ht_headings = ht_soup.find("div",{"class":"span7"})
atag = ht_headings.findAll("a")
ht_news = []
ht_url = []

for l in atag:
    try:
        Industry.objects.get(name=(l.text))

    except:    
        Industry.objects.create(name = (l.text),url='https://www.osha.gov'+(l["href"]))


def index(req):
    return render(req, 'main/index.html', {'toi_news':toi_news, 'ht_news': ht_news})