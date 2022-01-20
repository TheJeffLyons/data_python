open_cake = open("CupcakeInvoices.csv")

for cake in open_cake:
    print(cake)

open_cake.seek(0)

for cake in open_cake:
    cake = cake.strip()
    values = cake.split(",")
    print(values[2])

open_cake.seek(0)

for cake in open_cake:
    cake = cake.strip()
    values = cake.split(",")
    quantity = float(values[3])
    cost = float(values[4])
    total = quantity * cost
    print(total)
    
open_cake.seek(0)

amount1 = 0
amount2 = 0
for sprinkle in open_cake:
    cake = sprinkle.strip()
    values = cake.split(",")
    quantity = float(values[3])
    cost = float(values[4])
    amount1 += quantity
    amount2 += cost
    final = amount1 + amount2
    print(final)