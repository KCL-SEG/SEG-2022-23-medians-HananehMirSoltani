while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
numbers.sort()
q = len(numbers)//2 
if len(numbers) % 2 !=0:
   print(f'median is: {numbers[q]}')
else:
    print(f'median is: {(numbers[q-1]+numbers[q])/2}')
