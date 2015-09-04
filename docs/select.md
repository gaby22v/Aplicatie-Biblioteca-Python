page_title: Comanda SELECT
Modulul cx_Oracle ofera posibilitatea folosirii comenzii SELECT.<br/>
Functia urmatoare selecteaza toate informatiile din tabela data:
```python
#modul Oracle
import cx_Oracle
#modul passwordbox
from easygui import passwordbox
def select_all():
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
#comanda select
    cursor.execute('select * from %s' % tablename)
#afisarea informatiilor
    for rezultat in cursor:
        print (rezultat)
#if __name__ == '__main__':
   #select_all()
```