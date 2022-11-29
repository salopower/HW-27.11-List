A = []
N = int(input("Enter the number of list: "))
for num in range(N):
    number = int(input("Enter the numbers: "))
    A.append(number)
print(f"List:\n{A}")
max_el = A[0]
min_el = A[0]
for num in A:
    if num > max_el:
        max_el = num
    else:
        min_el = num
print(f"Max element: {max_el}\nMin element: {min_el}")