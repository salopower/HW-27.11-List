my_list = []
for num in range(10):
    number = int(input("Enter the numbers: "))
    my_list.append(number)
N = int(input("\nEnter the number: "))
value = my_list.count(N)
print(f"Amount of values: {value}")
