


# ******************************
numbers = list(map(int, input().split()))
print (numbers)

total = sum(numbers)
avg = total / len(numbers)

for i in range(len(numbers)):
	dist = abs(numbers[i] - avg)
	print (f'{dist:.2f}', end=' ')

# ******************************


# Use this statement to print out the list element. # Replace the variable 'dist' with your variable
# print (f'{dist:.2f}', end=' ')
