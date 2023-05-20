import random
import logging
logging.basicConfig(level=logging.DEBUG,
filename="logs.log", filemode="a",
format="We have next logging message: "
"%(asctime)s:%(levelname)s-%(message)s"
)

class restaurant:

    def __init__(self, name="restaurant" ):
        self.name = name
        self.money = 1000
        self.ingredients = 100
        self.popularity = 50
        self.job = True
        self.close = False
        self.alive = True
    def clients(self):
        if self.job:
            self.money += 10
            self.ingredients -= 15
            self.popularity += 5
            print("Обслужил клиента")
            logging.info("Когда ты готовишь ты получаешь деньги популярность но  теряешь ингридиенты")
        else:
            self.popularity -=10
            print(" НЕ Обслужил клиента")


    def clining(self):
        self.money -=5
        self.popularity +=8
        print("Решил помыть пол")
        logging.info("Когда ты юбираешься ты теряешь деньги на получаешь популярность")

    def money(self,):
        if self.money < 10:
            print("bankrupt")
            self.close = True

    def shoping(self):
        if self.ingredients < 20:
            self.money -=50
            self.ingredients += 50
            print("Схожу в магазин")
            logging.info("Когда ты скупаешься ты теряешь деньги но получаешь ингридиенты")

    def is_alive(self):
        if self.money < -10:
            print("bankrupt")
            self.alive = False
        elif self.popularity <= 20:
            print("abandoned")
            self.alive = False
        elif self.ingredients <= 5:
            print("No ingredients ")
            self.alive = False

    def end_of_day(self):
        print(f"Money = {self.money}")
        print(f"ingredients = {self.ingredients}")
        print(f"popularity = {round(self.popularity, 2)}")
    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.clients()
        elif live_cube == 2:
             self.clining()
        elif live_cube == 3:
             self.shoping()


        self.is_alive()
        self.end_of_day()

restauran = restaurant(name="restauran")

for day in range(365):
    # if restauran.close == True:
    if restauran.alive == False:
        break
    restauran.live(day)
