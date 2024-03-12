import random
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
prav = 0
ch = 0

while ch <= 3:
    if ch == 3:
        print("Игра окончена. Правильных ответов:", prav)
        break
    b = int(random.choice(a))
    c = int(random.choice(a))
    print(b, "+", c, "=", end=" ")
    d = int(input(""))
    if b + c == d:
        print("Правильно!")
        prav += 1
    elif b + c != d:
        print("Ответ неверный")
        ch += 1