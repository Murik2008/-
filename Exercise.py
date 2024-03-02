# Показывать все контакты
# 2. Добавлять контакт
# 3. Найти контакт
# 4. Изменять контакт
# 5. Удалить конаткт
# Имя Номер Коммент

list_numbers1 = []
list_functions = [ '1. Удалить контакт', '2. Добавить контакт', '3. Вывести справочник', '4. Найти контакт','5. Изменить контакт']

with open('phone numbers.txt', 'r') as file:
        for i in file:
            list_numbers2 = i.split()
            list_numbers1.append({'Имя': list_numbers2[0], 'Номер': list_numbers2[1], 'Комментарий': list_numbers2[2]})

def print_array(array):
    for i in array:
        print(i)            

print_array(list_functions)
while True:
    try:
        functions=int(input())
        break
    except ValueError:
        print("Вы ввели неверное значение. Выберите пункт из меню")
        next

def show_contacts(functions, array):
     if functions == 3:
          print('Ваш телефонный справочник: ')
          print_array(array)

def add_contact(functions, array):
    if functions == 2:
        name = input('Введите имя контакта: ')
        number = input('Введите номер контакта: ')
        comment = input('Введите комментарий: ')
        new_string = f'{name} {number} {comment}'
        array.append({'Имя': name, 'Номер': number, 'Комментарий': comment})
        with open('phone numbers.txt', 'a+') as file:
            file.write(new_string)
        show_contacts(3, array)

def find_contact(functions, my_dict):
    if functions == 4:
        search_word=input("Введите текст для поиска контакта:\n")
        search_result=[]
        for item in range(len(my_dict)):
            for i in my_dict[item].values():
                if search_word in i:
                    print(my_dict[item])
                    search_result.append(item)
        print(search_result)
        return search_result

def change_contact(functions, my_dict, index):
    if functions == 5:
        fields=list(my_dict[0].keys())
        print(fields)
        temp_dict=my_dict[index-1]
        to_change=int(input("В какое поле вносим изменения: 1. Имя 2. Телефон 3. Комментарий? "))
        new_value=input("Введите новое значение поля: ")
        temp_dict[fields[to_change-1]]=new_value
        my_dict[index-1]=temp_dict
        with open('phone numbers.txt', 'w') as file:
            for i in my_dict:
                file.write(f'{i["Имя"]} {i["Номер"]} {i["Комментарий"]}\n')
        show_contacts(3, my_dict)

add_contact(functions, list_numbers1)
show_contacts(functions, list_numbers1)
find_contact(functions, list_numbers1)
change_contact(functions, list_numbers1, int(input('Введите номер места контакта: ')))