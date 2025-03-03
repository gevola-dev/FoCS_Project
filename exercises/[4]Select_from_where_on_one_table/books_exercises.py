

# Exercise 1: Suppose the cover price of a book is €24.95, but bookstores get a 40% discount.
    # Shipping costs €3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?
output = 60 * 24.95 * (100 - 40)/100 + 3 + (60 - 1) * 0.75
print("exercise1 ouput:", output)

# Exercise 2: Compare your answer with the solution up to 2 decimal numbers.
output = 200 * 24.95 * (100 - 40)/100 + 3 + (60 - 1) * 0.75
print("exercise2 ouput:", output)

# Exercise 3: Find the number of copies you can buy with €10000.
def books_cost(num):
    return num * 24.95 * (100 - 40)/100 + 3 + (num - 1) * 0.75
print("exercise3 ouput:", books_cost(635))

# Exercise 4: Find the number of copies you can buy with €10000, using a while loop
i = 1
while books_cost(i) <= 10000:
    i += 1
print("exercise4 ouput:", i-1, books_cost(i-1))

# Exercise 5: Find the number of copies you can buy with €10000, using a for loop (Hint: use range(10000))
for x in range(700):
    if books_cost(x) > 10000:
        break
print("exercise4 output:", x-1, books_cost(x-1))
