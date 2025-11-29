class Customer:
    def __init__(self, name):
        self.name = name
        # Добавьте сюда атрибут "скидка" со значением по умолчанию 10.
        self.__discount = 10  # приватный атрибут со значением по умолчанию 10

    # Реализуйте методы get_price() и set_discount().
    def get_price(self, price):

        discounted_price = price * (100 - self.__discount) / 100
        return round(discounted_price, 2)
    
    def set_discount(self, new_discount):

        if new_discount > 80:
            self.__discount = 80
        else:
            self.__discount = new_discount


customer = Customer("Иван Иванович")
print(customer.get_price(100))  # 90.0
customer.set_discount(20)
print(customer.get_price(100))  # 80.0