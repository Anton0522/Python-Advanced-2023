def operate(operator, *args):
    def sum_nums():
        return sum(args)

    def subtract():
        res = 0
        for num in args:
            res -=num
        return res
    def miltiply():
        res = 1
        for num in args:
            res *= num
        return res

    def divide():
        res = 1
        for num in args:
            res /= num
        return res

    if operator == "+":
        return sum_nums()
    elif operator == "-":
        return subtract()
    elif operator == "*":
        return miltiply()
    else:
        return divide()
