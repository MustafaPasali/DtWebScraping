from bs4 import BeautifulSoup
import requests

def getData(url=""):
    """Haber Url Adreslerinden Verileri Topla"""

    # Seçilen Haberin Url Adresi

    urlResponse = requests.get(url)
    urlContent = str(urlResponse.content, 'utf-8')
    urlSoup = BeautifulSoup(urlContent, "lxml")

    # Tarih

    info = urlSoup.find("ul", id="nav-info")
    date = info.select_one('li > span').text

    # Başlık

    header = urlSoup.find("div", class_="panel-title").find("h1", class_="font-bold").text

    # Kategori

    categories = []
    for category in info.select("a", title_=""):
        categories.append(category.text)

    # Haber İçeriği

    text = urlSoup.find("div", id="detay-metin").text

    # Haber Görsel Url'leri

    body = urlSoup.find("div", class_="col-sm-8 panel-body pt-0 pl-0").find_all("img")

    images = []
    for image in body:
        images.append(image['src'])

    # Veri Liste Kaydı

    data = {'Url': url, 'Header': header, 'Categories': categories, 'Date': date, 'Text': text,
                           'Images': images}

    return data