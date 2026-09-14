numbers = []
total = 0


for i in range(10):
    while True: 
        try:
            num = int(input(f"Enter number {i+1}: "))
            numbers.append(num)
            total += num
            break  
        except ValueError:
            print("Invalid input. Please enter an integer.")


if numbers:  
    avg = total / len(numbers)
else:
    avg = 0


print("\nNumbers entered:", numbers)
print("Average:", avg)
print("Total:", total)
