def greet(name):
    print(f"Hello {name}")

def sum(a,b):
    return a+b

print("Hello world!")

names = ["John", "Jane", "Mary"]
for name in names:
    greet(name)

sums = [(1, 2), (3, 4), (sum(1, 2), sum(3, 4))]

for a, b in sums:
    print(sum(a, b))