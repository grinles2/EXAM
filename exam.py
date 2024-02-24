import requests
import lxml
from bs4 import BeautifulSoup

class Server:
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}  # Сессия
    session = requests.session()
    def __init__(self, url):
        self.url = url
        self.url = "https://kups.club/"
        # Сайт
    def get_response(self):
        self.response = self.session.get(self.url, headers=self.header)
        return self.response # вернём значение


    def get_info(self):
        if self.response.status_code == 200:
            soup = BeautifulSoup(self.response.text, "lxml")
            allProduct = soup.find("div", class_="row mt-4")  # div со всеми карточками
            products = allProduct.find_all("div",class_="col-lg-4 col-md-4 col-sm-6 portfolio-item") #Товар и его инфа

    def get_answer(self):
        product = self.get_info() # обращение к get_info за картoчками
        for i in product:
            try:
                title = product[i].find("div", class_="card-title").text.strip()  # имя товара
                price = product[i].find("div", class_="card-text").text.strip()  # Цена
                # print(title, price) выводим
                with open("products.txt", "a", encoding="UTF-8") as file:
                    file.write(f"{title} --->>> {price}\n")
            except:
                print("Гуляй Вася")


