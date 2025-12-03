# Abstract Factory

**Abstract Factory** is a creational design pattern that lets you produce families of related objects without specifying their concrete classes.

_Texbook_:
"Provide an interface for creating families of related or dependent objects without specifying their concrete classes."<br>
a.k.a - A factory of factories

---

### Problem:
Many systems need to work with **families of related objects** that must be used together.
These objects are designed to be **compatible** with one another, but different families should not be mixed.

<u>EX:</u> **💻 <span style="color: purple;">Mac</span> vs. <span style="color: green;">Windows</span> 🖥️**

A MacBook expects peripherals—keyboards, monitors, trackpads, chargers—that follow Apple-specific protocols and configurations. A Windows laptop expects a completely different family of devices built around Windows drivers, system APIs, and hardware standards. Even though both laptops use the same types of devices, their implementations aren’t interchangeable.

This is the exact type of problem the Abstract Factory pattern solves: it provides a clean way to create entire families of related, compatible objects for each platform—ensuring that the Mac family stays together, the Windows family stays together, and the application remains flexible.

---

### Applicability:
- a system should be independent of how its products are created, composed, and represented.
- a system should be configured with one of multiple families of products.
- a family of related product objects is designed to be used together, and you need to enforce this constraint.
- you want to provide a class library of produts, and you want to reveal just their intefaces, not their implementations.

---

### Structure:
![abstract_factory](../Abstract%20Factory/Images/abstractfactory_structure.png)

---

### Participants:
<u>**AbstractFactory:**</u><br>
- declares an interface for operations that create abstract product objects.<br>

<u>**ConcreteFactory:**</u><br>
- implements the operations to create concrete product objects.<br>

<u>**AbstractProduct:**</u><br>
- declares an interface for a type of product object.<br>

<u>**ConcreteProduct:**</u><br>
- defines a product object to be created by the corresponding concrete factory.<br>
- implements the AbstractProduct interface.<br>

<u>**Client:**</u><br>
- uses only interfaces desclared by AbstractFactory and AbstractProduct classes.<br>

---

### Pros and Cons:
_Pros_:

✅ You can be sure that the products you’re getting from a factory are compatible with each other.<br>
✅ You avoid tight coupling between concrete products and client code.<br>
✅ Single Responsibility Principle. You can extract the product creation code into one place, making the code easier to support.<br>
✅ Open/Closed Principle. You can introduce new variants of products without breaking existing client code.<br>

_Cons_:

❌ The code may become more complicated than it should be, since a lot of new interfaces and classes are introduced along with the pattern.<br>