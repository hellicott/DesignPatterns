# Design Patterns
## Contents
[Creational Design Patterns](#creational)
- [Singleton](#singleton)

[Structural Design Patterns](#structural)
- [Thing 1](Link 1)

[Behavioural Design Patterns](#behavioural)
- [Thing 1](link 1)

## Creational
### Singleton
[[code](singleton_pattern)]

#### What is it?
A class which can only have one instance.

#### When is it useful?
An application needs only one instance of an object which can be globally accessed.

A common use for the singleton pattern is for logging. Often you want one instance
of the logging class in your program, but wish to use it throughout. Therefore you
benefit from having a global single instance of this class.

#### When is it not useful?
It shouldn't be used as a global variable. Whilst it acts like one, you should really be asking yourself
> Why do I want to make this thing global?

Not 
> How can I make this thing global?

This is a code smell, implying bad design. 

[[Back To Top](#design-patterns)]
## Structural


[[Back To Top](#design-patterns)]
## Behavioural


[[Back To Top](#design-patterns)]

# References
[source making](https://sourcemaking.com/design_patterns)

[geeks for geeks](https://www.geeksforgeeks.org/software-design-patterns/)

[toptal](https://www.toptal.com/python/python-design-patterns)

[[Back To Top](#design-patterns)]