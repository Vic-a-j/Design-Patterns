# Builder


_Texbook_:
"Separate the construction of a complex object from its representation so that the same construction process can create different represeentations."<br>

---

### Problem:


---

### Structure:
![builder](../Builder/Images/builder_structure.png)

---

### Participants:
<u>**Builder:**</u><br>
- specifies an abstract interface for creating parts of a Product object.<br>

<u>**ConcreteBuilder:**</u><br>
- constructs and assenbles parts of the product by implementing the Builder interface.<br>

<u>**Director:**</u><br>
- constructs an object using the Builder interface.<br>

<u>**Product:**</u><br>
- represents the complex object under construction. ConcreteBuilder builds the product's internal represntation and defines the process by which it's assembled.<br>
- includes classes that define the constituent parsts, including interfaces for assembling the parts into the final result.<br>

---

### Pros and Cons:
_Pros_:

✅ <br>

_Cons_:

❌ <br>