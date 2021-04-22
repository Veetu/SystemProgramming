amount = int(input("How many numbers are you going to give: "))
NumberArray = []
i = 0
while i < amount:
    number = input("Enter number: ")
    NumberArray.append(int(number))
    i += 1
print("The average is ", sum (NumberArray) / amount)