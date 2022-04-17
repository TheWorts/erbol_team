# # 3
# Students room:
# Реализуйте студенческую комнату с помощью ООП:

# Copy:

# Steve = Student("Steven Schultz", 23, "English")
# Johnny = Student("Jonathan Rosenberg", 24, "Biology")
# Penny = Student("Penelope Meramveliotakis", 21, "Physics")
# print(Steve)
# <name: Steven Schultz, age: 23, major: English>
# print(Johnny)
# <name: Jonathan Rosenberg, age: 24, major: Biology>

# class Student:
#     def __init__(self,name,age,major):
#         self.name = name
#         self.age = age
#         self.major = major
# Steve = Student("Steven Schultz", 23, "English")
# Johnny = Student("Jonathan Rosenberg", 24, "Biology")
# Penny = Student("Penelope Meramveliotakis", 21, "Physics")
# print(Steve.__dict__)
# print(Johnny.__dict__)
# print(Penny.__dict__)

 # 2
# Furniture:
# Тип дома, общая площадь и перечень наименований мебели В новом доме совсем нет мебели.
# Мебель имеет название и площадь, из которых Спальня:
# 4 квадратных метра Гардероб: 2 квадратных метра Стол: 1,5 квадратных метра.
# Добавьте в дом три вышеупомянутых предмета мебели.
# При печати дома требуются следующие данные:
# тип дома, общая площадь, оставшаяся площадь, список названий мебели.
# class House:
#     def __init__(self,type_of_house,area):
#         self.type_of_house = type_of_house
#         self.area = area
#         self.furniture = dict()
#         self.ostatok = area
#     def add_furniture(self,name,area):
#         self.furniture[name] = area
#         self.ostatok-=area
# myHouse = House('elite',100)
# myHouse.add_furniture('спальня',4)
# myHouse.add_furniture("гардероб",2)
# myHouse.add_furniture("стол",1.5)
# print(myHouse.ostatok)
# print(myHouse.__dict__)

#1
#AK-47:
# У солдата Райана есть АК-47
# Солдаты могут стрелять («тиги-тигитиш»).
# Пистолеты могут стрелять пулями.
# Пистолеты могут начинать патроны - увеличивайте количество патронов (перезаряжает)
# Создайте класс Act_of_Shooting, который унаследует от класса Soldier класс Guns.
# Где солдат будет стрелять из пушки и перезаряжаться, и стрелять еще раз.





# class Soldier:
#     def __init__(self, name):
#         self.name = name
#         self.gun =  None
#     def fire(self):
#         if self.gun == None:
#             print('не имеет оружие', self.name)
#         print('тиги-тигитиш!!!',self.name)
#         self.gun.add_puli(50)
#         self.gun.strelyat()
#
# class Guns:
#     def __init__(self, model):
#         self.model = model
#         self.puli = 0
#
#     def add_puli(self, count):
#         self.puli += count
#
#     def strelyat(self):
#         if self.puli <= 0:
#             print('не имеет патронов', self.model)
#             return
#         self.puli -= 1
#         print(self.model, self.puli)
#
#
#
# ak = Guns('AK-47')
# ryan = Soldier('Ryan')
# ryan.gun = ak
# ryan.fire()


# # 6
# Спарсить сайт лалафо с недвижимостью (аренда посуточно)
# https://lalafo.kg/kyrgyzstan/nedvizhimost
# Название
# Цену
# Фото
# Адрес
# Дату
# Ссылку на пост

# from bs4 import BeautifulSoup
# from selenium.webdriver.common.keys import Keys
# import csv
# import urllib3
#
# urllib3.disable_warnings()
# from selenium import webdriver
# import time
# from selenium.webdriver.common.action_chains import ActionChains
#
#
# def get_data(URL):
#     driver = webdriver.Firefox()
#     driver.get(URL)
#     time.sleep(3)
#
#     count = 40
#     while count != 0:
#         actions = ActionChains(driver)
#         actions.send_keys(Keys.PAGE_DOWN).perform()
#         time.sleep(1)
#         count -= 1
#
#     with open('index.html', 'w') as f:
#         f.write(driver.page_source)
#
#
# with open('index.html', 'r') as file:
#     page = file.read()
#
# soup = BeautifulSoup(page, 'html.parser')
#
# all_elements = soup.find_all('div', 'AdTileHorizontal')
# apartaments = []
# for e in all_elements:
#     name = e.find('a', class_="AdTileHorizontalTitle").get_text(strip=True)
#     price = e.find('p', class_="AdTileHorizontalPrice").get_text(strip=True)
#     city = e.find('p', class_="city-wrap").get_text(strip=True)
#     data = e.find("span", class_="AdTileHorizontalDate").get_text(strip=True)
#     image = e.find("img", class_='AdTileImage').get('src')
#     link = e.find('a', class_="AdTileHorizontalTitle").get('href')
#     l = 'https://lalafo.kg'
#     apartaments.append({
#         'name': name,
#         'price': price,
#         'city': city,
#         'data': data,
#         'image': image,
#         'link': l + link
#     })
#
# columns = ['name', 'price', 'city', 'data', 'image', 'link']
# with open('lalafo.csv', 'w') as f:
#     writer = csv.DictWriter(f, fieldnames=columns)
#     writer.writeheader()
#     writer.writerows(apartaments)
#     print('files are written succesfully!!!')
#
#
# def main():
#     get_data("https://lalafo.kg/kyrgyzstan/kvartiry/arenda-kvartir/posutochnaya-arenda-kvartir")
#
#
# main()

# # 5
# Deck of Cards:
# Создайте класс колоды карт. Внутри колода карт должна использовать другой класс - класс карт. Ваши требования:
# Класс Deck должен иметь метод раздачи для раздачи одной карты из колоды.
# После раздачи карты она удаляется из колоды.
# Должен быть метод «смешивания», который проверяет, что в колоде есть все 52 карты, а затем меняет их случайным образом.
# Класс должен иметь масть (червы, бубны, трефы, пики) и ценность карты (A, 2,3,4,5,6,7,8,9,10, J, Q, K)
# ПРИМЕЧАНИЕ: используйте случайное перемешивание

# Copy
# from random import shuffle
# from random import shuffle
#
# class card_deck:
#      def init(self, rank, suite, card):
#
#
#         self.ran= rank
#         self.suite = suite
#
# def ranks(self):
#          return self.rank
# def suites(self):
#          return self.suite
# def cards(self,card):
#          suit_name= ['The suit of Spades','The suit of Hearts', 'The suit of Diamonds','Clubs']
#          rank_name=['Ace','2','3','4','5','6','7','8','9','10','J','Q','K']
#
#
# def value(self):
#          if self.rank == 'A':
#              return 1
#          elif self.rank == 'J':
#              return 11
#          elif self.rank == 'Q':
#              return 12
#          elif self.rank == 'K':
#              return 13
# def shffule(self):
#          shuffle(self.cards)
# def remove(self,card):
#          self.cards.remove(card)
#
#
# def cardremaining(self):
#         self.suite-self.rank
#
#
#
#
# def main():
#      try:
#          deck=[]
#          for i in ['червы','бубны', 'трефы','пики']:
#           for c in ['Ace','2','3','4','5','6','7','8','9','10','J','Q','K']:
#                  deck.append((c, i))
#          shuffle(deck)
#
#          hand = []
#          user =eval(input('Enter a number of cards: 1-7 '))
#          print()
#          while user <1 or user >7:
#              print ("Only a number between 1-7:")
#              return main()
#
#          for i in range(user):
#             hand.append(deck[i])
#          print (hand)
#      except ValueError:
#          print("Only numbers")
#          main()
#
# if name == 'main':
#     main()