import operator

ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

def regne():
    tall1 = float(input("Skriv inn tall: "))
    operasjon = input("Skriv in operasjon(+ - * /): ")
    tall2 = float(input("skriv inn tall: "))
    op_func = ops[operasjon]
    result = op_func(tall1, tall2)
    print(f"{tall1} {operasjon} {tall2} = {result}")
