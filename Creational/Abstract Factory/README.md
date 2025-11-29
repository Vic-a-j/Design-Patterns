# Abstract Factory

**Abstract Factory** is a creational design pattern that lets you produce families of related objects without specifying their concrete classes.

_Texbook_:
"Provide an interface for creating families of related or dependent objects without specifying their concrete classes."<br>
a.k.a - A factory of factories


### Problem:



### Structure


### Participants


### Pros and Cons
_Pros_:

✅ You can be sure that the products you’re getting from a factory are compatible with each other.<br>
✅ You avoid tight coupling between concrete products and client code.<br>
✅ Single Responsibility Principle. You can extract the product creation code into one place, making the code easier to support.<br>
✅ Open/Closed Principle. You can introduce new variants of products without breaking existing client code.<bre>

_Cons_:

❌ The code may become more complicated than it should be, since a lot of new interfaces and classes are introduced along with the pattern.<br>