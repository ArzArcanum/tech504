for i in range(1,101):
    print(i)
    current=""
    if i % 3 == 0:
        current += "Fizz"
    if i % 5 == 0:
        current += "Buzz"
    if current:
        print(current)