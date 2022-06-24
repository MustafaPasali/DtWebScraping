from bs4 import BeautifulSoup
import requests
import datetime

def getUrls():

    sitemapUrl = "https://duzcetv.com/sitemap2.asp"
    response = requests.get(sitemapUrl)
    urlContent = str(response.content, 'utf-8')
    soup = BeautifulSoup(urlContent, "lxml")

    # Haber Url Adresleri

    urls = []
    for selectedUrl in soup.select('url > loc'):
        url = selectedUrl.text.replace("\r", "").replace("\n", "")

        urlResponse = requests.get(url)
        urlContent = str(urlResponse.content, 'utf-8')
        urlSoup = BeautifulSoup(urlContent, "lxml")

        # Tarih

        info = urlSoup.find("ul", id="nav-info")
        date = info.select_one('li > span').text
        urlDateTime = datetime.datetime.strptime(date, '%d.%m.%Y - %H:%M')

        today = datetime.date.today()

        # Son 24 Saatte Eklenmiş Haber Urlleri

        if today == urlDateTime.date():

            urls.append(url)

        else:
            break

    return urls