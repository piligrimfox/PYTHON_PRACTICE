
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



#функция findTheMostReapetedEls
def findTheMostReapetedEls():
    list=[1, 1, 1, 3, 4, 2, 2, 2]
    list_1=[(list.count(x),x) for x in set(list)]
    max_count=max(list_1)[0]
    for ele in list_1:
        if ele[0]==max_count:
            print(ele[1])
findTheMostReapetedEls()

# функция stack


#функция checkForBadWord
def checkForBadWord():
    words = "Hi, Nikita"
    index = words.find("Hi")
    if (index !=-1):
     print(True)
    else:
     print(False)
checkForBadWord()
