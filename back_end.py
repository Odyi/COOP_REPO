import operator

tall2_input = 0

ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

def regne():
    tall1 = input("Skriv inn tall: ")
    try: 
        valid = int(tall1)
    except:
        print("Ugyldig input")
        regne()
    operasjon = input("Skriv in operasjon(+ - * /): ")
    tall2()

    global tall2_input

    tall1_int = int(tall1)
    tall2_int = int(tall2_input)
    op_func = ops[operasjon]
    result = op_func(tall1_int, tall2_int)
    print(f"{tall1_int} {operasjon} {tall2_int} = {result}")

def tall2():
    global tall2_input
    tall2_input = input("Skriv inn tall: ")
    print(type(tall2_input))

    try: 
        print("try: " + tall2_input)
        valid = int(tall2_input)
    except:
        print("except: " + tall2_input)
        input("Ugyldig input, trykk en tast for å fortsette")
        tall2()
