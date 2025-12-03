# Template

_Texbook_:
"Define the skeleton of an algorithm in an operation, deferring some steps to cubclasses. Template lets subclasses redefine certain steps of an algorihtn without changing the algorithm's structure."<br>

---

### Problem:


---

### Structure:
![template](../Template/Images/template_structure.png)

---

### Participants:
<u>**AbstractClass:**</u><br>
- defines abstract **primitive operations** that concrete subclasses define to implement steps of an algorithm.<br>
- implements a template method defining the skeleton of an algorithm. The template method calls primitive operations as well as operations defined in AbstractClass or those of other objects.<br>

<u>**ConcreteClass:**</u><br>
- implements the primitive operations to carry out subclass-specific steps of the algorithm.<br>

---

### Pros and Cons
_Pros_:

✅ <br>

_Cons_:

❌ <br>