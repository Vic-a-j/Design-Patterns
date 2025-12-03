# Composite

_Texbook_:
"Compose objects into tree structures to represent part-whole hierarchies. Composite lets clients treat individual objects and compositions of object uniformly."<br>

---

### Problem:


---

### Structure:
![composite_1](../Composite/Images/composite_structure_1.png)
![composite_2](../Composite/Images/composite_structure_2.png)

---

### Participants:
<u>**Component:**</u><br>
- defines the domain-specific interface that Client uses.<br>

<u>**Leaf:**</u><br>
- collaborates with objects conforming to the Target interface.<br>

<u>**Composite:**</u><br>
- defines an existing interface that needs adapting.<br>

<u>**Client:**</u><br>
- adapts the interface of Adaptee to the Target interface.<br>

---

### Pros and Cons:
_Pros_:

✅ <br>

_Cons_:

❌ <br>