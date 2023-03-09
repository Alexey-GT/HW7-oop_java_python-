from Manager import TaskManager
import time


manager = TaskManager()
while True:
    print("""Выберите один из вариантов:
    1. Создать новую задачу
    2. Показать все задачи
    3. Показать запись в файле .txt
    4. Выйти из ежедневника""")
    choise = input(' --->>>')


    if choise == '1':
        manager.new_task()
    elif choise == '2':
        manager.show_tasks()
    elif choise == '3':
        manager.show_log()
    elif choise == "4":
        print("Закрытие ежедневника....")
        time.sleep(5)
        break
    else:
        print("Нужно выбрать один из четырех вариантов структуры выбора")
