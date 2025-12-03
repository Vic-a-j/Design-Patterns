# Command

_Texbook_:
"Encapsulate a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations."<br>

---

### Problem:


---

### Structure:
![command](../Command/Images/command_structure.png)

---

### Participants:
<u>**Command:**</u><br>
- declares an interface for executing an operation.<br>

<u>**ConcreteCommand:**</u><br>
- defines a binding between a Receiver object and an action.<br>
- inmplements Execute by invoking the corresponding operation(s) on Receiver.<br>

<u>**Client:**</u><br>
- creates a ConcreteCommand object and sets its receiver.<br>

<u>**Invoker:**</u><br>
- aks the command to carry out the request.<br>

<u>**Receiver:**</u><br>
- knows how to perform the operations associated with carrying out a request. Any class may serve as a Receiver.<br>

---

### Pros and Cons:
_Pros_:

✅ <br>

_Cons_:

❌ <br>