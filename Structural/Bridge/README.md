# Bridge

_Texbook_:
"Decouple an abstraction from its implementation so that the two can vary independently."<br>

---

### Problem:


---

### Structure:
![bridge](images/bridge_structure.png)

---

### Participants:
<u>**Abstraction:**</u><br>
- defines the abstraction's interface.<br>
- maintains a reference to an object of type Implementor.<br>

<u>**RefinedAbstraction:**</u><br>
- extends the interface defined by Abstration.<br>

<u>**Implementor:**</u><br>
- defines the interface for implementation classes. This interface doesn't have to correspond exactly to Abstraction's interface; in fact the two interfaces can be quite different. Typically the Implementor interface provides only primitive operations, and Abstration defines higher-level operations based on these primitives.<br>

<u>**ConcreteImplementor:**</u><br>
- implements the Implementor interface and defines its concrete implementation.<br>

---

### Pros and Cons:
_Pros_:

✅ <br>

_Cons_:

❌ <br>