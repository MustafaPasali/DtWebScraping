import json

def writeDataJson(data):
    """Verileri JSON Formatında Kaydet"""

    with open('Data.json', 'w', encoding='utf-8') as jsonFile:
        json.dump(data, jsonFile, indent=5, ensure_ascii=False)

def readDataJson():
    """Verileri JSON Dosyasından Oku"""

    with open('Data.json', 'r', encoding='utf-8') as jsonFile:
        fileData = json.load(jsonFile)

    return fileData