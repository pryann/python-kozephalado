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
```

Készíts gettert a `fname` és `lname`-hez, és mindegyiket nagybetűsen adja vissza!