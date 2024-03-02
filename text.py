main_menu = ['Главное меню',
             'Открыть телефонную книгу',
             'Сохранить телефонную книгу',
             'Показать контакты',
             'Создать контакт',
             'Найти контакт',
             'Изменить контакт',
             'Удалить контакт',
             'Выход']

username_message = 'Введите имя пользователя: '
choise_main_menu = f'Выберите пункт из меню ({1}-{len(main_menu)-1}): '
choise_main_menu_error = f'Нужно ввести число от 1 до {len(main_menu)-1}!'

phone_book_opened_succesful = 'Телефонная книга открыта успешно!'
phone_book_saved_succesful = 'Телефонная книга сохранена успешно!'
phone_book_closed_successful = 'Телефонная книга закрыта успешно!'

empty_phone_book_error = 'Телефонная книга пуста или не открыта!'

input_new_contact = ['Ввелите имя контакта: ',
                     'Введите номер контакта: ',
                     'Введите комментарий для контакта: ']

input_search_word = 'Введите слово для поиска контакта: '
input_search_word_for_edit = 'Введите слово для поиска контакта, который хотите изменить: '
input_id_for_edit = 'Введите ID контакта, который хотите изменить: '
input_search_word_for_delete = 'Введите слово для поиска контакта, который хотите удалить: '
input_id_for_delete = 'Введите ID контакта, который хотите удалить: '

no_changes = 'Или ENTER, чтобы оставить без изменений'

edit_contact = [f'Введите новое имя ({no_changes}): ',
                f'Введите новый номер ({no_changes}): ',
                f'Введите новый комментарий ({no_changes}): ']

def greeting_user(username: str) -> str:
    return f'Здравствуйте, {username}!'

def new_contact_added_successfully(name: str) -> str:
    return f'Контакт "{name}" успешно добавлен!'

def find_contact_no_result(word: str) -> str:
    return f'Контакты содержащие "{word}" не найдены'

def edit_contact_succesful(name) -> str:
    return f'Контакт {name} успешно изменен!'

def delete_contact_succesful(name) -> str:
    return f'Контакт {name} успешно удален!'