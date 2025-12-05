# Builder

**Builder** is a creational design pattern that lets you construct complex objects step by step. The pattern allows you to produce different types and representations of an object using the same construction code.

_Texbook_:
"Separate the construction of a complex object from its representation so that the same construction process can create different represeentations."<br>

---

### Problem:
Imagine a complex object that requires laborious, step-by-step initialization of many fields and nested objects. Such initialization code is usually buried inside a monstrous constructor with lots of parameters. Or even worse: scattered all over the client code.

<u>EX:</u> **🏠 Building a House**

Let's say you want to build a house. A house has many optional customazable parts like how many floors it has, type of roof, does it have a garage, etc. The construction aspect can be hard to replicate or can be duplicated accross multiple objects. Why construct such a complicated thing when all we want is to 1) use parts to 2) construct a whole?

The Builder pattern suggests that you extract the object construction code out of its own class and move it to separate objects called builders.

The director class defines the order in which to execute the building steps, while the builder provides the implementation for those steps.

---

### Applicability:
- the algorithm for creating a complex object should be independent of the parts that make up the object and how they're assembled.
- the construction process must allow different representations for the object that's constructed.

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

✅ You can construct objects step-by-step, defer construction steps or run steps recursively.<br>
✅ You can reuse the same construction code when building various representations of products.<br>
✅ Single Responsibility Principle. You can isolate complex construction code from the business logic of the product..<br>

_Cons_:

❌ The overall complexity of the code increases since the pattern requires creating multiple new classes.<br>