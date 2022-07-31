from pprint import pprint

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def existence_check(document_number=0, shelf_number=0):
    if document_number != 0:
        document_number = document_number.replace(" ", "")
    elif shelf_number != 0:
        shelf_number = shelf_number.replace(" ", "")
    if document_number == str(0) or shelf_number == str(0):
        print("Ошика: номер документа или номер полки не может быть нулевой")
        return (False)
    elif shelf_number != 0:
        shelf_number_bool = False
        for key, valum in directories.items():
            if str(key).replace(" ", "") == shelf_number:
                shelf_number_bool = True
        if shelf_number_bool == False:
            return (False)
        else:
            return (True)
    elif document_number != 0:
        flag = False
        for personal_data in documents:
            for key, valum in personal_data.items():
                if str(valum).replace(" ", "") == document_number:
                    flag = True
        if flag == False:
            return (False)
        else:
            return (True)


def get_name(document_number):
    serch_name = None
    for personal_data in documents:
        for key, valum in personal_data.items():
            if str(valum).replace(" ", "") == str(document_number):
                serch_name = personal_data['name']
    return serch_name


def get_shelf(document_number):
    number_shelf = None
    for key, valum in directories.items():
        for document_ in valum:
            if str(document_).replace(" ", "") == str(document_number):
                number_shelf = int(key)
    return number_shelf

def get_list():
    new_directories = []
    for personal_data in documents:
        new_directories.append(personal_data)
    return (new_directories)


def add_data(shelf_number, name_doc, number_doc, full_name):
    person_data = {"type": name_doc, "number": number_doc, "name": full_name.title()}
    documents.append(person_data)
    for key, value in directories.items():
        if key == shelf_number:
            directories.setdefault(shelf_number, [])
            directories[shelf_number].append(number_doc)
    new_dir = get_list()
    return (new_dir)


def delete_data(document_number):
    examination = existence_check(document_number, 0)
    if examination == False:
        return None
    for id, personal_data in enumerate(documents):
        index_id = id
        for key, valum in personal_data.items():
            if str(valum).replace(" ", "") == document_number:
                documents.pop(index_id)
    for key, valum in directories.items():
        for id, doc_ in enumerate(valum):
            if doc_ == document_number:
                valum.pop(id)
    new_dir = get_list()
    return (new_dir)


def cut_and_paste(document_number, shelf_number):
    for key, valum in directories.items():
        for id, doc_ in enumerate(valum):
            if str(doc_).replace(" ", "") == document_number.replace(" ", ""):
                document_number = valum[id]
                valum.pop(id)
    for key, valum in directories.items():
        for num_ in key:
            if num_ == shelf_number:
                directories.setdefault(shelf_number, [])
                directories[shelf_number].append(document_number)
    return (directories)


def add_shelf(shelf_number):
    directories[shelf_number] = []
    return (directories)



if __name__ == '__main__':
    print(
        "Доступные команды:\np – Поиск ФИО по номеру документа\ns – Поиск полки хранения по по номеру документа\nl – Вывод списка\na – Добавить новые данные\nd – Удалит данные по номеру документа\nm – Перемещение документа на другую полку\nas – Добавить новую полку хранения\ne – Закрыть программу")
    while True:
        comand = (input("\n_________________________________________\n\nВведите команду: ")).lower()
        if comand == 'p':
            print("\n*Поиск ФИО по номеру документа*\n")
            document_number = input("Введите номер документа: ")
            examination = existence_check(document_number, 0)
            if examination == False:
                print('Информация не найдена')
            else:
                name_pa = get_name(document_number.replace(" ", ""))
                print(name_pa)
        elif comand == 's':
            print("\n*Поиск полки хранения по по номеру документа*\n")
            document_number = input("Введите номер документа_: ")
            examination = existence_check(document_number, 0)
            if examination == False:
                print('Информация не найдена')
            else:
                number_sh = get_shelf(document_number.replace(" ", ""))
                print(f'Номер полки: {number_sh}')
        elif comand == 'l':
            print("\n*Вывод списка*\n")
            list_ = get_list()
            pprint(list_)
        elif comand == 'a':
            print("\n*Добавление новых данных*\n")
            shelf_number = input("Введите номер полки: ")
            examination_s = existence_check(0, shelf_number)
            if examination_s == False:
                print('Данной полки не существует')
            else:
                name_doc = input("Введите имя документа: ")
                number_doc = input("Введите номер документа: ")
                examination_d = existence_check(number_doc, 0)
                if examination_d == True:
                    print('Данные по этому документу уже присутствуют в БД')
                else:
                    full_name = input("Введите ФИО: ")
                    new_dir = add_data(shelf_number, name_doc.replace(" ", ""), number_doc, full_name)
                    print("\nДанные успешно добавлены: ")
                    pprint(new_dir)
        elif comand == 'd':
            print("\n*Удалит данные по номеру документа*\n")
            document_number = input("Введите номер документа_: ")
            new_dir = delete_data(document_number.replace(" ", ""))
            if new_dir != None:
                print("\nДанные успешно изменены: ")
                pprint(new_dir)
            else:
                print('Информация не найдена')
        elif comand == 'm':
            print("\n*Перемещение документа на другую полку*\n")
            shelf_number = input("Введите номер полки: ")
            examination_s = existence_check(0, shelf_number)
            if examination_s == False:
                print('Данной полки не существует')
            else:
                number_doc = input("Введите номер документа: ")
                examination_d = existence_check(number_doc, 0)
                if examination_d == False:
                    print('Информация не найдена')
                else:
                    cut_and_paste_ = cut_and_paste(number_doc, shelf_number)
                    print("\nДанные успешно изменены: ")
                    pprint(cut_and_paste_)
        elif comand == 'as':
            shelf_number = input("Введите номер полки: ")
            examination_s = existence_check(0, shelf_number)
            if examination_s == True:
                print('Данная полка уже существует')
            else:
                new_sh = add_shelf(shelf_number)
                print(f'Полка добавлена:\n{new_sh}')
        elif comand == 'e':
            print('Работа с программой завершена')
            break
        else:
            print('Команда введена не верно')

