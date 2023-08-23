from soft import data_base
from soft.data_base import Editing_db
"""
Импортирование файл с базой данных
Импортирование класса для удобной работы

"""
conn = data_base.conn
cursor = data_base.cursor

"""
Перенос инициализации базы данных с фала DB

"""
def user_selection():#Запуск меню с информацей о выборе
    print("Выбирите цифру из предолженных варинтов")
    select = int(input('1: Добавить контакт\n2: Редактировать запись\n3: Поиск записи\n4: Посмотреть запись\n5: Выход\n===>>>'))
    return select

def run_select_1():#Добавление новой записи
    surname_db = input('Введите Surname:>>')
    surname_db.capitalize()

    middle_name_db = input('Введите Middle name:>>')
    middle_name_db.capitalize()

    name_db = input('Введите Name:>>')
    name_db.capitalize()

    while True: #Базовая проверка правильности ввода номера
        print('Номер телефон начинается с +7\nДлина номера должна состовлять 12 символов')
        privat_phone_db = input('Введите Privat phone:>>')
        if privat_phone_db[0] != '+' or privat_phone_db[1] != "7" or len(privat_phone_db) != 12:
            continue
        else:
            break
    
    company_db = input('Введите Company:>>')
    company_db.capitalize()
    
    while True: #Базовая проверка правильности ввода номера
        print('Номер телефон начинается с +7')
        work_phonee_db = input('Введите Work phonee:>>')
        if work_phonee_db[0] != '+' or work_phonee_db[1] != "7" or len(work_phonee_db) != 12:
            continue
        else: 
            break
    data_base.add_ad(surname = surname_db, middle_name = middle_name_db, name = name_db, company = company_db, privat_phone = privat_phone_db, work_phonee = work_phonee_db)
    return surname_db, middle_name_db, name_db, privat_phone_db, company_db, work_phonee_db

def run_select_2(): #Редактирование конкретнйо записи 
    print("Выбирите id Пользователся предолженных варинтов")
    data = data_base.id_all()
    data_base.conclusion_select_2(data)
    select = input("ID Пользователя n===>>>")
    select_performance = int(input('Введите то, что хотите изменить\nsurname = 1\nmiddle_name= 2\nname= 3\ncompany= 4\nprivat_phone = 5\nwork_phonee = 6\n>>>'))
    if select_performance == 1:
        surname_input = input('Введите новый surname:>>>')
        Editing_db.surname_db(surname = surname_input, id = select)
    
    if select_performance == 2:
        middle_name_input = input('Введите новый middle_name:>>>')
        Editing_db.middle_name_db(middle_name = middle_name_input, id = select)

    if select_performance == 3:
        name_input = input('Введите новый name:>>>')
        Editing_db.name_db(name = name_input, id = select)  

    if select_performance == 4:
        company_input = input('Введите новый company:>>>')
        Editing_db.company_db(company = company_input, id = select) 
      
    if select_performance == 5:
        while True:
            print('Номер телефон начинается с +7')
            privat_phone_input = input('Введите privat_phone:>>')
            if privat_phone_input[0] != '+' or privat_phone_input[1] != "7" or len(privat_phone_input) != 12:
                print('Неправильно набран номер, номер должен блинной 12 символов месте с "+" и начинается с +7')
                continue
            else: 
                break
        Editing_db.privat_phone_db(privat_phone = privat_phone_input, id = select) 

    if select_performance == 6:
        while True:
            print('Номер телефон начинается с +7')
            work_phonee_input = input('Введите Work phonee:>>')
            if work_phonee_input[0] != '+' or work_phonee_input[1] != "7" or len(work_phonee_input) != 12:
                print('Неправильно набран номер, номер должен блинной 12 символов месте с "+"')
                continue
            else: 
                break
        Editing_db.work_phonee(work_phonee = work_phonee_input, id = select)
"""
run_select_4 запускает вывод всех записей построчно 

"""
def run_select_4():
    data_base.conclusion()

"""
run_select_3 запускает поиск записей

"""

def run_select_3():
    data_base.search()
    
    
