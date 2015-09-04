#modul Oracle
#afisare toate tabelele detinute de utilizatorul curent
import cx_Oracle
#modul passwordbox
from easygui import passwordbox
def toate_tabelele_curente():
#cerem numele utilizatorului
    print("Numele utilizatorului:")
    user = input()
#cerem parola utilizatorului
    parola = passwordbox("Parola utilizatorului")
#conectarea la Oracle
    conexiune = cx_Oracle.connect(user,parola)
#functie care afiseaza structura unei tabele date
#cursor
    cursor = conexiune.cursor()
#comanda describe
    cursor.execute("select tablespace_name, table_name from user_tables")
#afisarea informatiilor
    for rezultat in cursor:
        print(rezultat)
#if __name__ == '__main__':
    #toate_tabelele_curente()
