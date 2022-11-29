A = []
C = []
for num in range(5):
    number = int(input("Enter the numbers: "))
    A.append(number)
print(f"\nList:\n{A}")
for num in A:
    if num > 5:
        C.append(num)
print(f"\nA list of numbers greater than 5:\n{C}")