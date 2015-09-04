page_title: Comanda SQL COUNT
Pentru a calcula numarul inregistrarilor dintr-o tabela folosim COUNT.<br/>
Prin intermediul cx_Oracle putem crea o functie foarte simpla:
```python
#modul Oracle
import cx_Oracle
#modul passwordbox
from easygui import passwordbox
def count():
#cerem numele utilizatorului
    print("Numele utilizatorului:")
    user = input()
#cerem parola utilizatorului
    parola = passwordbox("Parola utilizatorului")
#conectarea la Oracle
    conexiune = cx_Oracle.connect(user,parola)
#functie care afiseaza numar de inregistrari dintr-o tabela data
#utilizatorul trebuie sa introduca numele tabelei
    print("Numele tabelei")
    tablename = input()
#cursor
    cursor = conexiune.cursor()
#comanda describe
    cursor.execute('select count(*) from %s' % tablename)
    count = cursor.fetchall()[0][0]
#afisarea informatiilor
    print("Numarul de inregistrari din tabela", tablename, "este" , count)
#if __name__ == '__main__':
   #count()

```