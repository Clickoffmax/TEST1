import random
number = random.randint(1, 10)
print(number)
for i in range(10):
    playernumber = int(input())
    if playernumber == number:
        print("win")
    else:
        print("lose")
print("попытки закончились")