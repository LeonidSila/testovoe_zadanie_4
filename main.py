import soft # Импортирование рабочей папки

while True: # Создание базавого меню для работы
    select = soft.client.user_selection() #Запуск меню с информацей о выборе
    if select == 1:
        soft.client.run_select_1()
    if select == 2:
        soft.client.run_select_2()
    if select == 3:
        soft.client.run_select_3()
    if select == 4:
        soft.client.run_select_4()
    if select == 5:
        break



