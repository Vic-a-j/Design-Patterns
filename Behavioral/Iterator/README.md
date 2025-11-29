# Iterator

_Texbook_:
"Provide a way to access the elements of an aggregate object sequentially without exposing its underlying representation."<br>

---

### Problem:


---

### Structure:
![iterator](images/iterator_structure.png)

---

### Participants
<u>**Iterator:**</u><br>
- defines an interface for accessing and traversing elements.<br>

<u>**ConcreteIterator:**</u><br>
- implements the Iterator interface.<br>
- keeps track of the current position in the traversal of the aggregate.<br>

<u>**Aggregate:**</u><br>
- defines an interface for creating an Iterator object.<br>

<u>**ConcreteAggregate:**</u><br>
- implements the Iterator creation interface to return an instance of the proper ConcreteIterator.<br>

---

### Pros and Cons
_Pros_:

✅ <br>

_Cons_:

❌ <br>