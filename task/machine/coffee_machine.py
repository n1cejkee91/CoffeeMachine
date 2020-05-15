class CoffeeMachine:
    def __init__(self, water, milk, coffee, cups, money):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        self.money = money

    def actions(self):
        print("Write action (buy, fill, take, remaining, exit):")
        action = input()
        if action == 'exit':
            return CoffeeMachine._exit(self)
        elif action == 'buy':
            return CoffeeMachine._buy(self)
        elif action == 'fill':
            return CoffeeMachine._fill(self)
        elif action == 'take':
            return CoffeeMachine._take(self)
        elif action == 'remaining':
            return CoffeeMachine._remaining(self)
        else:
            print("Try again!\n")
            return CoffeeMachine.actions(self)

    def _exit(self):
        pass

    def _buy(self):
        print("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        action = input()
        if action == '1':
            if self.water >= 250 and self.coffee >= 16 and self.cups >= 1:
                self.water -= 250
                self.coffee -= 16
                self.cups -= 1
                self.money += 4
                print("I have enough resources, making you a coffee!\n")
            elif self.water < 250:
                print("Sorry, not enough water!\n")
            elif self.coffee < 16:
                print("Sorry, not enough coffee beans!\n")
            elif self.cups < 1:
                print("Sorry, not enough cups!\n")
            return CoffeeMachine.actions(self)
        elif action == '2':
            if self.water >= 350 and self.coffee >= 20 and self.cups >= 1 and self.milk >= 75:
                self.water -= 350
                self.milk -= 75
                self.coffee -= 20
                self.cups -= 1
                self.money += 7
                print("I have enough resources, making you a coffee!\n")
            elif self.water < 350:
                print("Sorry, not enough water!\n")
            elif self.milk < 75:
                print("Sorry, not enough milk!\n")
            elif self.coffee < 20:
                print("Sorry, not enough coffee beans!\n")
            elif self.cups < 1:
                print("Sorry, not enough cups!\n")
            return CoffeeMachine.actions(self)
        elif action == '3':
            if self.water >= 200 and self.coffee >= 12 and self.cups >= 1 and self.milk >= 100:
                self.water -= 200
                self.milk -= 100
                self.coffee -= 12
                self.cups -= 1
                self.money += 6
                print("I have enough resources, making you a coffee!\n")
            elif self.water < 200:
                print("Sorry, not enough water!\n")
            elif self.milk < 100:
                print("Sorry, not enough milk!\n")
            elif self.coffee < 12:
                print("Sorry, not enough coffee beans!\n")
            elif self.cups < 1:
                print("Sorry, not enough cups!\n")
            return CoffeeMachine.actions(self)
        elif action == 'back':
            print()
            return CoffeeMachine.actions(self)

    def _fill(self):
        self.water = int(input("\nWrite how many ml of water do you want to add: ")) + self.water
        self.milk = int(input("Write how many ml of milk do you want to add: ")) + self.milk
        self.coffee = int(input("Write how many grams of coffee beans do you want to add: ")) + self.coffee
        self.cups = int(input("Write how many disposable cups of coffee do you want to add:")) + self.cups
        print()
        # self.money = self.money
        return CoffeeMachine.actions(self)

    def _take(self):
        print("I gave you $" + str(self.money) + '\n')
        self.money -= self.money
        return CoffeeMachine.actions(self)

    def _remaining(self):
        print('''\nThe coffee machine has:
    {water} of water
    {milk} of milk
    {coffee} of coffee beans
    {cups} of disposable cups 
    {money} of money\n'''.format(water=self.water, milk=self.milk, coffee=self.coffee, cups=self.cups,
                                 money=self.money))
        return CoffeeMachine.actions(self)


if __name__ == "__main__":
    coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
    coffee_machine.actions()