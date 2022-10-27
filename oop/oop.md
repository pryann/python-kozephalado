# 1. feladatsor - OOP
## Személyek típusa

Írj egy Python programot ami képes személyek adatát tárolni a memóriában. A megvalósításban használj osztályt (`Person` néven).

A Person típusban el kell tudni tárolni a személy kereszt- és vezetéknevét, életkorát, címét (használj példány változókat a következő neveken:)

`fname, lname, age, address`

```python
class Person:
    def __init__(self, fname, lname, age, address):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.address = address

    def get_fname():
      return self.fname.upper()

    
    def get_lname():
      return self.lname.upper()
```

Készíts gettert a `fname` és `lname`-hez, és mindegyiket nagybetűsen adja vissza!
# 2. feladatsor - Öröklődés

Egészítsük ki a `Person` példát egy `Employee` és egy `Manager` leszármazott osztállyal.

Az `Employee` osztály egy olyan személyt valósít meg aki alkalmazott. Ennek megfelelően kell tárolnod a fizetését és a beosztását, és főnökét (`Manager`). (használj példány változókat)

`fname, lname, age, address, salary, role, manager`

Nem mindenkinek van egyből főnöke, legyen ez opcionálisan megadható. Ha valaki példányosítás után akarja megadni, legyen erre egy `set_manager` belső funkció a `Employee` osztályon.

---


A `Manager` osztály egy olyan személyt valósít meg aki foglalkoztat `Employee`kat. Tárolj a `Manager` osztályban egy `Employee` listat ami a beosztottakat tartalmazza. Legyen egy olyan függvénye, ami kiírja az összes beosztottját (`print_employees`).

`fname, lname, age, address, employees`