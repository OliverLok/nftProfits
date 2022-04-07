import royalty
import recordProfift
import cryptocompare as cc


def option1():
    name = input("Project Name: ")
    collection = input("Project URL: ")
    buyPrice = float(input("Buy Price + Gas: "))
    sellPrice = float(input("Sell Price: "))
    totalRoyalty = royalty.royaltyFees(collection)
    totalSellPrice = sellPrice - (sellPrice * totalRoyalty)  # how much you actually got back accounting for fees
    profit = round((totalSellPrice - buyPrice), 4)  # amount made/lost
    listNFT = recordProfift.record(name, buyPrice, totalSellPrice)
    listNFT.recordData(profit)
    return listNFT


def option2():
    collection = input("Please type the URL of the collection: ")
    buyPrice = float(input("Buy Price + Gas: "))
    totalRoyalty = royalty.royaltyFees(collection)
    breakEven = round((buyPrice + (buyPrice * totalRoyalty)), 4)
    print(f"You'll break even at {breakEven} ETH ")


def option3():
    file1 = open("profits.txt")
    numbers = file1.read()
    splitnum = numbers.split("\n")  # splits the file every time it ends a line (makes it a list)
    addedETH = 0
    for i in range(len(splitnum)):
        x = splitnum[i].split(":")  # splits the list so it seperates the project name from the profit you made
        addedETH += float(x[1])  # adds the profit together
    print(f"Total Profit in Etherium: {addedETH}")
    ethToUSD = cc.get_price('ETH', currency='USD')  # gets current price of etherium
    temp = ethToUSD.values()  # gets a dictionary of eth in USD
    v = str(*temp)  # removes dict_values and turns it into a string
    temp = v.split(":")  # splits the string into 2 parts (1st part 'USD', 2nd part price of eth)
    temp2 = temp[1]  # puts the 2nd part (price of eth) into temp 2
    temp3 = temp2[:-1]  # removes the hanging } at the end
    USD = float(temp3[1:])  # removes the space in the beginning
    profitUSD = round((addedETH * USD), 2)
    print(f"Total Profit in USD: ${profitUSD}")


print("Welcome to my Program. Please choose one of the following: ")
print("1) Record Profit")
print("2) How much to break even")
print("3) Profit List")
option = input("Please select an option: ")
if option == "1":
    print(option)
    option1()
elif option == "2":
    option2()
elif option == "3":
    option3()
