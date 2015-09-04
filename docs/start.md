page_title: Start
Pentru conectarea la o baza de date Oracle se foloseste modulul cx_Oracle.<br/>
Pentru instalare folositi urmatoarea comanda:
```
pip install cx_Oracle
```
 <br/>
 Exemplu de conectare la baza de date Oracle:<br/>
```python
#modulul pentru conectarea la Oracle
import cx_Oracle
#modul pentru passwordbox
from easygui import passwordbox
#preluam numele utilizatorului de la tastatura
print("Numele utilizatorului:")
user = input()
#preluam parola utilizatorului de la tastatura
print("Parola utilizatorului:")
parola = passwordbox("Parola")
#incercam sa ne conectam la Oracle si afisam
#un mesaj daca conectarea s-a realizat cu succes
try:
    connection = cx_Oracle.connect(user,parola)
    print("Conexiunea s-a realizat cu succes")
#daca utilizatorul sau parola este gresita afisam un mesaj de eroare
except:
    print("Utilizator sau parola gresita")
#inchidem conexiunea la Oracle
connection.close()
```