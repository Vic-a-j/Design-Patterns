# Flyweight

_Texbook_:
"Use sharing to support large numbers of fine-grained objects efficiently."<br>

---

### Problem:


---

### Structure:
![flyweight_1](images/flyweight_structure_1.png)
![flyweight_2](images/flyweight_structure_2.png)

---

### Participants:
<u>**Flyweight:**</u><br>
- declares an interface throgh which flyweights can receive and act on extrinsic state.<br>

<u>**ConcreteFlyweight:**</u><br>
- implement the Flyweight interface and adds storage for intrinsic state, if any. A ConcreteFlyweight object must be shareable. Any state it stores must be intrinsic; that is, it must be independent of the ConcreteFlyweight object's context.<br>

<u>**UnsharedConcreteFlyweight:**</u><br>
- not all Flyweight subclasses need to be shared. The Flyweight interface <u>enables</u> sharing; iot doesn't enforce it. It's common for UnsharedConcreteFlyweight objects to have ConcreteFlyweight objects as children at some level in the flyweight object structure (as the Row and Column classes have).<br>

<u>**FlyweightFactory:**</u><br>
- creates and manages flyweight objects.<br>
- ensures tat flyweights are shared properly. When a client requests a flyweight, the FlyWeightFactory object supplies an existing instance or creates one, if none exists.

<u>**Client:**</u><br>
- maintains a reference to flyweight(s).
- computes or stores the extrinsc state of flyweight(s).

---

### Pros and Cons:
_Pros_:

✅ <br>

_Cons_:

❌ <br>