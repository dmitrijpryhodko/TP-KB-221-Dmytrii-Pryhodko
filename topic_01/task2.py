a = "wElcOMe to School"
print(a.capitalize())
#.capitalize() - перетворює рядок так, щоб він починався з букви у верхньому регістрі, а решта букв переходила у нижній регістр

sometext = "wElcOMe to schOoL"
print(sometext.title())
#title() - пише кожне слово у рядку з великої літери

txt = "   Welcome to school  "
print(txt.strip())
#strip() - видаляє пробіли перед і після рядка 

b = "welcome to school"
print(b.upper())
#upper - переводить всі символи рядка у верхній регістр

с = "WELCOME To scOOL"
print(b.lower())
#lower - переводить всі символи рядка у нижній регістр

list = ['cherry', 'melon', 'apple', 'pear']
list.append('lemon')
print(list)
#append - додає елемент в кінець списку

list = ['cherry', 'melon', 'apple', 'pear','apple']
x = list.count('apple')
print(x)
#count - рахує скільки разів зустрічається певний елемент в списку

list = ['cherry', 'melon', 'pear', 'apple']
list.insert(2, 'lemon')
print(list)
#insert - додає елемент до списку по індексу