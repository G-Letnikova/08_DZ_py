phone_book = []
path = 'phone_book.txt'

# открыть файл с контактами - записать в phone_book
def open_file():
    phone_book = []
    path = 'phone_book.txt'

    with open(path, 'r', encoding='utf-8') as file:
        data = file.readlines()

        for row in data:
            contact = row.strip().split(';')
            phone_book.append(contact)
    return phone_book


# ---2 Найти контакт ---
def find_contact(ph_book):
    contact = input('введите имя: ')
    res = []
    for i in ph_book:
        if contact in i:
            res.append(i)
    return res


# -3-Добавить контакт ---
def add_contact(ph_book):
    name = input('введите имя: ').strip()
    phone = input('введите телефон: ').strip()
    comment = input('введите комментарий: ').strip()
    ph_book.append([name, phone, comment])
    return [name, phone, comment]

# - 4 - Изменить контакт ---
def change_contact(ph_book):
    contact = find_contact(ph_book)
    if contact != None:
        contact_new = contact.copy()
        print(contact)
        ch_name = input('введите новое имя(или enter,если имя не меняем): ')
        if ch_name != '':
            contact_new[0] = ch_name
        ch_phone = input('введите новый теефон(или enter, если телефон не меняем): ')
        if ch_phone != '':
            contact_new[1] = ch_phone
        ch_comment = input('введите новый комментарий(или enter, если комментарий не меняем): ')
        if ch_comment != '':
            contact_new[2] = ch_comment
        i = ph_book.index(contact)
        ph_book.pop(i)
        ph_book.append(contact_new)
        print('Контакт изменен:', *contact_new)

    else:
        print('такого контакта нет')


# - 5 - Удалить контакт ---
def del_contact(ph_book,cnt):
    for i in ph_book:
        if cnt in i:
            idx = ph_book.index(i)
            ph_book.pop(idx)
            return cnt
    return None


# - 6 - Сохранить телефоную книгу ---
def save_phonebook(ph_book):
    dict_str = ''
    for i in ph_book:
        dict_str = dict_str + ';'.join(i) + '\n'
    dict_str = dict_str[:-1]
    with open(path, 'w', encoding='utf-8') as file:
        file.write(dict_str)

