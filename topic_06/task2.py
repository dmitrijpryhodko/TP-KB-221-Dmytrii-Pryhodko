nameandmark = [{'name': 'Ivan', 'mark': 90},
        {'name': 'Peter', 'mark': 65},
        {'name': 'Evgeniy', 'mark': 88},
        {'name': 'Valeriy', 'mark': 67},
        {'name': 'Kyrylo', 'mark': 74},
        {'name': 'Viktoria', 'mark': 55},
        {'name': 'Alexander', 'mark': 83},
        {'name': 'Boris', 'mark': 92},
        {'name': 'Dmitriy', 'mark': 75},
        {'name': 'Julia', 'mark': 75},
        {'name': 'Igor', 'mark': 100},
        {'name': 'Anna', 'mark': 92}]


parameter = input("Виберіть ключ для сортування (N for name or M for mark): ")

def sort_data(nameandmark, parameter):
    if parameter == 'N':
        return sorted(nameandmark, key=lambda x: x['name'])
    elif parameter == 'M':
        return sorted(nameandmark, key=lambda x: x['mark'])
    else:
        print("Ключ сортування неправильний")
        return nameandmark

sorted_data = sort_data(nameandmark, parameter)

for item in sorted_data:
    print(f"Name: {item['name']}, Mark: {item['mark']}")
