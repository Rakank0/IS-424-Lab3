num = []
print("Welcome to the multiplication program")
for i in range(10):
    val = int(input("Enter value: "))
    num.append(val)
big = num[0]

for x in num:
    if x>big:
        big=x

print ("The biggest number is: ",big)