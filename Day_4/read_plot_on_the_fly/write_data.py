import random
import time
file_path = "data.txt"

# Open the file for writing
while True:  # Write 10 random values
    file = open(file_path, "a")
    time.sleep(0.1)
    value = random.uniform(-10, 10)
    print(value)

    file.write(str(value) + "\n")
    file.close()
