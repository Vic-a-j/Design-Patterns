# State

_Texbook_:
"Allow an object to alter its behavior when its internal state changes. The object will appear to change its class."<br>

---

### Problem:

---

### Structure:
![state](images/state_structure.png)

---

### Participants:
<u>**Context:**</u><br>
- defines the interface of interest to clients.<br>
- maintains an instance of a ConcreteState subclass that defines the current state.<br>

<u>**State:**</u><br>
- defines an interface for encapsulating the behavior associated with a particular state of the Context.<br>

<u>**ConcreteState subclasses:**</u><br>
- each subclass implements a behavior associated with a state of the Context.<br>

---

### Pros and Cons:
_Pros_:

✅ <br>

_Cons_:

❌ <br>