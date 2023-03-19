def show_menu() -> None:
    print('''
    1. Показать все контакты
    2. Найти контакт
    3. Добавить контакт
    4. Изменить контакт
    5. Удалить контакт
    6. Сохранить телефоную книгу
    7. Выход ''')

def choice_menu() -> int:
    while True:
        number = input('выберете пункт меню: ')
        if number.isdigit() and 0 < int(number) < 8:
            return int(number)
        print('введите число от 1 до 7: ')


# -1- показать контакты ---
def show_contacts(ph_book):
    if not ph_book:
        print('телефонная книга пуста')
        return False
    for index,contact in enumerate(ph_book,1):
        print(f'{index}. {contact[0]:<15}{contact[1]:<15}{contact[2]}')

