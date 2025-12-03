# Interpreter

_Texbook_:
"Given a language, define a representation for its grammar along with an interpreter that uses the representation to interpret sentences in the language."<br>

---

### Problem:


---

### Structure:
![interpreter](../Interpreter/Images/interpreter_structure.png)

---

### Participants:
<u>**AbstractExpression:**</u><br>
- declares an abstract Interpret operation that is common to all nodes in the abstract syntax tree.<br>

<u>**TerminalExpression:**</u><br>
- implements an Interpret operation associated with terminal symbols in the grammar.<br>
- an instance is required for every terminal symbol in a sentence.<br>

<u>**NonterminalExpression:**</u><br>
- one such class is required for every rule {R::== R_1, R_2...R_n} in the grammar.<br>
- maintains instance variables of tyope AbstractExpression for eahc of the symbols R1 through Rn.<br>
- implements an Interpret operation for nonterminal symbols in the grammar. Interpret typically calls itself recursively on the variables representing R1 through Rn.<br>

<u>**Context:**</u><br>
- contains information that's global to the interpreter.<br>

<u>**Client:**</u><br>
- builds _(or is given)_ an abstract syntax tree representing a particular sentence in the language that the grammar defines. The abstract syntax tree is assembled from instances of the NontermialExpression and TerminalExpression classess<br>
- invokes the Interpret operation.<br>

---

### Pros and Cons:
_Pros_:

✅ <br>

_Cons_:

❌ <br>