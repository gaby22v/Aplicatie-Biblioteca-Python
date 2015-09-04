#modulul pentru conectarea la Oracle
import cx_Oracle
#modulul pentru lucrul cu timpul
import time
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
    start = time.time()
    connection = cx_Oracle.connect(user,parola)
    elapsed = (time.time() - start)
    print("Conexiunea s-a realizat cu succes")
    #print("Conexiunea s-a realizat in:",elapsed, "secunde")
#daca utilizatorul sau parola este gresita afisam un mesaj de eroare
except:
    print("Utilizator sau parola gresita")
#inchidem conexiunea la Oracle
connection.close()
