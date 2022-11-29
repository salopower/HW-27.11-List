A = []
N = int(input("Enter the number of list: "))
for num in range(N):
    number = int(input("Enter the numbers: "))
    A.append(number)
reversed_A = A[::-1]
print(f"Reversed list: {reversed_A}")
