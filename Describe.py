#modul Oracle
import cx_Oracle
#modul passwordbox
from easygui import passwordbox
def describe():
#cerem numele utilizatorului
    print("Numele utilizatorului:")
    user = input()
#cerem parola utilizatorului
    parola = passwordbox("Parola utilizatorului")
#conectarea la Oracle
    conexiune = cx_Oracle.connect(user,parola)
#functie care afiseaza structura unei tabele date
#utilizatorul trebuie sa introduca numele tabelei
    print("Numele tabelei")
    tablename = input()
#cursor
    cursor = conexiune.cursor()
#comanda describe
    cursor.execute('select * from %s where 1=0' % tablename)
    print("Nume coloana\t", "NULL\t", "Tip\t", "Lungime\t")
#afisarea informatiilor
    for desc in cursor.description:
        column_name = desc[0]
        nullable = desc[6]
        data_type = desc[1].__name__
        data_length = desc[3]
        print (column_name, "\t",  nullable, "\t", data_type, "\t", data_length, "\t",)
#if __name__ == '__main__':
   # describe()
