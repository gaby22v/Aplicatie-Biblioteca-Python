page_title: Pornire baza de date
Modulul cx_Oracle ofera posibilitatea de a porni/opri o baza de date Oracle Database, incepand cu versiunea 10G.<br/>
Functie pentru pornirea bazei de date:
```python
import cx_Oracle
def pornire_db():
#conexiunea trebuie sa fie in modul PRELIM_AUTH
    try:
        connection = cx_Oracle.connect("/",
            mode = cx_Oracle.SYSDBA | cx_Oracle.PRELIM_AUTH)
        connection.startup()
        print("Conexiune creata!")
    except:
        print("A aparut o eroare!")
    try:
#SYSDBA
        connection = cx_Oracle.connect("/", mode = cx_Oracle.SYSDBA)
        cursor = connection.cursor()
        cursor.execute("alter database mount")
        cursor.execute("alter database open")
        print("Baza de date a fost pornita cu succes!")
    except:
        print("A aparut o eroare!")
#if __name__ == "__main__":
 #   pornire_db()
```