import time
from time import sleep
from threading import Thread

class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power


    def run(self):
        day=0
        enimies = 100
        print(f'{self.name}, на нас напали!')
        while enimies > 0 :

            day = day+1
            enimies = enimies - self.power
            sleep(1)
            print(f'{self.name}, сражается {day} день(дня)..., осталось {enimies} воинов')
        print(f'Sir {self.name} одержал победу спустя {day} дней(дня)!')

# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков и остановка текущего

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

# Вывод строки об окончании сражения
print('Все битвы закончились!')
