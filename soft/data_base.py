import sqlite3

conn = sqlite3.connect('dbtest.sql')
cursor = conn.cursor() 


"""
conn = sqlite3.connect('dbtest.sql')
cursor = conn.cursor() 

Подключение к базе данных

"""
class Editing_db: # Создание класса для удобной работы с базой данных
    def surname_db(surname, id):
        cursor.execute('UPDATE test_work set surname = ? where id = ?', (surname, id))
        conn.commit()
    def middle_name_db(middle_name, id):
        cursor.execute('UPDATE test_work set middle_name = ? where id = ?', (middle_name, id))
        conn.commit()
    def name_db(name, id):
        cursor.execute('UPDATE test_work set name = ? where id = ?', (name, id))
        conn.commit()
    def company_db(company, id):
        cursor.execute('UPDATE test_work set company = ? where id = ?', (company, id))
        conn.commit()
    def privat_phone_db(privat_phone, id):
        cursor.execute('UPDATE test_work set privat_phone = ? where id = ?', (privat_phone, id))
        conn.commit()
    def work_phonee(work_phonee, id):
        cursor.execute('UPDATE test_work set work_phonee = ? where id = ?', (work_phonee, id))
        conn.commit()

def initialization(): # Созадние БД если ее нет
    conn = sqlite3.connect('dbtest.sql')
    cursor = conn.cursor()   
    cursor.execute('CREATE TABLE IF NOT EXISTS test_work (id int AUTO_INCREMENT primary key, surname varchar(45), middle_name varchar(45), name varchar(45), company varchar(45), privat_phone varchar(45), work_phonee varchar(45))')
    conn.commit()
    return cursor
        
def id_all(): # Вывод всех строк в базе данных 
    cursor.execute('SELECT COUNT(*) FROM test_work')
    data = cursor.fetchone()
    data = data[0]
    conn.commit()
    return data

def conclusion_select_2(data): # Вывод построчно всех строк из БД
    print('ID, surname, middle_name, name, company, privat_phone, work_phonee')
    for i in range(1, data + 1):
        cursor.execute('SELECT * FROM test_work WHERE id = ?', (i, ))
        data = cursor.fetchone()
        print(data)
        conn.commit()
        

def add_ad(surname, middle_name, name, company, privat_phone, work_phonee):
    cursor.execute('INSERT INTO test_work (surname, middle_name, name, company, privat_phone, work_phonee) VALUES (?, ?, ?, ?, ?, ?)', (surname, middle_name, name, company, privat_phone, work_phonee))
    conn.commit()
"""
Функция add_add Добавляет новую запись в БД

"""

def conclusion(): # Вывод построчно всех строк из БД
    cursor.execute('SELECT COUNT(*) FROM test_work')
    data = cursor.fetchone()
    data = data[0]
    print('ID, surname, middle_name, name, company, privat_phone, work_phonee')
    for i in range(1, data + 1):
        cursor.execute('SELECT * FROM test_work WHERE id = ?', (i, ))
        data = cursor.fetchone()
        print(data)
        conn.commit()

def search(): # Поиск в БД
    while True:
        user_input = input("Ведите, то что хотите найти>>>")
        cursor.execute('SELECT * FROM test_work WHERE LOWER (surname) LIKE ?', (user_input, ))
        surname = cursor.fetchone()
        cursor.execute('SELECT * FROM test_work WHERE LOWER (middle_name) LIKE ?', (user_input, ))
        middle_name = cursor.fetchone()
        cursor.execute("SELECT * FROM test_work WHERE LOWER (name) LIKE ?", (user_input, ))
        name = cursor.fetchone()
        cursor.execute("SELECT * FROM test_work WHERE LOWER (company) LIKE ?", (user_input, ))
        company = cursor.fetchone()
        cursor.execute("SELECT * FROM test_work WHERE privat_phone LIKE ?", (user_input, ))
        privat_phone = cursor.fetchone()
        cursor.execute("SELECT * FROM test_work WHERE work_phonee LIKE ?", (user_input, ))
        work_phonee = cursor.fetchone()
        if surname != None:
            print(surname)
            break
        if middle_name != None:
            print(middle_name)
            break
        if name != None:
            print(name)
            break
        if company != None:
            print(company)
            break
        if privat_phone != None:
            print(privat_phone)
            break
        if work_phonee != None:
            print(work_phonee)
            break
        print ('Ничего не нашли')
        user_input_s = int(input("1: Продолжить поиск\n2: Выйти\n>>>>"))
        if user_input_s == 1:
            continue
        if user_input_s == 2:
            break


