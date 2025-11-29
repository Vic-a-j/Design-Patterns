# Observer

_Texbook_:
"Define a one-to-many dependency between objects so that when one object change state, all its dependents are notified and updated automatically."<br>

---

### Problem:

---

### Structure:
![observer](images/observer_structure.png)

---

### Participants:
<u>**Subject:**</u><br>
- knows its observers. Any number of Observer objects may observe a subject.<br>
- provides an interface for attaching and detaching Observer objects.<br>

<u>**Observer:**</u><br>
- defines an updating interface for objects that should be notified of changes in a subject.<br>

<u>**ConcreteSubject:**</u><br>
- stores state of interest to ConcreteObserver objects.<br>
- sends a notification to its observers when its state changes.<br>

<u>**ConcreteObserver:**</u><br>
- maintains a reference to a ConcreteSubject object.<br>
- stores state that should stay consistent with the subject's.<br>
- implement the Observer updating interface to keep its state consisten with the subject's.<br>

---

### Pros and Cons:
_Pros_:

✅ <br>

_Cons_:

❌ <br>