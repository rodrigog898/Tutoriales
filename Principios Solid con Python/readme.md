# Principios SOLID con Ejemplos en Python

## 🧱 Principios SOLID

SOLID es un acrónimo de cinco principios de diseño orientado a objetos que ayudan a escribir código más mantenible, escalable y flexible.

---

### 1. **S - Single Responsibility Principle (SRP)**
> Una clase debe tener **una única razón para cambiar**, es decir, **una sola responsabilidad**.

#### ❌ Mal ejemplo:
```python
class Report:
    def generate(self):
        print("Generating report...")

    def save_to_file(self):
        with open("report.txt", "w") as f:
            f.write("Report content")
```

#### ✅ Buen ejemplo:
```python
class Report:
    def generate(self):
        return "Report content"

class ReportSaver:
    def save_to_file(self, content):
        with open("report.txt", "w") as f:
            f.write(content)
```

---

### 2. **O - Open/Closed Principle (OCP)**
> El código debe estar **abierto para extensión, pero cerrado para modificación**.

#### ❌ Mal ejemplo:
```python
class PaymentProcessor:
    def pay(self, payment_type):
        if payment_type == "paypal":
            print("Paying with PayPal")
        elif payment_type == "creditcard":
            print("Paying with Credit Card")
```

#### ✅ Buen ejemplo:
```python
class PaymentMethod:
    def pay(self):
        raise NotImplementedError

class PayPal(PaymentMethod):
    def pay(self):
        print("Paying with PayPal")

class CreditCard(PaymentMethod):
    def pay(self):
        print("Paying with Credit Card")

def process_payment(payment_method: PaymentMethod):
    payment_method.pay()
```

---

### 3. **L - Liskov Substitution Principle (LSP)**
> Las subclases deben poder usarse en lugar de sus clases base **sin alterar el comportamiento del programa**.

#### ❌ Mal ejemplo:
```python
class Bird:
    def fly(self):
        print("Flying")

class Ostrich(Bird):
    def fly(self):
        raise Exception("Ostrich can't fly")
```

#### ✅ Buen ejemplo:
```python
class Bird:
    def make_sound(self):
        print("Tweet")

class FlyingBird(Bird):
    def fly(self):
        print("Flying")

class Ostrich(Bird):
    pass

class Sparrow(FlyingBird):
    pass
```

---

### 4. **I - Interface Segregation Principle (ISP)**
> Los clientes no deben estar obligados a depender de **interfaces que no usan**.

#### ❌ Mal ejemplo:
```python
class Animal:
    def fly(self): pass
    def swim(self): pass
    def walk(self): pass
```

#### ✅ Buen ejemplo:
```python
class Walker:
    def walk(self): pass

class Swimmer:
    def swim(self): pass

class Flyer:
    def fly(self): pass

class Duck(Walker, Swimmer, Flyer):
    pass

class Dog(Walker, Swimmer):
    pass
```

---

### 5. **D - Dependency Inversion Principle (DIP)**
> Depende de **abstracciones, no de concreciones**.

#### ❌ Mal ejemplo:
```python
class MySQLDatabase:
    def connect(self):
        print("Connecting to MySQL")

class App:
    def __init__(self):
        self.db = MySQLDatabase()
```

#### ✅ Buen ejemplo:
```python
class Database:
    def connect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        print("Connecting to MySQL")

class App:
    def __init__(self, db: Database):
        self.db = db

# Uso
db = MySQLDatabase()
app = App(db)
```
