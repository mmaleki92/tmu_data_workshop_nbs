v = 1

for i in range(500):
    v = v - 0.001
    print("Current value:", v)
    if v == 0.5:
        print("Target value reached!")
        break