ages = [18, 7, 13, 15, 9, 12, 10, 6, 19, 20]

Between = 0
Above = 0
Below = 0

for i in ages:
    if i >= 18 and i <= 20:
        Between += 1
    elif i > 20:
        Above += 1
    else:
        Below += 1

print("Between 18-20: ", Between)
print("Above 20: ", Above)
print("Below 18: ", Below)
