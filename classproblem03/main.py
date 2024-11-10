with open("fle.txt", "w") as f:
    f.write("hello sourav\n")


with open("fle.txt", "a") as f:
    f.write("hello sourav")
    f.close()

with open("fle.txt", 'r') as f:
    print(f.read())
