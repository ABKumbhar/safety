from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from industry.models import *
# Create your views here.



#Getting news from Hindustan times

# ht_r = requests.get("https://www.osha.gov/dts/osta/oshasoft/")
# ht_soup = BeautifulSoup(ht_r.content, 'html5lib')
# ht_headings = ht_soup.find("div",{"class":"span7"})
# atag = ht_headings.findAll("a")
# ht_news = []
# ht_url = []

# for l in atag:
#     ht_url.append(l["href"])
#     try:
#         Industry.objects.get(name=(l.text))

#     except:    
#         Industry.objects.create(name = (l.text),url='https://www.osha.gov'+(l["href"]),adinfo="OSHA")

# ni_r = requests.get("https://www.cdc.gov/niosh/topics/industries.html")
# ni_soup = BeautifulSoup(ni_r.content, 'html5lib')
# ni_headings = ni_soup.find("ul",{"class":"block-list"})
# atagni = ni_headings.findAll("a")


# for l in atagni:
    
#     try:
#         Industry.objects.get(name=(l.text))

#     except:
#         Industry.objects.create(name = (l.text),url='https://www.cdc.gov'+(l["href"]),adinfo="NIOSH")

def index(req):
    return render(req, 'main/index.html',) 
    #{'toi_news':toi_news, 'ht_news': ht_news})