# class Goods():
#     def __init__(self,unit_price,weight):
#         self.unit_price = unit_price
#         self.weight = weight
#
#     @property
#     def price(self):
#         return self.unit_price * self.weight
#
#
# lemons = Goods(7,4)
# lemons.price


# class Lemons():
#     def __init__(self,unit_price=7):
#         self.unit_price = unit_price
#
#     def get_unit_price(self):
#         return self.unit_price
#
#     def set_unit_price(self,new_unit_price):
#         self.unit_price = new_unit_price
#
#     def del_unit_price(self):
#         del self.unit_price
#
#     x = property(get_unit_price,set_unit_price,del_unit_price)
#
#
# l = Lemons()
#
# l.x



# class Watermelon():
#     def __init__(self,price):
#         self._price = price
#
#     def get_price(self):
#         return self._price
#
#     def set_price(self,new_price):
#         if new_price > 0:
#             self._price = new_price
#         else:
#             raise 'error:价格必须大于零'


class Watermelon():
    def __init__(self,price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,new_price):
        if new_price > 0:
            self._price = new_price
        else:
            raise 'error:价格必须大于零'
