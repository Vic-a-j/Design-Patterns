# Chain of Responsibility

_Texbook_:
"Avoid coupling the sender of a request to its receiver y giving more than one object a chance to handle the request. Chain the receiving objects and pass the request along the chain until an object handles it."<br>

---

### Problem:


---

### Structure:
![chain_of_responsibility](images/chain_of_responsibility_structure.png)

---

### Participants:
<u>**Handler:**</u><br>
- defines an interface for handling requests.<br>
- _(optional)_ implements the successor link.<br>

<u>**ConcreteHandler:**</u><br>
- handles requests it is responsible for.<br>
- can access its successor.<br>
- if the ConcreteHandler can handle the request, it does so; otherwise it forwards the request to its successor.<br>

<u>**Client:**</u><br>
- initiates the request to a ConcreteHandler object on the chain.<br>

---

### Pros and Cons:
_Pros_:

✅ <br>

_Cons_:

❌ <br>