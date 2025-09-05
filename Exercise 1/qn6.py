numbers = []


for i in range(5):
    number = float(input("Enter a number: "))
    numbers.append(number)


average = sum(numbers) / len(numbers)

print("The numbers you entered:", numbers)
print("The average is:", average)
    
    
