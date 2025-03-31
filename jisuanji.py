#简易计算器

while True:
    num1 = float(input("输入数字："))
    fu = input("输入符号：+-*/")
    num2 = float(input("输入数字："))

    if fu == "+":
        print(num1 + num2)
    elif fu == "-":
        print(num1 - num2)
    elif fu == "*":
        print(num1 - num2)
    elif fu == "/":
        print(num1 - num2)
    else:
        print("请重新输入")
