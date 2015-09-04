page_title: Inchidere baza de date
Functie pentru oprirea unei baze de date Oracle:
```python
#modulul pentru Oracle
import cx_Oracle
def shutdown_db():
#conectare ca SYSDBA or SYSOPER
    try:
        connection = cx_Oracle.connect("/", mode = cx_Oracle.SYSDBA)
        print("Conexiune realizata!")
    except:
        print("Conexiunea nu s-a putut realiza!")
#apelare functie shutdown
    try:
        connection.shutdown(mode = cx_Oracle.DBSHUTDOWN_IMMEDIATE)
        print("25% Complet")
    except:
        print("A aparut o eroare!")
#deconectare baza de date
    try:
        cursor = connection.cursor()
        cursor.execute("alter database close normal")
        cursor.execute("alter database dismount")
        print("75% Complet")
    except:
        print("A aparut o eroare!")
#final shutdown
    try:
        connection.shutdown(mode = cx_Oracle.DBSHUTDOWN_FINAL)
        print("100% Complet. Baza de date a fost inchisa cu succes!")
    except:
        print("Baza de date nu a fost inschisa!")
#if __name__ == "__main__":
#    shutdown_db()
```
 