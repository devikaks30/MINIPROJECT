import random

class dice:

    def roll(self, row, column):

        for i in range(1, column + 1):
            print("D%d" % i, "", end="\t|\t")
        print()

        for i in range(row):
            for j in range(column):
                print(random.randrange(1, 7), end="\t|\t")
            print()
        print(" To roll again type 1, to exit type 0")


while True:
    a = int(input('Input how many times you want the dice to be thrown : '))
    b = int(input("Input how many dice do you wish to throw : "))
    if (a >= 10):
        print("The number of times you want to throw the die cant be greater than 10. Please enter a number lesser than 10")
        print(" To Enter the values again type 1, to exit type 0")
    elif b >= 10:
        print("The number of die to be thrown, cant be greater than 10. Please enter a number lesser than 10")
        print(" To Enter the values again type 1, to exit type 0")
    else:
        obj = dice()
        obj.roll(a, b)
        
    c = input()
    if c == '0':
        break
  
