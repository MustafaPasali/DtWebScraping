import datetime

import constants
import scrapper
import time
import mongoDB

allData = []
savedUrls = []

while True:
    tdy = str(datetime.date.today().strftime('%d.%m.%Y'))
    urls = scrapper.getUrls()
    print(tdy, "Tarihli Haber Urlleri Alındı")

    if urls != []:
        for url in urls:
            if savedUrls.count(url) == 0:
                data = scrapper.getData(url)
                allData.append(data)
                savedUrls.append(url)

        scrapper.writeDataJson(allData)
        jsonData = scrapper.readDataJson()
        print("Kayıtlı Haber Verisi Sayısı (JSON):", len(jsonData))

        # mongoDB
        col = mongoDB.mongodb()
        col.insert_many(jsonData)
        print("Kayıtlı Haber Verisi Sayısı (Database):", col.count_documents({}))

    else:
        print(tdy, "Tarihinde Eklenen Bir Haber Bulunamadı")

    print(constants.SLEEP_TIME, "Saniye Uykuda")
    time.sleep(constants.SLEEP_TIME)


