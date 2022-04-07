class record:
    def __init__(self, name, buy, sell):
        self.buy = buy
        self.sell = sell
        self.name = name

    def __str__(self):
        print(self.name)
        print(self.sell)

    def recordData(self, profit):
        file1 = open('profits.txt', 'a')
        file1.write(f"{self.name}: {profit} \n")
        file1.close()
