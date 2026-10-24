#calculator rapid
numbera = int(input("Nr. 1: "))
numberb = int(input("Nr. 2: "))
symbol = input("Simbolul (-, +, :, x): ")


if symbol == "-":
    print(numbera - numberb)

elif symbol == "+":
    print(numbera + numberb)

elif symbol == ":":
    print(numbera / numberb)

elif symbol == "x":
    print(numbera * numberb)

else:
    print("Simbolul e gresit")