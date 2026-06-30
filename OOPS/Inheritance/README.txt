⭐ Inheritance in Python (Full Notes)
Inheritance allows one class (child/subclass) to acquire the properties and methods of another class (parent/superclass).

It supports:

Code reusability

Extensibility

Cleaner OOP design


⭐ Summary Table

Inheritance Type	Structure	Use Case

****************************************************************
Single			A → B		Simple extension
Multilevel		A → B → C	Stepwise specialization
Multiple		A + B → C	Combining behaviors
Hierarchical		A → B, C	Categorization
Hybrid			Mix		Complex models

super() in Python is a built‑in function that lets a child class call methods from its parent class—most commonly the parent constructor (__init__).

The key idea:

super() gives you access to the parent class without naming it directly.

This is essential for clean inheritance, especially when multiple classes are involved.
