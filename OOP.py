# №1
# Клиент приходит в кондитерскую. Он хочет приобрести один или несколько видов продукции, а также узнать её состав.
# Реализуйте кондитерскую. У вас есть словарь, где ключ – название продукции (торт, пирожное, маффин и т.д.).
# Значение – список, который содержит состав, цену (за 100гр) и кол-во (в граммах). Предложите выбор:
# 1. Если человек хочет посмотреть описание: название – описание 2. Если человек хочет посмотреть цену: название – цена.
# 3. Если человек хочет посмотреть количество: название – количество.
# 4. Всю информацию.
# 5. Приступить к покупке: С клавиатуры вводите название торта и его кол-во. n – выход из программы.
# Посчитать цену выбранных товаров и сколько товаров осталось в изначальном списке 6. До свидания.
#
# №2
# Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как в первом списке, так и во втором.
#
# №3
# В текстовый файл построчно записаны фамилия и имя учащихся класса и его оценка за контрольную.
# Вывести на экран всех учащихся, чья оценка меньше 3 баллов и посчитать средний балл по классу.

class Human:
    default_name = None
    default_age = 0

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.house = None
        self.money = 0

    def info(self):
        print(f"name: {self.name}")
        print(f"age: {self.age}")
        print(f"house: {self.house}")
        print(f"money: {self.money}")

    @staticmethod
    def default_info():
        print(f"Default name: {Human.default_name}")
        print(f"Default age: {Human.default_age}")

    def earn_money(self, amount):
        self.money += amount
        print(f"Пополнение: {amount}, Ваш баланс: {self.money}")

    def make_deal(self, house, price):
        self.money -= price
        self.house = house

    def buy_house(self, house, discount):
        price = house.final_price(discount)
        if price > self.money:
            print("Недостаточно средств ")
        else:
            self.make_deal(house, price)


class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        final_price = self._price * (100 - discount) / 100
        return final_price


class Small_house(House):
    default_area = 40

    def __init__(self, price):
        super().__init__(Small_house.default_area, price)


if __name__ == '__main__':
    Human.default_info()
    Bob = Human("Bob", 20)
    Bob.earn_money(20000)
    Bob.earn_money(5000)

    green=Small_house(30000)
    Bob.buy_house(green,20)
    Bob.info()