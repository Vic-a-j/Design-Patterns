# Factory

**Factory Method** is a creational design pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.

_Texbook_:
"Define an interface for creating an object, but let subclasses decide which class to instantiate. Factory Method lets a class defer instantiation to subclasses."<br>
a.k.a - Virtual Constructor

---

### Problem:
You want to create objects in your program, but you don’t want the rest of your code to know which specific class is being instantiated. Hard-coding object creation makes your system rigid, difficult to extend, and tightly coupled to concrete classes.

In other words, you need a way for your code to request _“give me something that behaves like X,”_
without knowing or caring about the exact concrete class.

<u>EX:</u> **🍦 Ice Cream Shop**

Imagine you are running an ice-cream shop and taking orders from people. You are direcyly asked to create various ice-cream types like _Cone()_, _Sundae()_, or _Milkshake()_. To know what someone wants, you may create multiple different **if/else** statements to create a specific type of ice-cream. Sometimes this can be redudant, and you can simply create a general **_create_dessert()_** method each desert class overrides and creates the ice-cream you want without knowing the dessert type. You can simply say - "hey, create a dessert for me" and the functionality of knowing what type of dessert is hidden from you, adding simplicity.

---

### Applicability:
- a class can't anticipate the class of objects it must create.
- a class wants its subclasses to specify the objects it creates.
- classes delegate responsibility to one of several helper subclasses, and you want to localize the knowledge of which helper subclass is the delegate.

---

### Structure:
![factory](images/factory_structure.png)

---

### Participants:
<u>**Product:**</u><br>
- defines the interface of objects the factory method creates.<br>

<u>**ConcreteProduct:**</u><br>
- implements the Product interface.<br>

<u>**Creator:**</u><br>
- declares the factory method, which returns an object of type Product. Creator may also define a default implementation of the factory method that returns a default ConcreteProduct object.<br>
- may call the factory method to create a Product object.<br>

<u>**ConcreteCreator:**</u><br>
- overrides the factory method to return an instance of a ConcreteProduct.<br>

---

### Pros and Cons:
_Pros_:

✅ You avoid tight coupling between the creator and the concrete products. <br>
✅ Single Responsibility Principle. You can move the product creation code into one place in the program, making the code easier to support. <br>
✅ Open/Closed Principle. You can introduce new types of products into the program without breaking existing client code. <br>

_Cons_:

❌ The code may become more complicated since you need to introduce a lot of new subclasses to implement the pattern. The best case scenario is when you’re introducing the pattern into an existing hierarchy of creator classes.<br>