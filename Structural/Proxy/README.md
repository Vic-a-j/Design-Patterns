# Proxy

_Texbook_:
"Provide a surrogate or placeholder for another object to control access to it."<br>


---

### Problem:


---

### Structure:
![proxy](../Proxy/Images/proxy_structure.png)

---

### Participants:
<u>**Proxy:**</u><br>
- maintains a reference that lets the proxy access the real subject. Proxy may refer to a Subject if the RealSubject and Subject interfaces are the same.<br>
- provides an interface identical to Subject's so that a proxy can be substituted for the real subject.<br>
- controls access to the real subject and may be responsible for creating and deleting it.<br>
- other responsibilities depend on the kind of proxy:<br>
<t>1) **<i>Remote Proxies</i>** are responsible for encoding a request and its arguments and for sending the encoded request to the real subject in a different address space.<br>
<t>2) **<i>Virtual Proxies</i>** may cache additional information about the real subject so that they can postpone accessing it. For example, the ImageProxy form the Motivation caches the real image's extend.<br>
<t>3) **<i>Protection Proxies</i>** check that the caller has the access permissions required to perform a request.<br>

<u>**Subject:**</u><br>
- defines the common interface for RealSubject and Proxy so that a Proxy can be used anywhere a RealSubject is expected.<br>

<u>**RealSubject:**</u><br>
- defines the real object that the proxy represents.<br>

---

### Pros and Cons:
_Pros_:

✅ <br>

_Cons_:

❌ <br>