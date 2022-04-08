from datetime import date

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
        today = date.today()
        d1 = today.strftime("%m/%d/%y")
        file1.write(f"\n{d1} - {self.name}: {profit}")
