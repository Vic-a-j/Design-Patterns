# Facade

_Texbook_:
"Provide a unified interface to a set of interfaces in a subsystem. Facade defines a higher-level interface that makes the subsystem easier to use."<br>


---

### Problem:


---

### Structure:
![facade](images/facade_structure.png)

---

### Participants:
<u>**Facade:**</u><br>
- knows which subsystem classes are responsible for a request.<br>
- delegates client requests to appropriate subsystem objects.

<u>**_subsystem classes:_**</u><br>
- implement subsystem functionality.<br>
- handle work assigned by the Facade object.<br>
- have no knowledge of the facade; taht is, they keep no references to it.

---

### Pros and Cons:
_Pros_:

✅ <br>

_Cons_:

❌ <br>