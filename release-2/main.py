def sorting(arr, direction):
    return 













#функция min
def Min():
    arr=[1, 5, 34, -100]
    smallest = min(arr)
    print(smallest)
Min()




#функция getSet
numbers = [1, 1, 1, 3, 4, 2, 2]
def getSet(numbers):
    list_of_unique_numbers = []
    unique_numbers = set(numbers)
    for number in unique_numbers:
        list_of_unique_numbers.append(number)

    return list_of_unique_numbers

print(getSet(numbers))
