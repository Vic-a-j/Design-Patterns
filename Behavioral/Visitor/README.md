# Visitor

_Texbook_:
"Represent an operation to be performed on the elements of an object structure. Visitor lets you define a nwe operation without changing the classes of the elements on which it operates."<br>

---

### Problem:


---

### Structure:
![visitor](images/visitor_structure.png)

---

### Participants:
<u>**Visitor:**</u><br>
- declares a Visit operation for each class of ConcreteElement in the object structure. The operation's name and signature identifies the class that sends the Visit request to the visitor. That lets the visitor determine the concrete class of the element being visited. Then the visitor can access the element directly through its particular interface.<br>

<u>**ConcreteVisitor:**</u><br>
- implements each operation declared by Visitor. Each operation implements a fragment of the algorithm defined for the corresponding class of object in the structure. ConcreteVisitor provides the context for the algorithm and stoes its local state. This state often accumulates results during the trraversal of the structure.<br>

<u>**Element:**</u><br>
- defines an Accept operation that takes a visitor as an argument.<br>

<u>**ConcreteElement:**</u><br>
- implements an Accept operation that takes a visitor as an argument.<br>

<u>**ObjectStructure:**</u><br>
- can enumerate its elements.<br>
- may provide a high-level interface to allow the visitor to visit its elements.<br>
- may either be a composite or a collection such as a list or a set.<br>

---

### Pros and Cons
_Pros_:

✅ <br>

_Cons_:

❌ <br>