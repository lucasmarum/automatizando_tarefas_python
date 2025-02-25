def spam(divididopor):
    try:
        return 42 / divididopor
    except ZeroDivisionError:
        print("argumento invalido")


for i in range (-13, 16):
    print(spam(i))