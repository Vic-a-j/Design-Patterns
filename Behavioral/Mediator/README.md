# Mediator

_Texbook_:
"Define an object that encapsulates how a set of obuects interact. Mediator promotes loose coupling by keeping objects from referring to each other explicitly, and it lets you vary their interaction independently."<br>

---

### Problem:


---

### Structure:
![mediator](../Mediator/Images/mediator_structure.png)

---

### Participants
<u>**Mediator:**</u><br>
- defines an interface for communicating with Colleague objects.<br>

<u>**ConcreteMediator:**</u><br>
- implements cooperative behavior by coordinating Colleague objects.<br>
- knows and maintains its colleagues.<br>

<u>**Colleague classes:**</u><br>
- each Colleague class knows its mediator object.<br>
- each colleague communicates with its mediator whenever it would have otherwise communicated with another colleague.<br>

---

### Pros and Cons
_Pros_:

✅ <br>

_Cons_:

❌ <br>