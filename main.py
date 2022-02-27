import json
f = open ('data/dinheiro.json', "r+")
money1 = json.loads(f.read())
money = money1["dinheiro"]
print("Hi what you what to do?")
print("1-See your money")
print("2-Deposit")
print("3-Withdraw")
respond1 = eval(input(""))
if respond1 == 1:
    print("Your money is " + str(money))
if respond1 == 2:
    print("How much you want to deposit?")
    print("Your have " + str(money))
    moneytoadd1 = input("")
    moneytoadd2 = float(money) + float(moneytoadd1)
    moneytoadd = {"dinheiro":float(moneytoadd2)}
    jsonString = json.dumps(moneytoadd)
    jsonFile = open("data/dinheiro.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()
if respond1 == 3:
    print("How much you want to withdraw?")
    print("Your have " + str(money))
    moneytotake1 = input("")
    moneytotake2 = float(money) - float(moneytotake1)
    moneytotake = {"dinheiro":float(moneytotake2)}
    jsonString = json.dumps(moneytotake)
    jsonFile = open("data/dinheiro.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()