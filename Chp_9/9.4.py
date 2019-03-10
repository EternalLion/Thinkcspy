"""Print out a neatly formatted multiplication table, up to 12 x 12."""

for x in range(1,13):
    for y in range (1,13):
        product = x * y
        print("{}".format(product:^6), end=" ")
    print()
