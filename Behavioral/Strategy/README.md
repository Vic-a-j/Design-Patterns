# Strategy

_Texbook_:
"Define a family of algorithms, encapsulate each one, and make them interchangeable. Strategy lets the algorithm vary independently from clients that use it."<br>

---

### Problem:


---

### Structure:
![strategy](../Strategy/Images/strategy_structure.png)

---

### Participants
<u>**Strategy:**</u><br>
- declares an interface common to all supported algorithms. Context uses this interface to call the algorithm deined by a ConcreteStrategy.<br>

<u>**ConcreteStrategy:**</u><br>
- implements the algorithm using the Strategy interface.<br>

<u>**Context:**</u><br>
- is configured with a ConcreteStrategy object.<br>
- maintains a reference to a Strategy object.<br>
- may define an interface that lets Strategy access its data.<br>

---

### Pros and Cons
_Pros_:

✅ <br>

_Cons_:

❌ <br>