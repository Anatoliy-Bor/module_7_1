from read_write import *
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category
    def __str__(self):
        return  f' название : {self.name}  вес : {self.weight} категория : {self.category}'
class Shop(Product):
    def __init__(self, name, weight, category, __file_name = 'products.txt'):
        super().__init__(name, weight, category)
        self.__file_name = __file_name
    def get_products(self):
        return reading(self.__file_name)
    def add(self, *products):
        for i in products:
            r = str(i)
            f = reading(self.__file_name)
            print(f)
            if r in f:
                print (f'Продукт , {self.name} уже есть в магазине' )
            else:
                appending(self.__file_name, f'\n{r}')

s1 = Shop('',0 , '')
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
