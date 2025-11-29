# Decorator

_Texbook_:
"Attach additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extending functionality."<br>

---

### Problem:


---

### Structure:
![decorator](images/decorator_structure.png)

---

### Participants:
<u>**Component:**</u><br>
- defines the interface for objects taht can have responsibilities added to them dynamically.<br>

<u>**CreateComponent:**</u><br>
- defines an object to which additional responsibilities can be attached.<br>

<u>**Decorator:**</u><br>
- maintains a reference to a Component object and defines an interface that conform to Component's interface.<br>

---

### Pros and Cons:
_Pros_:

✅ <br>

_Cons_:

❌ <br>