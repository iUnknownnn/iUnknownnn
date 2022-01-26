from json import load

user_choice=-1
tasks=[]
categories=["Bez kategorii"]
def load_file():
    try:
        file=open("to-do-list.txt")
        task_index=1
        for line in file.readlines():
            tasks.append(line.lstrip(str(task_index)+". ").capitalize().rstrip('\n'))
            task_index+=1
        file.close()
    except FileNotFoundError:
        return

def show_tasks():
    if len(tasks)==0:
        print("Lista jest pusta")
    else:
        task_index=1
        print("Lista zadań:")
        for task in tasks:
            print(str(task_index)+". "+task.capitalize())
            task_index+=1

def add_task():
    new_task=str(input("Podaj nowe zadanie: "))
    tasks.append(new_task)
    print("Zadanie zostało dodane")

def delete_task():
    if len(tasks)==0:
        print("Lista jest pusta")
    else:
        show_tasks()
        task_to_delete=int(input("Które zadanie usunąć? "))
        try:
            tasks.pop(task_to_delete-1)
            print("Zadanie zostało usunięte")
        except IndexError:
            print("Nie ma takiego zadania")

def show_categories():
    if len(categories)==1:
        print("Lista kategorii jest pusta")
    else:
        category_index=1
        print("Lista kategorii:")
        for category in categories:
            print(str(category_index)+". "+category.capitalize())
            category_index+=1

def add_category():
    new_category=str(input("Podaj nową kategorię: "))
    categories.append(new_category)
    print("Kategoria została dodana")

def delete_category():
    if len(categories)==1:
        print("Lista kategorii jest pusta")
    else:
        show_categories()
        category_to_delete=int(input("Którą kategorię usunąć? "))
        if category_to_delete==1:
            print("Nie można usunąć podstawowej kategorii")
        else:
            try:
                categories.pop(category_to_delete-1)
                print("Kategoria została usunięta")
            except IndexError:
                print("Nie ma takiej kategorii")

def save_file():
    file=open("to-do-list.txt", "w+")
    task_index=1
    for task in tasks:
        file.write(str(task_index)+". "+task.capitalize()+"\n")
        task_index+=1
    file.close()
    print("Lista została zapisana")

load_file()
while user_choice!=8:
    if user_choice==1:
        show_tasks()
    if user_choice==2:
        add_task()
    if user_choice==3:
        delete_task()
    if user_choice==4:
        show_categories()
    if user_choice==5:
        add_category()
    if user_choice==6:
        delete_category()
    if user_choice==7:
        save_file()
    print()
    print("----TO DO LIST----")
    print("1. Pokaż zadania")
    print("2. Dodaj zadanie")
    print("3. Usuń zadanie")
    print("4. Pokaż kategorie")
    print("5. Dodaj kategorie")
    print("6. Usuń kategorie")
    print("7. Zapisz zmiany")
    print("8. Wyjdź")
    user_choice=int(input("Wybierz liczbę: "))
    print()