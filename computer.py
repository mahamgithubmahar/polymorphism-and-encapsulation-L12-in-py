class computer:
    def __init__(self):
        self.__maxprice=900
    def sell(self):
        print("Selling price is {}".format(self.__maxprice))
    def setmaxprice(self,price):
        self.__maxprice=price

ob1=computer()
ob1.sell()
ob1.__maxprice=1000
ob1.sell()
ob1.setmaxprice(1000)
ob1.sell()