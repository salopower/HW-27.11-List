line = input("Enter the text: ").split()
count_digit = 0
for i in line:
    if i.isdigit():
        count_digit += 1
if count_digit == 0:
    print("Numbers not found")
else:
    print(f"Numbers found: {count_digit}")
