import time
import sys
from colored_print import log
boost=int(0)
Command=None
Options=["Balance","Plant","Quit"]
Booststr="⏩ Boost farming speed for 50$"
Booststr2="⏩⏩ Insanely Boost farming speed for 100$"
#Farm class
class Farm:
    def __init__(self, balance=9):
     self._balance=balance

    def __str__(self):
      return self._balance

    def withdraw(self, n):
     self._balance=self._balance-n

    def deposit(self, n):
     self._balance=self._balance+n

    @property
    def balance(self):
     return self._balance

    @property
    def size(self):
      return self._size

    @balance.setter
    def balance(self, value):
      self._balance = value

    def balance_check(self, n):
      return self._balance>=n

def plant(farm, plant):

    # Strawberry option
    if plant == "1":
      if farm.balance_check(9):
        farm.withdraw(9)
        time.sleep(0.2)
        log.err("You have spent: " + "9" + "$ " + "to plant one 🍓").store(path="log.txt")
        print("...")
        time.sleep(2.1-boost)
        farm.deposit(13)
        log.success("You have earned: " + "15" + "$ " + "from planting one 🍓").store()
      else:
        print("Insufficient funds")
    # Banana option
    elif plant == "2":
      if farm.balance_check(13):
        farm.withdraw(13)
        time.sleep(0.2)
        log.err("You have spent: " + "13" + "$ " + "to plant one 🍌").store(path="log.txt")
        print("...")
        time.sleep(2.7-boost)
        farm.deposit(19)
        log.success("You have earned: " + "19" + "$ " + "from planting one 🍌").store()
      else:
        print("Insufficient funds")
    # Apple option
    elif plant == "3":
      if farm.balance_check(6):
        farm.withdraw(6)
        time.sleep(0.2)
        log.err("You have spent: " + "6" + "$ " + "to plant one 🍎").store(path="log.txt")
        print("...")
        time.sleep(1.65-boost)
        farm.deposit(9)
        log.success("You have earned: " + "9" + "$ " + "from planting one 🍎").store()
      else:
        # little easter egg for being too poor xD
        print("Insufficient funds")
        time.sleep(0.6)
        print("a bit too broke aren't we?")
        farm.deposit(6)
        time.sleep(0.8)
        log.success("You have randomly earned: " + "6" + "$ " + "somehow!").store()
        time.sleep(0.5)
    # Watermelon option
    elif plant == "4":
      if farm.balance_check(25):
        farm.withdraw(25)
        time.sleep(0.2)
        log.err("You have spent: " + "25" + "$ " + "to plant one 🥑").store(path="log.txt")
        print("...")
        time.sleep(3.4-boost)
        farm.deposit(42)
        log.success("You have earned: " + "42" + "$ " + "from planting one 🥑").store()
      else:
        print("Insufficient funds")
    # Avocado option
    elif plant == "5":
      if farm.balance_check(40):
        farm.withdraw(40)
        time.sleep(0.2)
        log.err("You have spent: " + "40" + "$ " + "to plant one 🍉").store(path="log.txt")
        print("...")
        time.sleep(3.9-boost)
        farm.deposit(65)
        log.success("You have earned: " + "65" + "$ " + "from planting one 🍉").store()
      else:
        print("Insufficient funds")
    elif plant == "Back":
      menu()
    else:
      print("Unavailable option!")

#Plant prompt
def Plant_prompt(farm):
  print("What do you want to plant?")
  log.pink(f" balance:{str(farm.balance)}$ \n 1: 🍓 for 9$ \n 2: 🍌 for 13$ \n 3: 🍎 for 6$ \n 4: 🥑 for 25$ \n 5: 🍉 for 40$")
  Fruit_plant=input().capitalize().strip()
  #Match input with one of the options
  if Fruit_plant not in ["1","2","3","4","5","Back"]:
      print("Unavailable option!")
      return Plant_prompt(farm)
  elif Fruit_plant=="Back":
      return menu()
  else:
      plant(farm, Fruit_plant)
      return menu()
#Shop prompt
def shop_prompt(farm):
 global boost
 global Booststr
 global Booststr2
 # check for boost
 if boost>0.1:
  Booststr="Already owned!"
  Booststr2="⏩⏩ Insanely Boost farming speed for 100$"
 else:
   Booststr2="Locked!"
 if boost>0.5:
  Booststr2="Already owned!"
 print("What do you want to buy?")
 log.pink(f" balance:{str(farm.balance)}$ \n 1: {Booststr} \n 2: {Booststr2}  \n 3: Buy a house for 200$ (Ends the game!)")
 Fruit_shop=input().capitalize().strip()
 #Match input with one of the options
 if Fruit_shop not in ["1","2","3","Back"]:
      print("Unavailable option!")
      return shop_prompt(farm)
 elif Fruit_shop=="Back":
      return menu()
 else:
      shop(farm, Fruit_shop)
      return menu()
def reprompt():
  return (input("Enter a command:").capitalize())
def shop(farm, item):
    global boost
    # Speed-up option
    if item == "1":
      if farm.balance_check(50) and boost<0.2:
        farm.withdraw(50)
        time.sleep(0.2)
        log.success("You have spent: " + "50" + "$ " + "to upgrade your production!").store(path="log.txt")
        boost=boost+0.4
      else:
        print("Unable to make this purchase!")
    # Insane Speed-up option
    elif item == "2":
      if farm.balance_check(100) and 0.1<boost<0.8:
        farm.withdraw(100)
        time.sleep(0.2)
        log.success("You have spent: " + "100" + "$ " + "to insanely upgrade your production!").store(path="log.txt")
        boost=boost+1.2
      else:
        print("Unable to make this purchase!")
    # House option
    elif item == "3":
      if farm.balance_check(200):
        farm.withdraw(200)
        time.sleep(0.2)
        log.success("Thanks for playing! 🎉🎉🎉🎉").store()
        sys.exit()
      else:
        print("Insufficient funds")
    elif plant == "Back":
      menu()
    else:
      print("Unavailable option!")
#menu function
def menu():
  log.info("Kindly choose from the options below:")
  return (input("🏦 Balance \n🌱 Plant \n🛒 Shop \n⛔️ Quit \n").capitalize())

#options
def options(farm, Command):
  ##Option: Balance
  if Command == "Balance":
       log.success("We're currently at: " + str(farm.balance) + "$")
       return menu()

  #Option: Planting
  elif Command == "Plant":
      return Plant_prompt(farm)

  #Option: Shop
  elif Command == "Shop":
       return shop_prompt(farm)

  #Option: Quit
  elif Command == "Quit":
      sys.exit("Cya!")
  else:
     return menu()

# Main method
def main():
    farm = Farm()
    print("Welcome to my Farmer Simulator game!")
    Command = menu()
    while True:
        Command = options(farm, Command)


if __name__ == "__main__":
    main()
