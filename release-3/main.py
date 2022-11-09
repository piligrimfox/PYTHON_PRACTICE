#функция fullName
def BokLi():
    my_dictionary = {'name': 'Lim', 'surname': 'Bok', 'age': 12}
    print((my_dictionary['surname']) + ' ' +(my_dictionary['name']))
BokLi()






#функция createObjFromStr
def createObjFromStr(string):
    try:
        string = string[1:-1]
        string = string.replace(' ', ' ')
        string = string.replace(" ", " ")
        key_value = string.split(',')
        dictionary = {}
        for i in key_value:
            key, value = i.split(':')
            dictionary[key] = value
        return dictionary
    except:
        return 'ERROR'
print(createObjFromStr("{name: 'Vova', age: 12, type: 'owner'}"))
