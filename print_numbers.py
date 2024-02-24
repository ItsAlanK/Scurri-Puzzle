# Print nums 1 - 100
# Check mults of 3, 5, 3 and 5
# Print Three, Five, ThreeFive respectively

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("ThreeFive")
    elif i % 3 == 0:
        print("Three")
    elif i % 5 == 0:
        print("Five")
    else:
        print(i)