# Factory

_Texbook_:
"Define an interface for creating an object, but let subclasses decide which class to instantiate. Factory Method lets a class defer instantiation to subclasses."<br>

---

### Problem:

---


### Structure:
![factory](images/factory_structure.png)

---

### Participants:
<u>**Product:**</u><br>
- defines the interface of objects the factory method creates.<br>

<u>**ConcreteProduct:**</u><br>
- implements the Product interface.<br>

<u>**Creator:**</u><br>
- declares the factory method, which returns an object of type Product. Creator may also define a default implementation of the factory method that returns a default ConcreteProduct object.<br>
- may call the factory method to create a Product object.<br>

<u>**ConcreteCreator:**</u><br>
- overrides the factory method to return an instance of a ConcreteProduct.<br>

---

### Pros and Cons:
_Pros_:

✅ <br>

_Cons_:

❌ <br>