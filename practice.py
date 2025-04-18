
"""
username = input("Enter User name:")
print("the name is :"+username)

# lab report:2
constructing a factorial pyramid concerning
 the palindrome pyramid

rows = int(input("Enter the number of rows: "))
for i in range(rows):
    print(" " * (rows - i - 1), end="")

    num = 1
    for j in range(1, i + 2):
        num *= j
        print(num, end=" ")

    for j in range(i, 0, -1):
        num = 1
        for k in range(1, j + 1):
            num *= k
        print(num, end=" ")

    print()
"""




