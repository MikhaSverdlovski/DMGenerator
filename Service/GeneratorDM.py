import requests
from bs4 import BeautifulSoup
from pystrich.datamatrix import DataMatrixEncoder
import os


def generateDM(inputText):
    #Сначала принудительно удалим все файлы
    files_to_delete = os.listdir("static/Matrixes")
    for file_name in files_to_delete:
        file_path = os.path.join("static/Matrixes", file_name)
        os.remove(file_path)

    FNC1 = chr(231)  #'ç'
    file_names = []
    for counter, text in enumerate(inputText, start=0):
        data = FNC1 + text
        file_name = f"static/Matrixes/datamatrix_test{counter}.png"
        encoder = DataMatrixEncoder(data)
        file_names.append(file_name)
        encoder.save(file_name)
        # Получаем список имен файлов из папки
        file_names = os.listdir("static/Matrixes")
        # Создаем новый список, содержащий только имена файлов без пути
        file_names = [os.path.basename(file_name) for file_name in file_names]
        # Передаем список имен файлов в шаблон
    return file_names


#Извлекаем джитины из матрикса
def getGtins(text):
    gtins = []
    for text in text:
        gtin = text[2:16]
        gtins.append(gtin)
    return gtins









