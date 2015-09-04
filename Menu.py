#titlu          :menu.py
#descriere      :Meniu interactiv pentru lucrul cu bazele de date
#author         :Patrascu Gabriel
#date           :29/08/2015
#version        :0.1
#usage          :python menu.py
#notes          :
#python_version :3.5.0  
#--------------------------------------------------------------------------
#Module necesare pentru meniu
import sys, os
#functia pentru comanda describe
from Describe import describe
#functia pentru comanda count
from Count import count
#functia pentru comanda select
from Select import select_all
#functia pentru inchiderea bazei de date
from DatabaseShutdown import shutdown_db
#functia pentru afisarea tuturor tabelelor detinute de utilizatorul curent
from Toate_tabelele_curente import toate_tabelele_curente
#functia pentru pornirea bazei de date
from DatabaseStartup import pornire_db
#---------------------------------------------------------------------------
# definire meniu - constante
menu_actions  = {}  
#Functii meniu
def main_menu():
    os.system('cls')   
    print ("Bun venit, te rog alege meniul:")
    print ("1. Pornire baza de date")
    print ("2. Inchidere baza de date")
    print ("3. Afisarea tabelelor detinute de utilizatorul curent")
    print ("4. Comanda DESCRIBE")
    print ("5. Comanda SELECT")
    print ("6. Comanda COUNT")
    print ("0. Iesire")
    choice = input("Alegerea dvs.:")
    exec_menu(choice) 
    return
#Executarea meniu
def exec_menu(choice):
    os.system('cls')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print ("Meniul nu exista.\n")
            menu_actions['main_menu']()
    return 
#Meniul pentru pornirea bazei de date
def menu1():
    print ("Comanda care deschide baza de date\n")
    pornire_db()
    print ("9. Intoarcere la meniu")
    print ("0. Exit")
    choice = input("Comanda>>")
    exec_menu(choice)
    return
#Meniul pentru inchiderea bazei de date
def menu2():
    print ("Comanda pentru inchiderea bazei de date\n")
    print ("9. Intoarcere la meniu")
    print ("0. Iesire")
    shutdown_db()
    choice = input("Comanda>>")
    exec_menu(choice)
    return
#Meniul pentru afisarea tabelelor detinute de utilizatorul curent
def menu3():
    print ("Afisarea tabelelor detinute de utilizatorul curent\n")
    print ("9. Intoarcere la meniu")
    print ("0. Iesire")
    toate_tabelele_curente()
    choice = input("Comanda>>")
    exec_menu(choice)
    return
#Meniul pentru comanda DESCRIBE
def menu4():
    print ("Bun venit in meniul DESCRIBE\n")
    print ("9. Intoarcere la meniu")
    print ("0. Iesire")
    describe()
    choice = input("Comanda>>")
    exec_menu(choice)
    return
#Meniul pentru comanda SELECT
def menu5():
    print ("Bun venit in meniul SELECT\n")
    print ("9. Intoarcere la meniu")
    print ("0. Iesire")
    select_all()
    choice = input("Comanda>>")
    exec_menu(choice)
    return
#Meniul pentru comanda COUNT
def menu6():
    print ("Bun venit in meniul COUNT\n")
    print ("9. Intoarcere la meniu")
    print ("0. Iesire")
    count()
    choice = input("Comanda>>")
    exec_menu(choice)
    return
# Back to main menu
def back():
    menu_actions['main_menu']() 
# Exit program
def exit():
    sys.exit() 
#Definire meniu
menu_actions = {
    'main_menu': main_menu,
    '1': menu1,
    '2': menu2,
    '3': menu3,
    '4': menu4,
    '5': menu5,
    '6': menu6,
    '9': back,
    '0': exit,
}
# Main Program
if __name__ == "__main__":
    # Launch main menu
    main_menu()

