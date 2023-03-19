import view
import model

path = 'phone_book.txt'


def start():
    phone_book = open_file()  # сразу открываем тел. книгу
    while True:
        view.show_menu()
        menu_choice = view.choice_menu()
        match menu_choice:
            case 1:  # показать все контакты
                view.show_contacts(phone_book)
            case 2:   # найти контакт
                contact = model.find_contact(phone_book)
                if not contact:
                    print("такого контакта нет")
                else:
                    # print(contact)
                    [print(*i) for i in contact]
            case 3:   # добавить контакт
                add_co = model.add_contact(phone_book)
                print('Контакт',*add_co, 'добавлен')
            case 4:   # изменить контакт
                model.change_contact(phone_book)

            case 5:   # удалить контакт
                con_del = input('кого хотим удалить?: ')
                contact = model.del_contact(phone_book, con_del)
                if contact != None:
                    print(f"{contact} удален")
                else:
                    print('такого контакта нет')
            case 6:  # сохранить телю книгу
                model.save_phonebook(phone_book)
                print('Сохранено')
            case 7:    # выход
                ans = input('сохранить телЮ книгу? Y/N : ').lower()
                if ans == 'y':
                    model.save_phonebook(phone_book)
                print('end of work')
                return


def open_file():
    ph_book = []
    path = 'phone_book.txt'

    with open(path, 'r', encoding='utf-8') as file:
        data = file.readlines()

        for row in data:
            contact = row.strip().split(';')
            ph_book.append(contact)
    return ph_book


