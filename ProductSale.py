# needed for forward reference of Sale in Product,
# since Sale is not yet defined.
from __future__ import annotations
from typing import List

# forward reference used for class Sale


class Product:
    __lastSale: Sale = None
    __remaining_inventory: int = 0

    def __init__(self, sale: Sale, number: int):
        self.__lastSale = sale
        self.__remaining_inventory = number
        print("Product initialized with: " +
              str(self.__remaining_inventory) + " " + "items")

    def setLastSale(self, lastSale: Sale):
        self.__lastSale = lastSale

    @property
    def getLastSale(self) -> Sale:
        return self.__lastSale

    def __getitem__(self, item):
        return self

    def getInventory(self) -> int:
        return self.__remaining_inventory

    def productSold(self, quantity: int):
        self.__remaining_inventory -= quantity

        # no forward reference needed since Product is defined


class Sale:
    __saleTimes = 0
    __productSold: List[Product] = None
    __saleNumber: int = 0

    def __init__(self, product: List[Product]):  # , saleNumber: int = 1):
        Sale.__saleTimes += 1
        self.__product = product
        self.__saleNumber = Sale.__saleTimes
        for index, product in enumerate(product):
            product[index].setLastSale(self)
            product[index].productSold(1)

    def setProductsSold(self, productSold: List[Product]):
        self.__productSold = productSold

    @property
    def getSaleNumber(self) -> int:
        return self.__saleNumber


productOne = Product(sale=None, number=10)
productTwo = Product(sale=None, number=9)

saleOne = Sale([productOne, productTwo])
saleTwo = Sale([productOne])
saleThree = Sale([productTwo])

print(f"{productOne.getLastSale.getSaleNumber}, {productTwo.getLastSale.getSaleNumber}")
print(f"{productOne.getInventory()}, {productTwo.getInventory()}")
