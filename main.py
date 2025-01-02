def greet(name):
    print(f"Hello {name}")

def sum(a,b):
    return a+b

print("Hello world!")

names = ["John", "Jane", "Mary"]
for name in names:
    greet(name)

print(sum(1,2))
print(sum(3,4))
print(sum(sum(1,2),sum(3,4)))